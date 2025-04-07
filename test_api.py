import requests

url = "http://127.0.0.1:8000/predict"
data = {"text": "I love this!"}
response = requests.post(url, json=data)

print("Input Text:", data["text"])
print("Prediction:", response.json())