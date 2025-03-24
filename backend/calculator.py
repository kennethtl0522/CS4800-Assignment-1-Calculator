from flask import Flask, jsonify, request, send_from_directory
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
        data = "hello world"
        return jsonify({'data': data}) 
    
if __name__ == '__main__':
    app.run(debug=True)



# client = OpenAI()
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)


