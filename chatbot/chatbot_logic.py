import nltk
from nltk.chat.util import Chat, reflections

# Define predefined question-answer pairs

pairs = [
    ["hi|hello|hey",["Hello! How can I you with banking"]],
    ["what is my account balance",["I'm unable to access your account, but you can check it through net banking or our mobile app."]],
    ["how to apply for a loan", ["You can apply for a loan through our website or visit the nearest branch."]],
    ["what are your working hours", ["Our bank is open from 9 AM to 5 PM, Monday to Friday."]],
    ["bye|goodbye", ["Goodbye! Have a great day."]]

]

# Create the chatbot instance

chatbot = Chat(pairs,reflections)

def get_response(user_input):
    response =  chatbot.respond(user_input)
    if response:
        return response
    else:
        return " I'm sorry, I don't understand that. Please ask about banking services."


  