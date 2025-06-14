
from flask import Flask, request, jsonify
from flask_cors import CORS

def detect_phishing(prompt):
    phishing_keywords = ["password", "urgent", "verify", "account", "click here", "login"]
    score = sum(word in prompt.lower() for word in phishing_keywords)
    if score > 2:
        return "Likely Phishing Email"
    elif score > 0:
        return "Possibly Suspicious"
    else:
        return "Safe Email"

app = Flask(__name__)
CORS(app)

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = detect_phishing(prompt)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
