from openai import OpenAI
from dotenv import load_dotenv
import random
import json

load_dotenv()

class QuestionBuilder():
    def __init__(self):
        self.categories = ["math", "reading", "vocabulary"]
        self.math = 0
        self.reading = 0
        self.vocabulary = 0
        self.questions = []

    def send_ui_client(self, json_object):
        """this is just a dummy method that would include the logic to send the json to the ui"""

    def generate_all_questions(self):
        """creates 15 SAT questions in valid json format"""
        for _ in range(15):
            category = self.next_category()
            json_object = self.generate_valid_json_question(category)
            self.questions.append(json_object)
            self.send_ui_client(json_object)

    def generate_valid_json_question(self, category):
        """
           ensures that the response is valid json, or recursively calls another generation
           in practice we would want to have some type of max_attempts so this does not
           continue infinitely and return an error if the max attempts are reached
        """
        response = self.generate(category)
        json_string = response.choices[0].message.content
        try:
            json_object = json.loads(json_string)
            return json_object
        except json.JSONDecodeError:
            self.generate_valid_json_question(category)

    def rubric_for(self, category):
        """returns rubric instructions for each category"""
        if category == "vocabulary":
            return """
                - Select words that are challenging yet appropriate for high school students preparing for the SAT.
                - Include a mix of word types (nouns, verbs, adjectives, etc.) and themes.
                - ...
            """

    def total_questions_generated(self):
        """returns a count of the total questions"""
        return self.math + self.reading + self.vocabulary

    def next_category(self):
        """randomly selects a category, ensures that 5 questions are generated for each category"""
        if self.total_questions_generated() != 15:
            category = self.pick_category()
            if getattr(self, category) == 5:
                self.next_category()
            else:
                current_count = getattr(self, category)
                setattr(self, category, current_count + 1)
                return category

    def pick_category(self):
        """random category selection"""
        return random.choice(self.categories)

    def generate(self, category):
        """
           calls the openai api with the detailed prompt
           the AI returns a valid json object for one question in that category
        """
        client = OpenAI()
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.prompt(category)
                }
            ],
            model="gpt-3.5-turbo"
        )
        return response

    def prompt(self, category):
        """the detailed prompt we send to the ai, customized for the specific category"""
        prompt_text = f""""
            You are an expert tutor with excellent knowledge of the Scholastic Aptitude Test (SAT). Your job is to generate sample {category} test questions for a student who is practicing for the {category} section of the SAT. Each question should have four possible answer choices. Only one choice should be correct and the other three choices should be incorrect. Mix up the order of the correct choice in each question so it appears in a different location in the sequence each time. Each response should be in valid json format. Please include the following key value pairs:
            <question_number>:<{self.total_questions_generated()}>
            <category_name>:<{category}>
            <question_text>:<question text goes here>
            <answer_choices>:<answer choices go here>
            <correct_choice>:<the key of the correct choice goes here>

            The format of the answer choices should be:
                <choice_1>:<choice one text goes here>
                <choice_2>:<choice two text goes here>
                <choice_3>:<choice three text goes here>
                <choice_4>:<choice four text goes here>

            Here is an example of valid json to you might respond with for a sample question in the math category:

            {{
                "question_number":{self.total_questions_generated()},
                "category_name":"math",
                "question_text":"What is 1 + 1 equal to?",
                "answer_choices": {{
                    "choice_1": "1",
                    "choice_2": "7",
                    "choice_3": "2",
                    "choice_4": "0"
                }},
                "correct_choice":"choice_4"
            }}

            Don't actually use this sample question, generate your own but use this format.

            Please double check the json format to ensure it is valid json before responding with the sample question. If it is invalid, fix it before responding.

            When you are generating sample {category} questions, please follow this rubric:

            {self.rubric_for(category)}

            Let's think step by step:
            1. use your expert SAT knowledge to generate a sample {category} question with 4 potential answer choices. Three choices should be incorrect and one choice should be correct.
            2. generate a valid json object in the format provided which includes the sample question details
            3. verify you created valid json, if it is invalid fix it
            4. respond with the valid json object only
        """

        return prompt_text
