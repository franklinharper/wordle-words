#!/usr/bin/env python3
"""Calculate the frequency of each vowel (including Y) in the Wordle word list."""

import json

VOWELS = "aeiouy"
WORD_LIST = "wordle_valid_guesses.json"
OUTPUT_FILE = "vowel_frequency.txt"


def main():
    with open(WORD_LIST) as f:
        words = json.load(f)

    counts: dict[str, int] = {v: 0 for v in VOWELS}
    total_vowels = 0
    total_letters = 0

    for word in words:
        for ch in word.lower():
            total_letters += 1
            if ch in counts:
                counts[ch] += 1
                total_vowels += 1

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"Vowel frequency in {len(words)} Wordle words "
                f"({total_letters} total letters)\n\n")
        f.write(f"{'Vowel':<8}{'Count':>8}{'% of vowels':>14}{'% of letters':>14}\n")
        f.write(f"{'-' * 8}{'-' * 8}{'-' * 14}{'-' * 14}\n")
        for vowel, count in ranked:
            pct_vowels = count / total_vowels * 100
            pct_letters = count / total_letters * 100
            f.write(f"{vowel:<8}{count:>8}{pct_vowels:>13.1f}%{pct_letters:>13.1f}%\n")
        f.write(f"\n{'Total':<8}{total_vowels:>8}{100.0:>13.1f}%"
                f"{total_vowels / total_letters * 100:>13.1f}%\n")

    print(f"Vowel frequency across {len(words)} words:")
    for vowel, count in ranked:
        print(f"  {vowel}: {count}")
    print(f"Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
