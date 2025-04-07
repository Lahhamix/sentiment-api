# 🚀 Simple Sentiment Analysis API

This project demonstrates how to build and deploy a simple sentiment analysis API using **FastAPI** and a **custom-trained scikit-learn model**. It also includes collaborative development using **GitHub workflows**.

---

## 🔧 Features

- ✅ REST API with FastAPI
- ✅ Custom-trained Naive Bayes classifier
- ✅ Predicts `positive` or `negative` sentiment
- ✅ Lightweight and beginner-friendly
- ✅ Git-based collaboration workflow

---

## 🧠 How It Works

The model is trained on a small dataset of labeled text using `CountVectorizer` and `MultinomialNB`, then saved using `joblib`. FastAPI loads the saved model and exposes an endpoint to receive text input and return a sentiment prediction.

---

## 📁 Project Structure

