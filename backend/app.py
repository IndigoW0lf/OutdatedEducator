from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

app = Flask(__name__)
CORS(app)

@app.route('/getFacts', methods=['POST'])
def get_facts():
    data = request.json
    year = data['year']
    country = data['country']

    prompt = f"""
Provide 5 major facts or concepts that were likely taught to high school senior students in {country} in the year {year} that have since been challenged, revised, or disproven. For each fact, briefly describe the revision or refutation and mention the year it was revisited.
"""

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )

    facts = response['choices'][0]['message']['content'].strip()

    return jsonify({"facts": facts})

if __name__ == "__main__":
    app.run(debug=True)
