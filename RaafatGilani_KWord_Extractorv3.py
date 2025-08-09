# %%
import streamlit as st

import string
import re
import os

# Get the folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICT_DIR = os.path.join(BASE_DIR, "dictionaries")  # folder where .txt files are stored

def load_wordset(filename):
    filepath = os.path.join(DICT_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return set(f.read().split())

# Load all dictionaries. Putting dictionary file content as split string into variables--to be used later.
UHwords = load_wordset("UHwords.txt")
Ewords = load_wordset("Ewords.txt")
Pwords = load_wordset("Pwords.txt")
Cwords = load_wordset("CWords.txt")
JKnames = load_wordset("JKnames.txt")
Kwords = load_wordset("Kwords.txt")


# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Read file content (uploaded_file is already a file-like object)
    text = uploaded_file.read().decode("utf-8")

# Fix common patterns before punctuation removal.
text = re.sub(r"http\S+", "", text)                    # Remove URLs
text = re.sub(r'(?<=\w)-(?=\w)', ' ', text)            # Fix hyphenated words like "forty-year-old"
text = re.sub(r'(?<=\w)—(?=\w)', ' ', text)            # Fix emdashed words like "Yes—never again!"

# Replace necessary punctuation (avoiding certain ones) with space.
text = re.sub(r"[‘…–“”—©.,?%!:;()\[\]{}]", " ", text)

# Lowercase the text
text = text.lower()

# Remove digits
text = re.sub(r"\d+", "", text)

# Split into words
cleantext = text.split()

# %%
def nonEnglish(cleantext):
    container = []
    for word in cleantext:  # Loop over words for matching.
        if word in Ewords: # Skip over existing English words.
            continue
        elif word in UHwords: # Skip over existing Urdu/Hindi words.
            continue
        elif word in Cwords: # Skip over recognised English contractions that use apostrophe.
            continue
        elif word in Kwords: 
            container.append(word) # Add known Kashmiri words.
        elif word in Pwords: 
            container.append(word) # Add known proper nouns.
        elif word in JKnames:
            container.append(word) # Add known J&K place names.
        else:
            container.append(word) # Add remaining words to container.

    result = sorted(set(container))
    print(f"Total non-English words: {len(result)}")
    return result


nonEnglish(cleantext)

st.write("File uploaded successfully!")
st.text_area("File Content Preview", text, height=300)



