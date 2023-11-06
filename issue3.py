import math

def idf_transform(count_matrix):
    num_documents = len(count_matrix)
    idf_vector = [round(1.0 + math.log((num_documents + 1) / (sum(1 for document in count_matrix if document[i] > 0) + 1)), 1) for i in range(len(count_matrix[0]))]
    return idf_vector

count_matrix = [
   [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]

idf_matrix = idf_transform(count_matrix)

print(idf_matrix)