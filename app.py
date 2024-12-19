from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="AIzaSyC4unLojdhSHpqQ4Qfh252tkid3oGIKNjI",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query')
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful dental assistant."},
            {"role": "user", "content": query}
        ]
    )
    return jsonify(response.choices[0].message)

if __name__ == '__main__':
    app.run(debug=True)
