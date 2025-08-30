import os
import google.generativeai as genai
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])
print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
user_input = input("You: ")
response = chat.send_message(user_input)
print("Gemini:", response.text, "\n")
