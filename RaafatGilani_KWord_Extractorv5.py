import streamlit as st
import re
import os
import csv
from io import StringIO

# =====================
# 1️⃣ Load Dictionaries
# =====================
def load_wordset(filename):
    file_path = os.path.join("dictionaries", filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return set(f.read().split())
    except FileNotFoundError:
        st.error(f"Dictionary file not found: {filename}")
        return set()

UHwords = load_wordset("UHwords.txt")
Ewords = load_wordset("Ewords.txt")
Pwords = load_wordset("Pwords.txt")
Cwords = load_wordset("CWords.txt")
JKnames = load_wordset("JKnames.txt")
Kwords = load_wordset("Kwords.txt")

# =====================
# 2️⃣ Streamlit UI
# =====================
st.title("Kashmiri Word Extractor")

uploaded_file = st.file_uploader("Upload a TXT file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    # =====================
    # 3️⃣ Cleaning Logic
    # =====================
    text = re.sub(r"http\S+", "", text)                    # Remove URLs
    text = re.sub(r'(?<=\w)-(?=\w)', ' ', text)            # Fix hyphenated words
    text = re.sub(r'(?<=\w)—(?=\w)', ' ', text)            # Fix em-dash words
    text = re.sub(r"[‘…–“”—©.,?%!:;()\[\]{}]", " ", text)  # Replace punctuation with space
    text = text.lower()
    text = re.sub(r"\d+", "", text)                        # Remove digits

    cleantext = text.split()

    # =====================
    # 4️⃣ Processing Logic
    # =====================
    def nonEnglish(cleantext):
        container = []
        for word in cleantext:
            if word in Ewords:
                continue
            elif word in UHwords:
                continue
            elif word in Cwords:
                continue
            elif word in Kwords:
                container.append(word)
            elif word in Pwords:
                container.append(word)
            elif word in JKnames:
                container.append(word)
            else:
                container.append(word)
        return sorted(set(container))

    result = nonEnglish(cleantext)

    # =====================
    # 5️⃣ Display + Download
    # =====================
    st.success(f"Total extracted words: {len(result)}")
    st.text_area("Extracted Words", "\n".join(result), height=300)

    # Create CSV string using csv module
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Extracted Words"])  # header
    for word in result:
        writer.writerow([word])

    st.download_button(
        label="📥 Download as CSV",
        data=csv_buffer.getvalue(),
        file_name="extracted_words.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a TXT file to begin.")