# SentiCart- Sentiment Analysis Web App

This project is a user-friendly Sentiment Analysis Web Application powered by a fine-tuned **DistilBERT** model. Users can input text, and the app predicts whether the sentiment is **Positive 😊**, **Neutral 😐**, or **Negative 😠** using a trained deep learning model.

---

##  Features

-  Predict sentiment using a DistilBERT model (fine-tuned)
-  Real-time predictions with a REST API built using **Flask**
- Clean and modern **responsive frontend** using **HTML**, **CSS**, **Bootstrap**, and **JavaScript**
- Smooth animations and background effects
- Easy-to-deploy and open-source

---

## 📁 Project Structure
sentiment-analysis-app/
│
├── backend/
│ ├── app.py # Flask backend API
│ └── saved_model/ # Trained model files
│ ├── config.json
│ ├── model.safetensors
│ ├── tokenizer_config.json
│ ├── tokenizer.json
│ ├── special_tokens_map.json
│ └── vocab.txt
│
├── frontend/
│ ├── index.html # Webpage UI
│ ├── style.css # Styling and animations
│ └── script.js # Handles API requests
│
├── .gitignore
├── requirements.txt # Python dependencies
└── README.md # Project documentation
## ⚙️ Installation & Setup


## Model used: DistilBERTForSequenceClassification

Trained using Hugging Face's transformers library

Output Labels:

0: Negative 😠

1: Neutral 😐

2: Positive 😊


