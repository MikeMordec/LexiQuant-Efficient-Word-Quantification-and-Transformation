LexiQuant is a Python toolkit designed to streamline text analytics by providing efficient word quantification and transformation utilities. This toolkit enables seamless conversion between words and numeric representations, facilitating various text processing tasks.
Features

    Word Quantification: Convert words into numeric representations for efficient text processing.
    Transformation: Convert numeric representations back into words, maintaining data integrity.
    Efficiency: Optimized algorithms ensure fast and reliable performance, even with large datasets.
    Flexibility: Easily integrate LexiQuant into your existing text analytics workflows or utilize it as a standalone tool.
    User-Friendly: Simple and intuitive interface makes it easy to use for both beginners and advanced users.

Installation

To use LexiQuant, simply clone this repository to your local machine:

bash

git clone https://github.com/your-username/lexi-quant.git

Usage

    Word to Number Conversion:

    python

from lexiquant import word_to_num

word = "example"
numeric_representation = word_to_num(word)

Number to Word Conversion:

python

from lexiquant import num_to_word

numeric_representation = 123456
word = num_to_word(numeric_representation)

Text Processing:

python

# Example usage in text processing
with open("input.txt", "r") as file:
    text = file.read()

words = text.split()
numeric_words = [word_to_num(word) for word in words]
processed_text = " ".join([num_to_word(num) for num in numeric_words])

with open("output.txt", "w") as file:
    file.write(processed_text)
