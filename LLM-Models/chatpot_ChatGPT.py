"""
Author: Batool Alkaddah 
Time & Date: 11:13 p.m. 2024-02-02
PyCharm
"""
import openai
import os

# Define OpenAI API key
openai.api_key = "#############"

def test_chat_gpt(msg: str) -> str:
  response= openai.Completion.create(
    engine= 'gpt-3.5-turbo-instruct',
    prompt= msg,
    max_tokens=150

  )
  return response.choice[0].text

#Start a conversation
conversation= []

while True:
  user_input= input("You: ")
  conversation.append(f'You: {user_input}')

  # Exit the loop if 'exit'
  if user_input.lower() == 'exit':
    break

  # Generate a response form chatGPT
  response= test_chat_gpt("\n".join(conversation))
  print(f"ChatGPT: {response}")
  conversation.append(f"ChatGPT: {response}")


def mini_chatGPT(first_prompt: str):
  prompt= first_prompt


  while True:

    user_input= input("User: ")

    response= openai.Completion.create(
        model= 'gpt-3.5-turbo-instruct',
        prompt= prompt + "\nUser: " + user_input +"\n",
        temprature= 0.7,
        max_tokens=150
    )

    chatbot_response= response.choice[0].text
    print("Chatpot: ", chatbot_response)

    prompt=f'{prompt}\nChatpot:  {chatbot_response}\n'