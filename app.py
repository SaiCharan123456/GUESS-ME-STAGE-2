from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 5,
        "category": "Sports",
        "word": "Chess"
    },
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },
    {
        "inputs": 5,
        "category": "Very popular Asian country",
        "word": "India"  
    },
    {
        "inputs": 6,
        "category": "What is always in front of you but can't be seen?",
        "word": "Future"
    },
    {
        "inputs": 5,
        "category": "Get Google's AI to compose your emails here",
        "word": "Gmail"  
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
})

if __name__ == "__main__":
    app.run()