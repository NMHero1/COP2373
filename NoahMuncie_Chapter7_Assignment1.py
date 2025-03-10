# This program is designed to take a paragraph as an input and split it into each sentence and display the total amount of sentences.

# Import regular expressions
import re

# Define function to split the paragraph
def split_sentences(paragraph):

    # Define pattern to use
    sentence_pattern = r'(?<=[.!?])(?=\s*[A-Z0-9])'

    # Split the paragraph based on the pattern
    sentences = re.split(sentence_pattern, paragraph)
    return [s.strip() for s in sentences if s.strip()]

# Define main function to control the program
def main():

    # Get user input
    paragraph = input("Enter a paragraph: ")
    sentences = split_sentences(paragraph)

    # Print output
    print("\nIndividual Sentences:")

    # Enumerate through the list of sentences
    for idx, sentence in enumerate(sentences, start=1):
        print(f"{idx}. {sentence}")

    # Print the total number of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")

# Main
if __name__ == "__main__":
    main()
