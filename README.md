# 🧩 PDF Merge Tool

This is a simple and interactive Python script to **merge multiple PDF files** from a folder into a single PDF.  
The tool supports file reordering, selective removal, and progress tracking using a command-line interface.

## ✅ Features

- Lists all PDF files in a folder
- Allows manual removal and reordering before merging
- Displays progress with a progress bar
- Handles errors gracefully

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ratzlord3125/pdf-merge-tool.git
cd pdf-merge-tool
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install PyPDF2 tqdm
```

---

## 🚀 How to Use

Run the script using Python:

```bash
python merge_pdfs.py
```

You’ll see a menu like this:

```markdown
📝 PDF Merger - Menu
---------------------
1. Merge PDF files in a folder
2. Exit
```

### Example Run

1. **Select option** `1`  
2. **Enter the full path** to the folder containing PDF files  
3. **Enter the desired output file path** (e.g., `merged_output.pdf`)  
4. **Use the interactive menu** to remove or reorder files  
5. **Proceed with merging** and watch the progress bar!

---

## 📂 Example Folder Structure

```sql
pdf-merge-tool/
│
├── merge_pdfs.py         # <-- Your main script
├── README.md             # <-- This file
└── some_folder/
    ├── file1.pdf
    ├── file2.pdf
    └── ...
```

---

## 📄 Output

The final merged PDF will be saved to the path you specified, combining all selected and reordered PDF files.

---

## 💡 Requirements

- Python 3.6+
- Works with large PDFs (tested > 500MB)

---

## 🛠 Dependencies

- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [tqdm](https://pypi.org/project/tqdm/)

---

## 📃 License

This project is open-source under the MIT License.

---