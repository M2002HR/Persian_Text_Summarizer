from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class PersianSummarizer:
    def __init__(self, model_name):
        print("Loading tokenizer and model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def summarize(self, text, max_length=150, min_length=30):
        input_text = f"summarize: {text}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(
            inputs,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
