from openai import OpenAI
from dotenv import load_dotenv
import random

load_dotenv()

class QuestionBuilder():
    def __init__(self):
        self.categories = ["math", "reading", "vocabulary"]
        self.math = 0
        self.reading = 0
        self.vocabulary = 0

    def rubric_for(self, category):
        if category == "vocabulary":
            return """
                - Select words that are challenging yet appropriate for high school students preparing for the SAT.
                - Include a mix of word types (nouns, verbs, adjectives, etc.) and themes.
                - ...
            """

    def total_questions_generated(self):
        return self.math + self.reading + self.vocabulary

    def next_category(self):
        if self.total_questions_generated() != 15:
            category = self.pick_category()
            if getattr(self, category) == 5:
                self.next_category()
            else:
                current_count = getattr(self, category)
                setattr(self, category, current_count + 1)
                return category

    def pick_category(self):
        return random.choice(self.categories)

    def generate(self):
        client = OpenAI()
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.prompt()
                }
            ],
            model="gpt-3.5-turbo"
        )
        return response

    def prompt(self):
        category = self.next_category()
        prompt_text = f""""
            You are an expert tutor with excellent knowledge of the Scholastic Aptitude Test (SAT). Your job is to generate sample {category} test questions for a student who is practicing for the {category} section of the SAT. Each question should have four possible answer choices. Only one choice should be correct and the other three choices should be incorrect. Mix up the order of the correct choice in each question so it appears in a different location in the sequence each time. Each response should be in valid json format. Please include the following key value pairs:
            <question_number>:<question number goes here>
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
                "question_number":1,
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
