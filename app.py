import json
from flask import Flask, request, jsonify, render_template
from summarizer import PersianSummarizer

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

app = Flask(__name__)
summarizer = PersianSummarizer(model_name=config["model_name"])

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text", "").strip()
        if input_text:
            max_len = int(len(input_text) * config["max_ratio"])
            min_len = int(max(len(input_text) * config["min_ratio"], config["min_length_floor"]))
            summary = summarizer.summarize(input_text, max_length=max_len, min_length=min_len)

    return render_template("index.html", summary=summary, input_text=input_text)

@app.route("/api/summarize", methods=["POST"])
def api_summarize():
    data = request.get_json()
    input_text = data.get("text", "").strip()

    if not input_text:
        return jsonify({"error": "No input text provided."}), 400

    min_length_floor = config["min_length_floor"]
    min_length_ceil = config["min_length_ceil"]
    max_length_floor = config["max_length_floor"]
    max_length_ceil = config["max_length_ceil"]

    min_r = config["min_ratio"]
    max_r = config["max_ratio"]

    min_length = len(input_text) * max_r
    max_length = len(input_text) * min_r

    if min_length > min_length_ceil:
        min_length = min_length_ceil
    elif min_length < min_length_floor:
        min_length = min_length_floor

    if max_length > max_length_ceil:
        max_length = max_length_ceil
    elif max_length < max_length_floor:
        max_length = max_length_floor

    summary = summarizer.summarize(input_text, max_length=int(max_length), min_length=int(min_length))

    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(host=config["host"], port=config["port"], debug=config["debug"])
