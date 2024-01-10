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
    def setUp(self):
        self.question_builder = QuestionBuilder()

    def test_pick_category(self):
        category = self.question_builder.pick_category()
        self.assertIn(category, self.question_builder.categories, "should be one of the categories")

    def test_next_category(self):
        for _ in range(16):
            self.question_builder.next_category()

        self.assertEqual(self.question_builder.math, 5, "should be 5")
        self.assertEqual(self.question_builder.reading, 5, "should be 5")
        self.assertEqual(self.question_builder.vocabulary, 5, "should be 5")

class TestGenerateAll(unittest.TestCase):
    def test_generate_all_questions(self):
        question_builder = QuestionBuilder()
        question_builder.generate_all_questions()

        self.assertEqual(question_builder.math, 5, "should be 5")
        self.assertEqual(question_builder.reading, 5, "should be 5")
        self.assertEqual(question_builder.vocabulary, 5, "should be 5")

if __name__ == "__main__":
    unittest.main()
