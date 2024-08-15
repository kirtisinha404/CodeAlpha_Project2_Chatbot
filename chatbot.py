import nltk   #natural language toolkit
from nltk.chat.util import Chat, reflections
import random

joins = [
    [
        r"Hi|Hey|Hello",
        ["Hello, how may I help you?","Hey there, how may I help you today?",]
    ],
    [
        r"My name is(.*)",
        ["Hello %1,how are you today?", ]
    ],
    
    [
        r"How are you ?",
        ["I'm doing well, thank you!\nHow about you?", ]
    ],
    [
        r"sorry(.*)",
        ["It's alright", "No Problem", ]
    ],
    [
        r"good|fine|great",
        ["That's so great to hear<3",]
    ],
    [
        r"Bye",
        ["Goodbye! Take care and have a Nice day.",]
    ],
]

def chatbot():
    print("Hi, I'm a chatbot! Type 'Bye' to exit. ")
    chat = Chat(joins, reflections)
    chat.converse()
    
chatbot()