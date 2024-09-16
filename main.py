from flask import Flask, render_template, request, session
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
app.secret_key = '9035473467'

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('input_data')

        if not user_input:
            return render_template('index.html', error_message="Please enter a valid question.")
        
        if 'conversation_context' not in session:
            session['conversation_context'] = ""
        
        if 'responses' not in session:
            session['responses'] = []

        try:    
            result = chain.invoke({
                "context": session['conversation_context'], 
                "question": user_input
            })

            session['conversation_context'] += f"\nUser: {user_input}\nAI: {result}"
            session['responses'].append({"user_input": user_input, "result": result})

        except Exception as e:
            return render_template('index.html', error_message=f"ERROR: {str(e)}")
    responses = session.get('responses', [])
    return render_template('index.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)