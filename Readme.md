# 🧠 Persian Text Summarizer

A Persian text summarization app and evaluation framework using summarization models from Hugging Face.

## 🔧 Features

- Web interface for interactive summarization (Flask-based)
- REST API endpoint (`/api/summarize`) for programmatic access
- Configurable length controls via `config.json`
- Built-in evaluation using ROUGE metrics
- Supports batch evaluation with progress bar

## 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/persian-summarizer.git
    cd persian-summarizer
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### 🌐 Web App
Run the web application:

```bash
python app.py
````

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🧪 Evaluation

Evaluate your summarizer on the dataset:

```bash
python evaluate.py
```

The evaluation script uses `ROUGE` scores and shows results like:

```
📊 Average ROUGE scores:
rouge1: 0.4123
rouge2: 0.2157
rougeL: 0.3978
```

### 📡 API

You can send a POST request to `/api/summarize`:

```bash
curl -X POST http://127.0.0.1:5000/api/summarize \
    -H "Content-Type: application/json" \
    -d '{"text": "متنی برای خلاصه‌سازی"}'
```

## 🛠 Config

Edit `config.json` to control:

* Model name
* Length ratios & hard caps
* Server host/port
* Evaluation dataset path

Example:

```json
{
  "model_name": "m3hrdadfi/bert2bert-fa-wiki-summary",
  "min_length_floor": 50,
  "min_length_ceil": 200,
  "max_length_floor": 200,
  "max_length_ceil": 300,
  "max_ratio": 0.5,
  "min_ratio": 0.25,
  "host": "127.0.0.1",
  "port": 5000,
  "debug": true,
  "dataset_path": "dataset/samples.json"
}
```

