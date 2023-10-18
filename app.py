from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set up OpenAI API Key
openai.api_key = "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"
openai.Model.list()

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    print(request.form)

    question = request.form.get('question')
    
    # Only proceed if the question is tax-related (simplified filtering for this example)
    if "tax" not in question.lower():
        return jsonify({"error": "Please ask only tax-related questions."})
    
    # Send the question to OpenAI's GPT model
    try:
        response = openai.Completion.create(
        model="text-davinci-002", 
        prompt=question, 
        max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    except openai.error.OpenAIError as e:
        # This will catch any OpenAI-specific errors
        return jsonify({"error": str(e)})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
