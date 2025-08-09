import streamlit as st
import re
import string
import os

# =====================
# 1️⃣ Load Resources
# =====================
# Helper function to load dictionary files from the 'dictionaries' folder
def load_word_set(filename):
    file_path = os.path.join("dictionaries", filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return set(f.read().split())
    except FileNotFoundError:
        st.error(f"Dictionary file not found: {filename}")
        return set()

# Load all word sets
UHwords = load_word_set("UHwords.txt")
Ewords = load_word_set("Ewords.txt")
Pwords = load_word_set("Pwords.txt")
Cwords = load_word_set("CWords.txt")
JKnames = load_word_set("JKnames.txt")
Kwords = load_word_set("Kwords.txt")

# =====================
# 2️⃣ File Upload & Cleaning
# =====================
st.title("Word Extractor Tool")

uploaded_file = st.file_uploader("Upload a TXT file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    # Text cleaning
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = text.lower()

    st.subheader("File Content Preview")
    st.text_area("Preview", text[:2000], height=300)

    # =====================
    # 3️⃣ Processing & Output
    # =====================

    def nonEnglish(text):
        return [word for word in text.split() if word not in Ewords]

    def persianOnly(text):
        return [word for word in text.split() if word in Pwords]

    def customWords(text):
        return [word for word in text.split() if word in Kwords]

    def unknownWords(text):
        return [word for word in text.split() if word not in Ewords and word not in Pwords]

    st.subheader("Processing Results")
    st.write("Non-English Words:", nonEnglish(text))
    st.write("Persian Words:", persianOnly(text))
    st.write("Custom Words:", customWords(text))
    st.write("Unknown Words:", unknownWords(text))

else:
    st.info("Please upload a TXT file to begin.")
