# 📚 Tshiluba Text Corpus (Monolingual)

## Overview
This project provides a **monolingual text corpus** for **Tshiluba (Ciluba)**, a Bantu language spoken by over **7 million people** in the Democratic Republic of Congo (DRC). Tshiluba is a **low-resource language**, with very limited publicly available datasets for Natural Language Processing (NLP).  

This corpus was compiled from **publicly available text sources** to support **language modeling, text classification, and other NLP tasks**. It represents the first stage of a broader effort to build **both monolingual and parallel (Tshiluba ↔ English) corpora**.  

---

## ✨ Features
- **Language**: Tshiluba (Ciluba)  
- **Data type**: Monolingual sentences  
- **Format**: JSONL (`id`, `text`)  
- **Sources**:  
  - Public domain Bible texts (1996, 2003 editions)  
  - Tshiluba song lyrics  
  - Other public domain texts  

---

## 📂 Dataset Structure
The dataset is split into training, validation, and test sets:  
train.jsonl # ~70% of data
val.jsonl # ~15% of data
test.jsonl # ~15% of data


Each line is a JSON object:  

```json```
{"id": "train_001", "text": "Muana udi kuenda."}
{"id": "train_002", "text": "Bantu badi mu mukanda."}

## 📊 Current Statistics (example)

(to be updated after running the pipeline)

- Total sentences: 10733 sentences  
- Training set: 7513 sentences  
- Validation set: 1610 sentences  
- Test set: 1610 sentences  
- Vocabulary size: *(to be calculated)*  
- Avg. sentence length: *(to be calculated)*  

---

## 🛠️ Usage

This dataset can be used for:

- Pretraining language models (e.g., HuggingFace Transformers)

- Tokenizer training (e.g., SentencePiece, BPE)

- Downstream NLP tasks (classification, clustering, keyword search)

- Linguistic research and digital preservation

Example in Python:

import json

with open("train.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)
        print(entry["id"], entry["text"])

---      

## 🚧 Limitations

- Orthographic variation: Tshiluba uses diacritics inconsistently across sources.

- Domain bias: Most data currently comes from religious texts and song lyrics.

- Work in progress: Parallel Tshiluba ↔ English dataset will be added in the next stage.

---

## 🔮 Future Work

- Expand monolingual corpus with more diverse sources.

- Build a parallel Tshiluba ↔ English dataset (Bible, Morrison’s dictionary).

- Release pretrained Tshiluba word embeddings and language models.


---
