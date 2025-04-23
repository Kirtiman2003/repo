import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

class NaiveBayes:
    def __init__(self):
        self.class_probabilities = None
        self.word_probabilities = None
    
    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.classes = np.unique(y)
        num_classes = len(self.classes)
        
        self.class_probabilities = np.zeros(num_classes)
        for i, c in enumerate(self.classes):
            self.class_probabilities[i] = np.sum(y == c) / num_samples
        
        self.word_probabilities = np.zeros((num_classes, num_features))
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            total_word_counts = np.sum(X_c, axis=0)
            self.word_probabilities[i] = (total_word_counts + 1) / (np.sum(total_word_counts) + num_features)
    
    def predict(self, X):
        num_samples, _ = X.shape
        predictions = np.zeros(num_samples, dtype=int)
        for i in range(num_samples):
            probabilities = np.zeros(len(self.classes))
            for j, c in enumerate(self.classes):
                probabilities[j] = np.log(self.class_probabilities[j]) + np.sum(np.log(self.word_probabilities[j]) * X[i])
            predictions[i] = self.classes[np.argmax(probabilities)]
        return predictions

corpus = [
    "This movie is great and enjoyable.",
    "I really liked this film!",
    "The acting was terrible.",
    "Such a waste of time.",
    "Not worth watching."
]
labels = [0, 1, 0, 0, 0]

X_train, X_test, y_train, y_test = train_test_split(corpus, labels, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


print("Using custom NaiveBayes implementation:")
custom_classifier = NaiveBayes()
custom_classifier.fit(X_train_vectorized.toarray(), y_train)
custom_predictions = custom_classifier.predict(X_test_vectorized.toarray())

for i, (test, prediction) in enumerate(zip(X_test, custom_predictions)):
    print(f"Test Data: '{test}'")
    print(f"Predicted Label: {prediction}")

custom_accuracy = accuracy_score(y_test, custom_predictions)
print("Custom Accuracy:", custom_accuracy)

print("\nUsing sklearn's MultinomialNB:")
sklearn_classifier = MultinomialNB()
sklearn_classifier.fit(X_train_vectorized, y_train)
sklearn_predictions = sklearn_classifier.predict(X_test_vectorized)

for i, (test, prediction) in enumerate(zip(X_test, sklearn_predictions)):
    print(f"Test Data: '{test}'")
    print(f"Predicted Label: {prediction}")

sklearn_accuracy = accuracy_score(y_test, sklearn_predictions)
print("Sklearn Accuracy:", sklearn_accuracy)
