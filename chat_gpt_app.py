from flask import Flask, render_template, request
from chat_gpt import chat_completion

app= Flask(__name__)
#list to store history of chat bot questions and answers
chatting_history= []

@app.route('/')
def index():
    return render_template('chat_index.html')

@app.route('/get_chat_answer', methods= ['GET', 'POST'])
def chat_answer():
    question = request.form['question']
    answer= chat_completion(question)
    chatting_history.append({"User's Question": question, "ChatBot's Answer": answer})
    return render_template('chat_index.html', que = question, ans= answer, hist= chatting_history)
if __name__ == '__main__': 
   app.run()