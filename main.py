from collections import Counter

def word_frequency_counter():
    text = input("Enter a paragraph:\n")

    words = text.lower().split()

    words = [word.strip(".,!?;:()[]{}\"'") for word in words]

    freq = Counter(words)

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    print("\nTop 3 most frequent words:")
    for word, count in sorted_words[:3]:
        print(f"{word}: {count}")

word_frequency_counter()
