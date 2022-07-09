# Building a mood chatbot
# Import module to choose randomly from bot rsponses.
from random import choice


# List of bot responses based on user response
happy = ["Glad to hear that", "That's awesome", "👌", "Yah, that's great"]
sad = ["Sorry about that", "Don't worry, it will be fine",
       "Cheer up", "play some music"]
hungry = ["I get hungery too", "fix some pancakes",
          "why don't you order pizza"]

# Define a function named get_bot_response that takes the parameter user_response
# and returns a string with the chat bot response.


def get_bot_response(user_response):
    if user_response == "happy":
        return choice(happy)
    elif user_response == "sad":
        return choice(sad)
    elif user_response == "hungry":
        return choice(hungry)
    else:
        return f"I don't understand that. Are you happy, or sad or hungry"


name = input("What's your name: ")
print(f"{name} welcome to ChatBotty 😊")
print(f"{name} tell me how are you feeling today\n")

while True:
    user_response = input("Are you happy or sad or hungry: ").lower()
    if user_response == "quit":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response.upper())
    print("\nTo exit at any time, type quit\n")
