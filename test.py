import unittest
from question_builder import QuestionBuilder
from openai.types.chat.chat_completion import ChatCompletion

class TestQuestionBuilder(unittest.TestCase):
    def setUp(self):
        question_builder = QuestionBuilder()
        self.response = question_builder.generate()

    def test_generate(self):
        self.assertIsInstance(self.response, ChatCompletion)

if __name__ == "__main__":
    unittest.main()
