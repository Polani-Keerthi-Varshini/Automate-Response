from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'API_KEY'

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for automated response generation
@app.route('/generate_response', methods=['POST'])
def generate_response():
    query = request.form.get('query')

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        # Generate a response using GPT-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": query},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = response.choices[0].message['content'].strip()
        return jsonify({'response': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
