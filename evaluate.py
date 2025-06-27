import json
from summarizer import PersianSummarizer
from rouge_score import rouge_scorer
from pathlib import Path
from tqdm import tqdm

def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate(debug=False):
    config = load_config()
    summarizer = PersianSummarizer(model_name=config["model_name"])

    dataset_path = Path(config["dataset_path"])
    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    min_length_floor = config["min_length_floor"]
    min_length_ceil = config["min_length_ceil"]
    max_length_floor = config["max_length_floor"]
    max_length_ceil = config["max_length_ceil"]

    min_r = config["min_ratio"]
    max_r = config["max_ratio"]

    rouge = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

    scores = []
    print("🔍 Evaluating dataset...")
    for idx, item in enumerate(tqdm(dataset, desc="Evaluating")):
        input_text = item["text"]
        reference = item["summary"]

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

        generated = summarizer.summarize(input_text, max_length=int(max_length), min_length=int(min_length))

        if debug and idx < 3:
            print(f"\n--- Sample {idx + 1} ---")
            print(f"Input text: {input_text[:300]}...") 
            print(f"Reference summary: {reference[:300]}...")
            print(f"Generated summary: {generated[:300]}...\n")

        score = rouge.score(reference, generated)
        scores.append(score)

    avg = {
        "rouge1": sum(s["rouge1"].fmeasure for s in scores) / len(scores),
        "rouge2": sum(s["rouge2"].fmeasure for s in scores) / len(scores),
        "rougeL": sum(s["rougeL"].fmeasure for s in scores) / len(scores)
    }

    print("📊 Average ROUGE scores:")
    for k, v in avg.items():
        print(f"{k}: {v:.4f}")

if __name__ == "__main__":
    evaluate(debug=True)
