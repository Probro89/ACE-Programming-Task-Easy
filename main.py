from collections import Counter

def word_frequency_counter():
    # Take paragraph input from user
    text = input("Enter a paragraph:\n")

    # Convert to lowercase and split into words
    words = text.lower().split()

    # Remove punctuation from each word
    words = [word.strip(".,!?;:()[]{}\"'") for word in words]

    # Count frequencies using Counter (like HashMap)
    freq = Counter(words)

    # Sort by frequency (descending), then alphabetically
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Print top 3 words
    print("\nTop 3 most frequent words:")
    for word, count in sorted_words[:3]:
        print(f"{word}: {count}")

# Run program
word_frequency_counter()
