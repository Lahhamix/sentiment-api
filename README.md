# 🚀 Simple Sentiment Analysis API

A lightweight and collaborative AI API project built with **FastAPI** and a custom-trained **Naive Bayes** model. This API classifies input text as **positive** or **negative**. The project demonstrates collaborative development using **GitHub branches, commits, pull requests, and reviews**.

---

## 🎯 Project Goals

- Deploy a custom AI model as a REST API
- Collaborate via GitHub with feature branches, commits, and pull requests
- Document API usage with a test script and health check endpoint

---

## 🧠 How It Works

- The model is trained on a sample dataset using `CountVectorizer` + `MultinomialNB`
- The trained model is saved using `joblib`
- FastAPI exposes two endpoints: `/predict` and `/health`
- The API accepts JSON input, loads the model, and returns the sentiment

---

## 📁 Folder Structure

```
sentiment-api/
├── app/
│   ├── main.py          # FastAPI API code
│   └── model.joblib     # Saved trained model
├── train_model.py       # Training script
├── test_api.py          # Script to test the API
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api
```

### 2. (Optional) Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Train the Model

```
python train_model.py
```

### 5. Run the API

```
uvicorn app.main:app --reload
```

Visit the Swagger UI at:  
http://127.0.0.1:8000/docs

---

## 📬 API Endpoints

### 📍 `POST /predict`

**Request:**

```json
{
  "text": "I love this product!"
}
```

**Response:**

```json
{
  "input": "I love this product!",
  "sentiment": "positive"
}
```

---

### ❤️ `GET /health`

**Response:**

```json
{
  "status": "API is up and running"
}
```

---

## 🧪 Testing the API

You can test the API locally using the included script:

```
python test_api.py
```

**Example Output:**

```
Input Text: I love this!
Prediction: {'input': 'I love this!', 'sentiment': 'positive'}
```

This test hits the `/predict` endpoint with sample input.

---

## 🤝 GitHub Collaboration Workflow

This project follows a collaborative workflow:

- Each contributor created their own **feature branch**
- Changes were committed with descriptive messages
- **Pull Requests** were used for merging into `main`
- Each PR was **reviewed and approved** by the other collaborator

---

## 📌 Contributors

| Name              | Role |
|-------------------|------|
| **Hadi Elham** | Developed the FastAPI app and `/health` endpoint |
| **Zakaria Labban** | Created the test script and updated documentation |

---

## 🏁 Final Note

This project demonstrates a successful end-to-end deployment of an AI model API, with clean collaboration and documentation practices that align with real-world workflows.
