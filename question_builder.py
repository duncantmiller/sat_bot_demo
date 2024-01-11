from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class QuestionBuilder():
    def generate(self, theme_string):
        client = OpenAI()
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.prompt(theme_string)
                }
            ],
            model="gpt-3.5-turbo"
        )
        return response

    def prompt(self, theme_string):
        prompt_text = (
            "You are an expert tutor with excellent knowledge of the Scholastic Aptitude Test "
            " SAT). Your job is to generate sample test questions for a student who is practicing "
            f"for the SAT. The theme for these questions is: {theme_string}, please use this theme "
            "when generating questions. There are three categories of questions to generate. "
            "Your task will be to generate five sample questions for each category, for a "
            "total of fifteen questions. Each question should have four possible answer "
            "choices. Only one choice should be correct and the other three choices should "
            "be incorrect. Mix up the order of the correct choice in each question so it "
            "appears in a different location in the sequence each time. The question "
            "categories are math, reading and vocabulary. Please generate the sample "
            "questions one at a time and respond with each individual sample question and "
            "its answer choices. Each response should be in valid json format. Please "
            "include the following key value pairs:\n"
            "<question_number>:<question number goes here>\n"
            "<category_name>:<category name must be either math, reading or vocabulary>\n"
            "<question_text>:<question text goes here>\n"
            "<answer_choices>:<answer choices go here>\n"
            "<correct_choice>:<the key of the correct choice goes here>\n\n"
            "The format of the answer choices should be:\n"
            "    <choice_1>:<choice one text goes here>\n"
            "    <choice_2>:<choice two text goes here>\n"
            "    <choice_3>:<choice three text goes here>\n"
            "    <choice_4>:<choice four text goes here>\n\n"
            "Here is an example of valid json to you might respond with for a sample "
            "question in the math category:\n\n"
            "{\n"
            "    \"question_number\":1,\n"
            "    \"category_name\":\"math\",\n"
            "    \"question_text\":\"What is 1 + 1 equal to?\",\n"
            "    \"answer_choices\": {\n"
            "        \"choice_1\": \"1\",\n"
            "        \"choice_2\": \"7\",\n"
            "        \"choice_3\": \"2\",\n"
            "        \"choice_4\": \"0\"\n"
            "    },\n"
            "    \"correct_choice\":\"choice_4\"\n"
            "}\n\n"
            "Don't actually use this example question, generate your own but use this format.\n\n"
            "Please double check the json format to ensure it is valid json before responding "
            "with the sample question. If it is invalid, fix it before responding. Keep track "
            "of three variables math_questions, reading_questions, and vocabulary_questions. "
            "Each variable should initially be set to 0. After each response, increment the "
            "corresponding variable. For example, after responding with your first math "
            "question the variables should be:\n"
            "math_questions = 1\n"
            "reading_questions = 0\n"
            "writing_questions = 0\n"
            "Then after responding with a writing question they should be:\n"
            "math_questions = 1\n"
            "reading_questions = 0\n"
            "writing_questions = 1\n"
            "Keep going until you have a value of 5 questions in each category for a total of "
            "15 sample questions.\n\n"
            "When you are generating sample vocabulary questions, please follow this rubric:\n\n"
            "- Select words that are challenging yet appropriate for high school students "
            "preparing for the SAT.\n"
            "- Include a mix of word types (nouns, verbs, adjectives, etc.) and themes.\n\n"
            "Let's think step by step:\n"
            "1. first pick a category randomly from either math, reading or vocabulary\n"
            "2. then use your expert SAT knowledge to generate a sample question for that "
            "category with 4 potential answer choices. The question should follow the theme: "
            f"{theme_string}. Three choices should be incorrect and one choice should be correct.\n"
            "3. generate a valid json object in the format provided which includes the sample "
            "question details\n"
            "4. verify you created valid json, if it is invalid fix it\n"
            "5. respond with the valid json object only\n"
            "6. increment the math_questions, reading_questions, and vocabulary_questions "
            "based on which category you generated a sample question for. Just keep track of "
            "this internally, do not include these variables in your response.\n"
            "7. repeat step 1 until you have generated 5 sample questions for each category"
        )

        return prompt_text
