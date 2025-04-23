import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (only needs to run once)
nltk.download('stopwords')

class Inverted_Index:
    def __init__(self):
        self.index = {}
        self.docs = {}

    def tokenize(self, text):
        words = re.findall(r"\b\w+\b", text.lower())
        stop_words = set(stopwords.words("english"))
        filtered_words = set(x for x in words if x not in stop_words)
        return filtered_words

    def index_doc(self, doc_id, text):
        tokens = self.tokenize(text)
        for token in tokens:
            if token not in self.index:
                self.index[token] = []
            if doc_id not in self.index[token]:  # Avoid duplicates
                self.index[token].append(doc_id)
        self.docs[doc_id] = text

    def retrieve_doc(self, query):
        tokens = self.tokenize(query)
        rel_doc_id = set()
        for token in tokens:
            if token in self.index:
                rel_doc_id.update(self.index[token])
        res = {}
        for doc_id in rel_doc_id:
            res[doc_id] = self.docs[doc_id]
        return res

    def disp(self, res, form):
        print(f"\n{form} documents are:")
        if not res:
            print("No documents matched your query.")
        for doc_id, doc in res.items():
            print(f"{doc_id} : {doc}")

inverted_index = Inverted_Index()
inverted_index.index_doc(1, "Inverted index is a data structure has a class meeting.")
inverted_index.index_doc(2, "This is an example of index construction algorithm.")
inverted_index.index_doc(3, "The algorithm constructs an inverted index from documents.")

inverted_index.disp(inverted_index.docs, "Present")

query = input("\nPlease enter your query to retrieve documents: ")
res = inverted_index.retrieve_doc(query)
inverted_index.disp(res, "Retrieved")
