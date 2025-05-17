async function analyzeSentiment() {
  const text = document.getElementById('inputText').value;
  const resultDiv = document.getElementById('result');

  if (!text.trim()) {
    resultDiv.className = "mt-4 alert alert-warning fade-in";
    resultDiv.textContent = "Please enter some text!";
    resultDiv.classList.remove("d-none");
    return;
  }

  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text })
  });

  const result = await response.json();
  const sentiment = ["Negative 😠", "Neutral 😐", "Positive 😊"][result.sentiment];
  const alertClass = ["danger", "secondary", "success"][result.sentiment];

  resultDiv.className = `mt-4 alert alert-${alertClass} fade-in`;
  resultDiv.textContent = `Sentiment: ${sentiment}`;
  resultDiv.classList.remove("d-none");
}
