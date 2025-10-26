import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    print("Error: GEMINI_API_KEY not found.")
    exit()

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

print("The Simple Gemini Chatbot is ready, using 2.5 flash version. Type in 'quit' to exit the chatbot.")
print("Hi, I am Gemini. How can I help you today?")
print("="*50)

while True:
    user_input = input("Your Input : ")

    if not user_input.strip():
        print("Please enter a valid message.")
        continue

    if user_input.lower() == "quit":
        print("\nGoodbye.")
        break

    try:
        response = chat.send_message(user_input, stream=True)
        print("Gemini : ",end="")

        for each in response:
            print(each.text, end="")
        print("\n")

    except Exception as e:
        print(f"Gemini has an error occur while getting a response : {e}")
        print("\n")