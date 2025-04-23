
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class VSM:
    def __init__(self):
        self.docs = {}
    def add_doc(self, doc_id, text):
        self.docs[doc_id] = text
    def tokenize(self, text):
        words = re.findall(r"\b\w+\b", text.lower())
        stop_words = set(stopwords.words("english"))
        filtered_words = set(x for x in words if x not in stop_words)
        return filtered_words
    def cal_csm(self, query):
        tokenized_docs = [self.tokenize(doc) for doc in self.docs.values()]
        tokenized_query = self.tokenize(query)
        preprocessed_docs = [" ".join(x) for x in tokenized_docs]
        preprocessed_query = " ".join(tokenized_query)
        vec = TfidfVectorizer()
        matrix = vec.fit_transform(preprocessed_docs)
        query_vec = vec.transform([preprocessed_query])
        cos_sim = cosine_similarity(query_vec, matrix)
        res = [(self.docs[i+1], cos_sim[0][i]) for i in range(2)]
        res.sort(key = lambda x: x[1], reverse = True)
        print(f"Query: {query}\n")
        for doc, sim in res:
            print(f"Similarity: {sim:.2f}\n{doc}\n")
vsm = VSM()
vsm.add_doc(1, "The sky is blue.")
vsm.add_doc(2, "shipment of gold damaged in a gold fire")
query = "gold silver truck"
vsm.cal_csm(query)
