import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "Email": [
        "Win a free iPhone now",
        "Meeting at 5 PM",
        "Claim your lottery prize",
        "Project submission tomorrow",
        "Congratulations! You won cash",
        "Let's have lunch"
    ],
    "Label": [
        "Spam",
        "Ham",
        "Spam",
        "Ham",
        "Spam",
        "Ham"
    ]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df["Email"],
    df["Label"],
    test_size=0.3,
    random_state=42
)

vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))

# Test
email = ["Congratulations! Claim your free reward"]
email_vector = vectorizer.transform(email)

print("Prediction:", model.predict(email_vector)[0])