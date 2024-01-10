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
                    "content": "foo"
                }
            ],
            model="gpt-3.5-turbo"
        )
        return response
