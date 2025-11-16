from flask import Flask, render_template, request
import fitz
import pytesseract
from PIL import Image
import docx
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text.strip()

def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")
    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif filename.endswith(".pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text("text")
        return text
    elif filename.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(file)
        return pytesseract.image_to_string(image)
    return ""

def calculate_similarity(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)
    cv = CountVectorizer(stop_words='english')
    vectors = cv.fit_transform([text1, text2]).toarray()
    sim = cosine_similarity(vectors)[0][1]
    return round(sim * 100, 2)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check", methods=["POST"])
def check():
    print("Received a request to /check")
    if "file1" not in request.files or "file2" not in request.files:
        return render_template("home.html", result="Please upload both files.")

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    text1 = extract_text(file1)
    text2 = extract_text(file2)

    if not text1.strip() or not text2.strip():
        return render_template("home.html", result="Text extraction failed from one or both files.")

    similarity = calculate_similarity(text1, text2)
    return render_template("home.html", result=f"Similarity: {similarity}%")

if __name__ == "__main__":
    app.run(debug=True)
