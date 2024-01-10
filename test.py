import unittest
from question_builder import QuestionBuilder

class TestQuestionBuilder(unittest.TestCase):

    def test_generate(self):
        question_builder = QuestionBuilder()
        self.assertTrue(question_builder.generate())

if __name__ == "__main__":
    unittest.main()
