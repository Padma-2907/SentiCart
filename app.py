from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
from flask_cors import CORS  # Only if frontend is on a different port

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (helpful when frontend is separate)

# ✅ Correct path to your model folder (raw string or forward slashes)
MODEL_PATH = r"D:\sentiment_analysis_f\saved_model"

# Load the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

# Label mapping
label_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    # Tokenize and predict
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=1).item()

    return jsonify({
        'sentiment': predicted_class,
        'label': label_map[predicted_class]
    })

@app.route('/')
def home():
    return "API is running. Send POST to /predict."

if __name__ == '__main__':
    app.run(debug=True)
