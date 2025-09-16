# ⚙️ Installation Guide

This guide explains how to set up and run the **Tshiluba Text Corpus** project.

---

## 1. Clone the Repository

bash
git clone https://github.com/<your-username>/CILUBA-TEXT-DATASET.git
cd CILUBA-TEXT-DATASET

---

## 2. Create a Virtual Environment (Recommended)

It’s best to keep project dependencies isolated.

# Create virtual environment
python3 -m venv venv

# Activate it
# On Linux/Mac
source venv/bin/activate
# On Windows (PowerShell)
venv\Scripts\Activate

---

## 3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

---

## 4. Generate the Dataset

Open the Jupyter notebook and run the pipeline:

jupyter notebook main.ipynb


This will:

- Collect raw Tshiluba text

- Clean and normalize it

- Split into train.jsonl, val.jsonl, test.jsonl

---

## 5. Train the Tokenizer (Optional)

To train a SentencePiece tokenizer:

python train_tokenizer.py


This will generate:

- tshiluba_spm.model

- tshiluba_spm.vocab