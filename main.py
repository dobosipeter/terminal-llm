import os
import rich
from rich.markdown import Markdown

import google.generativeai as genai

# TODO: What is a secure way of storing/accessing the API Key?
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is None:
  raise ValueError("Google API Key not found. Make sure to set your API key in the GOOGLE_API_KEY environment variable!")
# Set the api key
genai.configure(api_key=google_api_key)

# Check that the model we want to use is available
available_models = [model.name for model in genai.list_models()]
if "models/gemini-pro" not in available_models:
  raise KeyError("Gemini Pro not present in the list of available models. Make sure that you have access to the model.")

# set the model
model = genai.GenerativeModel('gemini-pro')
# Create a new chat
chat = model.start_chat(history=[])
print("Starting chat session with the model.\nType 'quit' to quit.")
while True:
  user_input = input("\nPlease input your query to the model:\n")
  if user_input == "quit":
    break
  # Query the model
  model_response = chat.send_message(user_input)
  # Handle markdown output
  rich.print(Markdown(model_response.text))

