# Persian Text Summarizer

**A Persian abstractive-summarization service with a Flask web interface, REST API, configurable generation controls, and ROUGE evaluation.**

The project serves Hugging Face sequence-to-sequence summarization models through both a browser interface and a programmatic API. It also includes a batch-evaluation workflow for measuring summary quality against reference texts.

## Engineering highlights

- Persian abstractive summarization with transformer models
- Flask-based web application
- JSON REST API for programmatic inference
- Configurable model and length controls
- Batch evaluation with progress reporting
- ROUGE-1, ROUGE-2, and ROUGE-L metrics
- Separation between application, configuration, model inference, and evaluation workflows

## Technology

`Python` · `Flask` · `Hugging Face Transformers` · `PyTorch` · `Persian NLP` · `ROUGE`

## Architecture

```text
Web UI or API client
        │
        ▼
Flask application
        │
        ▼
Input validation and length controls
        │
        ▼
Hugging Face summarization model
        │
        ▼
Generated Persian summary

Evaluation dataset
        │
        ▼
Batch inference ──► ROUGE metrics
```

## Features

- interactive summarization from the web interface
- `POST /api/summarize` endpoint
- model selection through `config.json`
- proportional and absolute minimum/maximum summary lengths
- configurable server host, port, and debug mode
- dataset-driven evaluation
- aggregate ROUGE reporting

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open the application at:

```text
http://127.0.0.1:5000
```

## API example

```bash
curl -X POST http://127.0.0.1:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"text":"متنی برای خلاصه‌سازی"}'
```

## Evaluation

Run batch evaluation against the configured dataset:

```bash
python evaluate.py
```

The evaluator reports aggregate scores such as:

```text
ROUGE-1
ROUGE-2
ROUGE-L
```

These metrics compare generated summaries with reference summaries. They are useful for controlled experiments but should be interpreted together with qualitative review, especially for Persian fluency and factual consistency.

## Configuration

`config.json` controls the model and runtime behavior:

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

Length ratios allow generation bounds to adapt to the input while the hard floors and ceilings prevent extreme output sizes.

## Model and evaluation notes

- Model quality depends on the selected checkpoint and its training data.
- Long documents may require chunking or a model with a larger context window.
- ROUGE primarily measures lexical overlap and does not fully capture factuality or writing quality.
- The default configuration is appropriate for local experimentation, not unattended public deployment.
- Production deployment should add authentication, request limits, structured logging, timeouts, and model-resource monitoring.

## Project status

This repository is a focused NLP application demonstrating model serving, API design, configurable inference, Persian-language processing, and quantitative evaluation.