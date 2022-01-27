import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
samples = [doc for doc in os.listdir() if doc.endswith('.txt')]
sample_contents = [open(File).read() for File in samples]
 
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
plag_percentage = lambda doc1, doc2: cosine_similarity([doc1, doc2])
 
vectors = vectorize(sample_contents)
s_vectors = list(zip(samples, vectors))
 
def check_plagiarism():
    results = set()
    global s_vectors
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        i = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[i]
        for sample_b, text_vector_b in new_vectors:
            sim_score = plag_percentage(text_vector_a, text_vector_b)[0][1]
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], sim_score
            results.add(score)
    return results
 
for data in check_plagiarism():
    print(data)    