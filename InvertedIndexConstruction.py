import re
from collections import defaultdict

documents = {
    "doc1": "The computer science students are appearing for practical examination.",
    "doc2": "computer science practical examination will start tomorrow."
}

def preprocess(text):
    text = text.lower()                      
    text = re.sub(r'[^\w\s]', '', text)      
    return text.split()                      


def build_inverted_index(docs):
    inverted_index = defaultdict(set)
    for doc_id, content in docs.items():
        tokens = preprocess(content)
        for token in tokens:
            inverted_index[token].add(doc_id)
    return inverted_index

def retrieve_documents(inverted_index, query_terms):
    result_sets = []
    for term in query_terms:
        result_sets.append(inverted_index.get(term, set()))
    if result_sets:
        return set.intersection(*result_sets)
    return set()

inverted_index = build_inverted_index(documents)

query = ["computer", "science"]
result = retrieve_documents(inverted_index, query)

print("Inverted Index:")
for term, doc_ids in inverted_index.items():
    print(f"{term}: {doc_ids}")
print("\nDocuments containing 'computer science':")
print(result)