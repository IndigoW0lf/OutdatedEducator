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

    prompt = f"Provide 5 facts and concepts that might have been taught in 12th grade in {country} in the year {year} that have since been challenged, revised, or disproven. Ensure this was still being taught to high school seniors in {year}."

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=750
    )

    facts = response.choices[0].text.strip()

    return jsonify({"facts": facts})

if __name__ == "__main__":
    app.run(debug=True)
