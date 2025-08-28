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

mode = st.radio("Choose extraction mode:","All Non-English words*", "Kashmiri words only*")

uploaded_file = st.file_uploader("Upload a TXT file", type=["txt"])
text = uploaded_file

if st.radio == "All non-English words*":
    text = re.sub(r"http\S+", "", text)                    # Remove URLs
    text = re.sub(r'(?<=\w)-(?=\w)', ' ', text)            # Fix hyphenated words
    text = re.sub(r'(?<=\w)—(?=\w)', ' ', text)            # Fix em-dash words
    text = re.sub(r"[‘…–“”—©.,?%!:;()\[\]{}]", " ", text)  # Replace punctuation with space
    text = text.lower()
    text = re.sub(r"\d+", "", text)                        # Remove digits

    cleantext = text.split()

    # =====================
    # non-English Processing Logic
    # =====================
    def nonEnglish(cleantext):
        container = []
        for word in cleantext:
            if word in Ewords:
                continue
            elif word in Cwords:
                continue
            elif word in JKnames:
                continue
            elif word in UHwords:
                container.append(word)
            elif word in Kwords:
                container.append(word)
            elif word in Pwords:
                container.append(word)
            else:
                container.append(word)
        return sorted(set(container))

    result = nonEnglish(cleantext)

    # =====================
    # non-English Display + Download
    # =====================
    st.success(f"Total non-English extracted words: {len(result)}")
    st.text_area("Extracted Words", "\n".join(result), height=300)

    # Create CSV string using csv module
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Extracted non-English Words"])  # header
    for word in result:
        writer.writerow([word])

    st.download_button(
        label="📥 Download as CSV",
        data=csv_buffer.getvalue(),
        file_name="extracted_non_english_words.csv",
        mime="text/csv"
    )
elif st.radio == "Kashmiri words only*":
    text = re.sub(r"http\S+", "", text)                    # Remove URLs
    text = re.sub(r'(?<=\w)-(?=\w)', ' ', text)            # Fix hyphenated words
    text = re.sub(r'(?<=\w)—(?=\w)', ' ', text)            # Fix em-dash words
    text = re.sub(r"[‘…–“”—©.,?%!:;()\[\]{}]", " ", text)  # Replace punctuation with space
    text = text.lower()
    text = re.sub(r"\d+", "", text)                        # Remove digits

    cleantext = text.split()

    # =====================
    # Kashmiri words exclusive processing logic
    # =====================
    def KashmiriWords(cleantext):
        container = []
        for word in cleantext:
            if word in Ewords:
                continue
            elif word in Cwords:
                continue
            elif word in JKnames:
                container.append(word)
            elif word in UHwords and Kwords:
                container.append(word)
            elif word in Kwords:
                container.append(word)
            elif word in Pwords:
                container.append(word)
            else:
                container.append(word)
        return sorted(set(container))

    result = KashmiriWords(cleantext)

    # =====================
    # non-English Display + Download
    # =====================
    st.success(f"Total extracted Kashmiri words: {len(result)}")
    st.text_area("Extracted Words", "\n".join(result), height=300)

    # Create CSV string using csv module
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Extracted Kashmiri Words"])  # header
    for word in result:
        writer.writerow([word])

    st.download_button(
        label="📥 Download as CSV",
        data=csv_buffer.getvalue(),
        file_name="extracted_Kashmiri_words.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a TXT file to begin.")  