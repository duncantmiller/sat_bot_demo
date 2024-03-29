import unittest
from question_builder import QuestionBuilder
from openai.types.chat.chat_completion import ChatCompletion
import json

class TestQuestionBuilder(unittest.TestCase):
    def setUp(self):
        question_builder = QuestionBuilder()
        self.response = question_builder.generate("hard questions")

    def test_generate(self):
        self.assertIsInstance(self.response, ChatCompletion, "should be a OpenAI object")

    def test_is_valid_json(self):
        json_string = self.response.choices[0].message.content
        self.assertTrue(json.loads(json_string), "should be valid json format")

if __name__ == "__main__":
    unittest.main()
