Features

1.Supports multiple file types: PDF, DOCX, TXT, JPG, PNG
2.OCR support for scanned documents & images
3.Smart text cleaning (lowercasing, removing symbols, spacing fixes)
4.Cosine Similarity based comparison
5.Flask web interface
6.Fast & easy to use



Tech Stack

1.Python
2.Flask
3.PyMuPDF (fitz) – PDF parsing
4.python-docx – Word document parsing
5.Pytesseract – OCR
6.scikit-learn – CountVectorizer & Cosine Similarity
7.HTML/CSS for frontend



Installation

1. Clone the repository
git clone https://github.com/your-username/plagiarism-detector.git
cd plagiarism-detector
2. Install dependencies
pip install -r requirements.txt
3. Install Tesseract (for OCR)

Windows: Install from https://github.com/tesseract-ocr/tesseract

Linux:
sudo apt install tesseract-ocr

macOS:
brew install tesseract

Run the App
python app.py




How It Works

1.User uploads two files
2.App extracts text using:
3.PyMuPDF (PDF)
4.python-docx (DOCX)
5.Pytesseract (Images)
6.Text is cleaned and vectorized
7.Cosine similarity score is generated
8.Result is displayed on the web page


Contributing

Pull requests are welcome!
Feel free to open issues for bugs or improvements.
