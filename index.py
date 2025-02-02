from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load marks from JSON file
json_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(json_path, "r") as file:
    marks_data = json.load(file)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get multiple name parameters
    result = [marks_data.get(name, "Not Found") for name in names]
    return jsonify(result)

# Vercel requires this handler
def handler(event, context):
    return app(event, context)
