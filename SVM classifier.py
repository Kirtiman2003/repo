from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC          # fast linear SVM for text
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


categories = [
    "alt.atheism",
    "soc.religion.christian",
    "comp.graphics",
    "sci.med",
]

train = fetch_20newsgroups(
    subset="train", categories=categories,
    remove=("headers", "footers", "quotes")
)
test  = fetch_20newsgroups(
    subset="test",  categories=categories,
    remove=("headers", "footers", "quotes")
)

text_clf = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1,2),          
        min_df=3                    
    )),
    ("svm", LinearSVC(C=1.0))       
])


text_clf.fit(train.data, train.target)


pred = text_clf.predict(test.data)
print(f"Accuracy: {accuracy_score(test.target, pred):.3f}\n")
print(classification_report(test.target, pred, target_names=categories))
