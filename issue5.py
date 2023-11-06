import math

class TfidfVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.word_count = 0
        self.idf_vector = None

    def fit_transform(self, corpus):
        self.vocabulary = {}
        self.word_count = 0
        num_documents = len(corpus)

        for document in corpus:
            words = document.lower().split()
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary[word] = self.word_count
                    self.word_count += 1

        count_matrix = [[0] * self.word_count for _ in range(num_documents)]

        for i, document in enumerate(corpus):
            words = document.lower().split()
            for word in words:
                word_index = self.vocabulary[word]
                count_matrix[i][word_index] += 1

        self.idf_vector = [1.0 + math.log((num_documents + 1) / (sum(1 for document in count_matrix if document[i] > 0) + 1)) for i in range(self.word_count)]

        tfidf_matrix = []

        for document in count_matrix:
            total_words = sum(document)
            tfidf_vector = [round((count / total_words) * idf, 3) for count, idf in zip(document, self.idf_vector)]
            tfidf_matrix.append(tfidf_vector)

        return tfidf_matrix

    def get_feature_names(self):
        return list(self.vocabulary.keys())

corpus = [
   'Crock Pot Pasta Never boil pasta again',
   'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
for vector in tfidf_matrix:
    print(vector)