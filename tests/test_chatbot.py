import unittest
from src.chatbot import GenAIChatbot

class TestGenAIChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = GenAIChatbot()
        # open context.txt file and read the content
        with open('context.txt', 'r', encoding='utf-8') as f:
            self.context = f.read()

    def test_get_answer1(self):
        question = "What is GitLab?"
        response = self.chatbot.get_answer(question, self.context)
        print("Response1:", response)
        self.assertIn("complete DevOps platform", response.get('answer', ""))

    def test_empty_question(self):
        question = ""
        response = self.chatbot.get_answer(question, self.context)
        print("Response2:", response.get('answer', ""))
        self.assertEqual(response.get('answer', ""), "")

    def test_followUp_question(self):
        question = "What is GitLab in layman's terms?"
        response = self.chatbot.get_answer(question, self.context)
        print("Response4:", response.get('answer', ""))
        followUp_question = "What is a DevOps platform?"
        response = self.chatbot.get_answer(followUp_question, self.context)
        print("Response5:", response.get('answer', ""))
        self.assertIn("DevOps platform", response.get('answer', ""))

if __name__ == '__main__':
    unittest.main()