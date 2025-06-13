import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask, request, jsonify
from langchain_core.messages import AIMessage, HumanMessage
from src.helpers.qa_chain import qa_chain

app = Flask(__name__)
CORS(app)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

qa_chain = qa_chain()

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No se proporcionó una pregunta"}), 400
    response = qa_chain.invoke({
        "question": question
    })
    
    return jsonify({"response": response})