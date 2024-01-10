import unittest
from question_builder import QuestionBuilder
from openai.types.chat.chat_completion import ChatCompletion

class TestQuestionBuilder(unittest.TestCase):

    def test_generate(self):
        question_builder = QuestionBuilder()
        response = question_builder.generate()
        self.assertIsInstance(response, ChatCompletion)

if __name__ == "__main__":
    unittest.main()
