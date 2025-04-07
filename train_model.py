from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample training data
texts = [
    "I love this product", "This is amazing", "Happy and satisfied", "Best experience",
    "I hate this", "This is terrible", "Worst ever", "Not happy", "Very disappointed"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1 = positive, 0 = negative

# Create pipeline: vectorizer + classifier
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(texts, labels)

# Save the model
joblib.dump(model, 'app/model.joblib')

print("✅ Model trained and saved to app/model.joblib")
