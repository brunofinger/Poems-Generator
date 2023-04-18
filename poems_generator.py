import os
import argparse
import spacy
import numpy as np

def format_poem(text):
    """
    Formats the generated poem by capitalizing the first letter and adding a period at the end.
    """
    text = text[:1].upper() + text[1:]
    text = text[:-1] + '.'
    return text

def poem_generator(file, word, n_lines=4):
    """
    Generates a poem given a file with a collection of sentences and a starting word.
    """
    # Load the English model from Spacy
    nlp = spacy.load("en_core_web_sm")
    # Initialize the string to start the poem
    init_str = nlp(word.strip())
    # Read the sentences from the file
    if not os.path.exists(file):
        raise FileNotFoundError(f"{file} does not exist.")
    with open(file, 'r') as f:
        sentences = [line.strip() for line in f]
    # Check if there are enough unique sentences in the file
    if len(set(sentences)) < n_lines:
        raise ValueError("Not enough unique sentences in the file.")
    # Generate the poem
    poem = []
    for i in range(n_lines):
        # Shuffle the sentences
        np.random.shuffle(sentences)
        # Compute the similarity of each sentence to the initial string
        sim_list = [init_str.similarity(nlp(sent)) for sent in sentences]
        # Select the most similar sentence that has not been used in the poem
        sent_index = np.argmax(sim_list)
        while sentences[sent_index] in poem:
            sim_list[sent_index] = -1.0
            sent_index = np.argmax(sim_list)
            sent = sentences[sent_index]
            # Add the selected sentence to the poem
            poem.append(sent)
            # Update the initial string with the selected sentence
            init_str = nlp(sent.strip())
    # Join the sentences with line breaks
    str_poem = "\n".join(poem)
    return format_poem(str_poem)

if __name__ == "main":
    parser = argparse.ArgumentParser(description="Generates a poem based on a file with sentences and a starting word.")
    parser.add_argument("-f", "--file", type=str, required=True, help="File with sentences to use in the poem.")
    parser.add_argument("-w", "--word", type=str, required=True, help="Starting word for the poem.")
    parser.add_argument("-n", "--n_lines", type=int, default=4, help="Number of lines in the poem.")
    args = parser.parse_args()
    try:
        poem = poem_generator(args.file, args.word, args.n_lines)
        print(poem)
    except Exception as e:
        print(f"Error generating poem: {e}")