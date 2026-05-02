# 📄 PDF Merger

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0%2B-orange.svg)](https://pypi.org/project/PyPDF2/)

A lightweight and efficient Python script to merge multiple PDF files into a single document. Simply drop the script into your folder with PDFs and run it — no configuration needed.

---

## ✨ Features

- 🔍 **Auto-Detection** — Automatically finds all PDF files in the current directory
- ⚡ **Zero Configuration** — No CLI arguments or setup required
- 📦 **Lightweight** — Minimal dependencies, just `PyPDF2`
- 🚀 **Fast Processing** — Merges PDFs in seconds
- 🖥️ **Cross-Platform** — Works on Windows, macOS, and Linux

---

## 📋 Requirements

- Python 3.6 or higher
- PyPDF2 library

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pdf-merger.git
   cd pdf-merger
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 Usage

1. Copy `merge.py` into the folder containing your PDF files
2. Run the script:
   ```bash
   python merge.py
   ```
3. A `merged.pdf` file will be created in the same directory

**Example:**
```
my-documents/
├── merge.py
├── chapter1.pdf
├── chapter2.pdf
├── chapter3.pdf
└── merged.pdf  ← Generated automatically
```

---

## ⚙️ How It Works

1. Scans the current directory for all `.pdf` files
2. Reads each PDF and extracts all pages
3. Combines them sequentially into a single PDF
4. Saves the output as `merged.pdf`

---

## 🛠️ Customization

Want to customize the behavior? Edit these variables in `merge.py`:

| Variable | Description | Default |
|----------|-------------|---------|
| `output_filename` | Name of the merged output file | `merged.pdf` |
| `pdf_extension` | File extension to search for | `.pdf` |

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/pdf-merger/issues).

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!
