import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses for the chatbot
patterns = [
    (r'(.*)hello(.*)', ('Hello!', 'Hi there!', 'How can I help you today?')),
    (r'(.*)help(.*)', ('I can assist with basic health-related questions.', 'What do you need help with?')),
    (r'(.*)symptoms(.*)', ('Please describe your symptoms.', 'What are your symptoms?')),
    (r'(.*)headache(.*)', ('Headaches can have various causes. It could be tension, dehydration, or something else. Please provide more details.',)),
    (r'(.*)fever(.*)', ('Fever is often a sign of infection. Are you experiencing any other symptoms?',)),
    (r'(.*)thank you(.*)',('You are welcome!,You can always ask if you have more questions')),
    (r'(.*)quit(.*)', ('Goodbye!', 'Take care!')),
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Define a function to start and interact with the chatbot
def doctor_assistant():
    print("AI Doctor Assistant: Hello! How can I assist you today?")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    doctor_assistant()
