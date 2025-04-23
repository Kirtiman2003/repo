import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt')
nltk.download('stopwords')


documents = [
    "The cat is on the mat.",
    "The dog is in the yard.",
    "A bird is flying in the sky.",
    "The sun is shining brightly."
]


stop_words = set(nltk.corpus.stopwords.words('english'))


def custom_analyzer(text):
    tokens = nltk.word_tokenize(text)
    return [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]


vectorizer = TfidfVectorizer(analyzer=custom_analyzer)
tfidf_matrix = vectorizer.fit_transform(documents)


def answer_question(query, documents, tfidf_matrix, vectorizer):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_idx = similarities.argmax()
    return documents[most_similar_idx]


query = "Where is the cat?"
answer = answer_question(query, documents, tfidf_matrix, vectorizer)
print("Answer:", answer)
