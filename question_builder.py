from openai import OpenAI
from dotenv import load_dotenv
import random

load_dotenv()

class QuestionBuilder():
    def pick_category(self):
        categories = ["math", "reading", "vocabulary"]
        return random.choice(categories)

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
        prompt_text = """"
            You are an expert tutor with excellent knowledge of the Scholastic Aptitude Test (SAT). Your job is to generate sample test questions for a student who is practicing for the SAT. There are three categories of questions to generate. Your task will be to generate five sample questions for each category, for a total of fifteen questions. Each question should have four possible answer choices. Only one choice should be correct and the other three choices should be incorrect. Mix up the order of the correct choice in each question so it appears in a different location in the sequence each time. The question categories are math, reading and vocabulary. Please generate the sample questions one at a time and respond with each individual sample question and its answer choices. Each response should be in valid json format. Please include the following key value pairs:
            <question_number>:<question number goes here>
            <category_name>:<category name must be either math, reading or vocabulary>
            <question_text>:<question text goes here>
            <answer_choices>:<answer choices go here>
            <correct_choice>:<the key of the correct choice goes here>

            The format of the answer choices should be:
                <choice_1>:<choice one text goes here>
                <choice_2>:<choice two text goes here>
                <choice_3>:<choice three text goes here>
                <choice_4>:<choice four text goes here>

            Here is an example of valid json to you might respond with for a sample question in the math category:

            {
                "question_number":1,
                "category_name":"math",
                "question_text":"What is 1 + 1 equal to?",
                "answer_choices": {
                    "choice_1": "1",
                    "choice_2": "7",
                    "choice_3": "2",
                    "choice_4": "0"
                },
                "correct_choice":"choice_4"
            }

            Don't actually use this sample question, generate your own but use this format.

            Please double check the json format to ensure it is valid json before responding with the sample question. If it is invalid, fix it before responding. Keep track of three variables math_questions, reading_questions, and vocabulary_questions. Each variable should initially be set to 0. After each response, increment the corresponding variable. For example, after responding with your first math question the variables should be:
            math_questions = 1
            reading_questions = 0
            writing_questions = 0
            Then after responding with a writing question they should be:
            math_questions = 1
            reading_questions = 0
            writing_questions = 1
            Keep going until you have a value of 5 questions in each category for a total of 15 sample questions.

            When you are generating sample vocabulary questions, please follow this rubric:

            - Select words that are challenging yet appropriate for high school students preparing for the SAT.
            - Include a mix of word types (nouns, verbs, adjectives, etc.) and themes.
            - ...

            Let's think step by step:
            1. first pick a category randomly from either math, reading or vocabulary
            2. then use your expert SAT knowledge to generate a sample question for that category with 4 potential answer choices. Three choices should be incorrect and one choice should be correct.
            3. generate a valid json object in the format provided which includes the sample question details
            4. verify you created valid json, if it is invalid fix it
            5. respond with the valid json object only
            6. increment the math_questions, reading_questions, and vocabulary_questions based on which category you generated a sample question for. Just keep track of this internally, do not include these variables in your response.
            7. repeat step 1 until you have generated 5 sample questions for each category
        """

        return prompt_text
