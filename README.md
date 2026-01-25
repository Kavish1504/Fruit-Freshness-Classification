# 🍎 Fruit Freshness Classification System

An AI-powered web application that classifies fruit images as **Fresh** or **Rotten** using a CNN model.  
Built with **Flask**, **TensorFlow/Keras**, and a modern **HTML + JavaScript** frontend.

---

## 🚀 Features

- Upload fruit images and get instant predictions
- Deep Learning–based CNN classifier
- Clean, responsive UI
- Handles multiple backend response formats safely
- CORS enabled for local and remote usage
- Displays raw model response for debugging

---

## 🛠 Tech Stack

### Backend
- Python 3.8+
- Flask
- TensorFlow / Keras
- OpenCV
- Flask-CORS

### Frontend
- HTML5
- CSS3
- Bootstrap 4
- JavaScript (jQuery)

---

## ⚙️ Installation & Setup (VS Code)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Kavish1504/Fruit-Freshness-Classification.git
cd Fruit-Freshness-Classification

# create virtual environment
conda create -m venv python==3.8 -y

# activate virtual environment
conda activate venv

# install required dependencies
pip install -r requirements.txt

# run the Flask application
python app.py

# Open Your Browser at
http://localhost:8080
