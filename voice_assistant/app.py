from flask import Flask, render_template , request , jsonify
from Jarvis import *
import asyncio

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_voice_input', methods=['POST'])
def process_voice_input():
    # Call the Main function to listen, process, and respond
    main_reply, additional_messages = asyncio.run(Main())
    
    print("main reply:", main_reply)
    print("additional message:", additional_messages)
    return jsonify({'main_reply': main_reply, 'additional_messages': additional_messages})

if __name__ == '__main__':
    app.run(debug=True)





