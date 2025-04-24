'''
Clean the paragraph by converting to lowercase and removing punctuation
Remove common stop words (like 'the', 'is', 'at', etc.)
Count how often each word appears
Filter and return the top-3 words that start with a given prefix, sorted by frequency
'''

import re
stop_words = ['the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'for', 'with', 'as', 'by', 'from']

def clean_text(text):
    # Make everything lowercase and remove punctuation
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return [word for word in words if word not in stop_words]

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def top_prefix(word_count, prefix, k):
    # Filter words by prefix and sort by frequency
    filtered = [(word, freq) for word, freq in word_count.items() if word.startswith(prefix)]
    filtered.sort(key=lambda x: -x[1])  # Sort by frequency descending
    return filtered[:k]

# Example paragraph
paragraph = """
The theory of relativity is one of the pillars of modern physics. It was proposed by Albert Einstein and transformed our understanding of space, time, and gravity. 
Theoretical physicists often work on abstract problems in quantum mechanics and thermodynamics.
"""

words = clean_text(paragraph)
word_count = count_words(words)

result = top_prefix(word_count, 'th', 3)
print(result)
