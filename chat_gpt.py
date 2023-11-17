import os
import openai

#setting openai key
openai.api_key = '-------------------------------------'

#model we will be using ---> 'gpt-3.5-turbo'
#to control randomness of answer of the chatgpt--->temperature= 0

def chat_completion(prompt, model= 'gpt-3.5-turbo', temperature= 0):
    #message that will be passed to chatgpt
    message= [{"role": "user", "content": prompt}]

    #response of the model after we pass the input
    response= openai.ChatCompletion.create(
        #model we will be using (gpt-3.5-turbo)
        model= model,
        #users prompt/message
        messages = message,
        #to control randomness-- 0 means there will be complete random answers
        temperature= temperature
    )

    #now just return the response
    return response.choices[0].message["content"]

