import unittest
from question_builder import QuestionBuilder
from openai.types.chat.chat_completion import ChatCompletion
import json

class TestAPIResponse(unittest.TestCase):
    def setUp(self):
        question_builder = QuestionBuilder()
        self.response = question_builder.generate()

    def test_generate(self):
        self.assertIsInstance(self.response, ChatCompletion, "should be a OpenAI object")

    def test_is_valid_json(self):
        json_string = self.response.choices[0].message.content
        self.assertTrue(json.loads(json_string), "should be valid json format")

class TestNonAPIFunctions(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
