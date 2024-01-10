from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class QuestionBuilder():
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
        return "foo"
