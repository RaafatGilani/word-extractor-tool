# Word Extractor

A Streamlit-based tool for extracting **non-English and Romanized Kashmiri words** from plain text files. Built with dictionary-matching logic, it's designed to help researchers, linguists, and language enthusiasts identify and collect words from underrepresented languages — especially Kashmiri — within multilingual or code-switched text.

---

## Features

- **Two extraction modes:**
  - **All Non-English Words** — strips out common English and common-word noise, returning everything else
  - **Kashmiri Words Only** — applies a focused Kashmiri dictionary filter using multiple specialized word lists
- Upload any `.txt` file and get results instantly
- Extracted words are displayed in-app and downloadable as a **CSV file**
- Automatic text cleaning: removes URLs, punctuation, digits, and normalizes hyphenation
- Tilted toward **higher recall** — better to capture a few extras than miss real Kashmiri words

---

## How It Works

The tool loads several dictionary files from the `dictionaries/` folder at startup:

| File | Purpose |
|---|---|
| `Ewords.txt` | Common English words to exclude |
| `CWords.txt` | Additional common/stopwords to exclude |
| `Kwords.txt` | Kashmiri vocabulary |
| `UHwords.txt` | Urdu/Hindi words that overlap with Kashmiri |
| `Pwords.txt` | Punjabi words |
| `JKnames.txt` | Jammu & Kashmir proper names |

In **Non-English mode**, any word not found in the English or common-word lists is kept. In **Kashmiri-only mode**, a layered logic is applied — words are included if they appear in the Kashmiri, Punjabi, or name dictionaries, with Urdu/Hindi words only included when they also appear in the Kashmiri list.

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)

### Installation

```bash
git clone https://github.com/RaafatGilani/word-extractor-tool.git
cd word-extractor-tool
pip install streamlit
```

### Running the App

```bash
streamlit run RaafatGilani_KWord_Extractorv5.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## Usage

1. Choose an extraction mode: **All Non-English Words** or **Kashmiri Words Only**
2. Upload a `.txt` file
3. View the extracted word list in the app
4. Download the results as a CSV

> **Tip:** If your source document is in a different format (PDF, DOCX, etc.), convert it to `.txt` first using a tool like [Convertio](https://convertio.co/).

---

## Limitations

- Only `.txt` files are supported currently (more formats coming soon)
- Dictionary-matching means some words may be incorrectly included or excluded — this is expected behavior
- The tool is optimized for **Romanized Kashmiri**, not Nastaliq/Perso-Arabic script

---

## Contributing & Feedback

Feedback and collaboration are welcome! Reach out via the [contact form](https://www.raafatgilani.com/contact-10) on the author's website.

---

## License

This project is licensed under the [MIT License](LICENSE.md).
