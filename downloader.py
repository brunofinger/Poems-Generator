import os
import pandas as pd
import requests
import re
import spacy
from bs4 import BeautifulSoup
import argparse


def get_poem_links(writer):
    url = f"https://mypoeticside.com/poets/{writer}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    poem_list = soup.find(class_="list-poems")
    links = poem_list.find_all("a")
    poem_links = [f"https:{link.get('href')}" for link in links]
    return poem_links


def get_poem_content(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find(class_="title-poem").get_text()
    poem = soup.find(class_="poem-entry").find("p").get_text()
    return title, poem


def save_poems_to_csv(poems, file_path):
    df = pd.DataFrame({"title": [p[0] for p in poems], "text": [p[1] for p in poems]})
    df.to_csv(file_path, index=False)


def docs_to_sentences(file, split=r"\n"):
    df_docs = pd.read_csv(file)
    df_sentences = pd.DataFrame(columns=["doc_id", "sentence"])
    for i, text in enumerate(df_docs["text"]):
        # dictionary to replace unwanted elements
        replace_dict = {"?«": "«", "(": "", ")": "", ":": ",", ".": ",", ",,,": ",", '"': ""}
        for x, y in replace_dict.items():
            text = text.replace(x, y)
        text = text.lower()
        # split into sentences
        sentences = re.split(split, text)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        # save sentence and doc_id
        doc_sentences = pd.DataFrame({"doc_id": [i] * len(sentences), "sentence": sentences})
        df_sentences = df_sentences.append(doc_sentences)
    # extra cleaning and reset index
    df_sentences.reset_index(drop=True, inplace=True)
    # saves clean sentences to a .csv file
    output_file = os.path.splitext(file)[0] + "_sentences.csv"
    df_sentences.to_csv(output_file, index=False)


def main(writer):
    poem_links = get_poem_links(writer)
    poems = [get_poem_content(link) for link in poem_links]
    file_path = f"{writer}_poems.csv"
    save_poems_to_csv(poems, file_path)
    docs_to_sentences(file=file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--writer", required=True, help="Name of the writer to scrape poems")
    args = parser.parse_args()
    main(args.writer)
