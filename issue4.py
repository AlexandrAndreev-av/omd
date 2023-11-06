import math

class TfidfTransformer:
    def fit_transform(self, count_matrix):
        num_documents = len(count_matrix)
        num_words = len(count_matrix[0])
        tfidf_matrix = []
        idf_vector = [1.0 + math.log((num_documents + 1) / (sum(1 for document in count_matrix if document[i] > 0) + 1)) for i in range(num_words)]

       
        for document in count_matrix:
            total_words = sum(document)
            tfidf_vector = [round((count / total_words) * idf, 3) for count, idf in zip(document, idf_vector)]
            tfidf_matrix.append(tfidf_vector)

        return tfidf_matrix
count_matrix = [
   [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]

transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count_matrix)

for vector in tfidf_matrix:
    print(vector)