"""Write the entry: one excuse an AI agent gives for a missed deadline.

Deterministic: the text is a fixed literal. No network, no randomness,
no input read; the output directory is created when missing and never deleted.
"""

import os

ENTRY = "I was on schedule until my context window compacted the deadline into a single token, and that token turned out to be 'later'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
