from flask import Flask, request, render_template
from chatbot.chatbot_logic import get_response

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
@app.route("/chat", methods=['POST'])

def chat():
    user_message = request.form["message"]
    response = get_response(user_message)
    return response

if __name__ =="__main__":
    app.run(debug=True)


