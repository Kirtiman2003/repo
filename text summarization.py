import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.cluster.util import cosine_distance
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')
def sentence_similarity(sent1, sent2):
    stopwords_list = stopwords.words('english')
    word_vector1 = [word.lower() for word in sent1 if word.lower() not in stopwords_list]
    word_vector2 = [word.lower() for word in sent2 if word.lower() not in stopwords_list]
    all_words = list(set(word_vector1 + word_vector2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    for word in word_vector1:
        vector1[all_words.index(word)] += 1
    for word in word_vector2:
        vector2[all_words.index(word)] += 1
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 != idx2:
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2])
    return similarity_matrix
def generate_summary(text, num_sentences):
    sentences = sent_tokenize(text)
    sentence_tokens = [word_tokenize(sentence) for sentence in sentences]
    similarity_matrix = build_similarity_matrix(sentence_tokens)
    scores = np.array([np.sum(similarity_matrix[i]) for i in range(len(sentences))])
    scores /= scores.sum()
    ranked_sentences = [sentence for _, sentence in sorted(zip(scores, sentences), reverse=True)]
    return " ".join(ranked_sentences[:num_sentences])

text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial
intelligence concerned with the interactions between computers and human language, in
particular how to program computers to process and analyze large amounts of natural language
data. The goal is to enable computers to understand, interpret, and generate human language in
a way that is both meaningful and useful.
Text summarization is the process of distilling the most important information from a source (or
sources) to produce a concise and coherent summary. There are two main approaches to text
summarization: extractive and abstractive. Extractive summarization involves selecting and
combining key phrases or sentences from the source text, while abstractive summarization
involves generating new sentences that capture the main ideas of the original text.
TextRank is a popular algorithm for extractive text summarization. It is based on the PageRank
algorithm used by Google to rank web pages in search results. TextRank works by treating
sentences as nodes in a graph, with edges representing the similarity between sentences. The
algorithm then iteratively calculates a score for each sentence based on the scores of its
neighboring sentences, similar to how PageRank calculates the importance of web pages based
on the links between them.
In this example, we'll implement a simple extractive text summarization algorithm using
TextRank and NLTK. We'll start by tokenizing the input text into sentences and words, then
build a similarity matrix based on the cosine similarity between sentence vectors. Finally, we'll
use PageRank to rank the sentences and select the top-ranked sentences as the summary.
"""
summary = generate_summary(text, num_sentences=3)
print(summary)
