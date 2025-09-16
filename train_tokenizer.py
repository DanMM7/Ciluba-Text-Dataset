import json
import sentencepiece as spm

# Paths
INPUT_FILE = "tshiluba_corpus.txt"
MODEL_PREFIX = "tshiluba_spm"
VOCAB_SIZE = 8000  # adjust based on corpus size

# Step 1: Extract sentences from train.jsonl
with open("train.jsonl", "r", encoding="utf-8") as f:
    train_lines = [json.loads(line)["text"] for line in f]

with open(INPUT_FILE, "w", encoding="utf-8") as f:
    for line in train_lines:
        f.write(line + "\n")

print(f"Saved {len(train_lines)} sentences to {INPUT_FILE}")

# Step 2: Train SentencePiece model
spm.SentencePieceTrainer.Train(
    f"--input={INPUT_FILE} "
    f"--model_prefix={MODEL_PREFIX} "
    f"--vocab_size={VOCAB_SIZE} "
    f"--character_coverage=1.0 "  # keeps all Tshiluba characters
    f"--model_type=bpe"           # 'bpe' recommended; can try 'unigram'
)

print("✅ Tokenizer training complete!")

# Step 3: Load and test tokenizer
sp = spm.SentencePieceProcessor()
sp.load(f"{MODEL_PREFIX}.model")

sample_text = "Muana udi kuenda."
encoded = sp.encode(sample_text, out_type=int)
decoded = sp.decode(encoded)

print("Sample text:", sample_text)
print("Encoded IDs:", encoded)
print("Decoded back:", decoded)
