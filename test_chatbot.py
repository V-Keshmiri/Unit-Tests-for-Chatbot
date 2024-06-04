"""
Author: Vahid Keshmiri
Email: V.Keshmiry@Gmail.com

This module includes unit tests for the Chatbot class implemented using a finite state machine (FSM). 
The tests cover the state transitions and responses of the chatbot.
"""

import unittest
from fsm_chatbot import Chatbot, State

class TestChatbot(unittest.TestCase):
    """
    Unit tests for the Chatbot class.
    """

    def setUp(self):
        """
        Set up the chatbot instance for testing.
        """
        self.chatbot = Chatbot()

    def test_start_state(self):
        """
        Test the chatbot's response and state transition from the START state.
        """
        response = self.chatbot.handle_message("")
        self.assertEqual(response, "Hi! What's your name?")
        self.assertEqual(self.chatbot.state, State.ASK_NAME)

    def test_ask_name_state(self):
        """
        Test the chatbot's response and state transition from the ASK_NAME state.
        """
        self.chatbot.state = State.ASK_NAME
        response = self.chatbot.handle_message("Alice")
        self.assertEqual(response, "Nice to meet you, Alice. How old are you?")
        self.assertEqual(self.chatbot.state, State.ASK_AGE)

    def test_ask_age_state(self):
        """
        Test the chatbot's response and state transition from the ASK_AGE state.
        """
        self.chatbot.state = State.ASK_AGE
        self.chatbot.user_name = "Alice"
        response = self.chatbot.handle_message("25")
        self.assertEqual(response, "25 is a great age to be! It was nice chatting with you!")
        self.assertEqual(self.chatbot.state, State.END)

if __name__ == "__main__":
    unittest.main()
