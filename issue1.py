#задача 1
from functools import total_ordering

class CountVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.word_count = 0

    def fit_transform(self, corpus):
        for document in corpus:
            words = document.lower().split()  
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary[word] = self.word_count
                    self.word_count += 1

        count_matrix = [[0] * self.word_count for _ in range(len(corpus))]
        for i, document in enumerate(corpus):
            words = document.lower().split()  
            for word in words:
                word_index = self.vocabulary[word]
                count_matrix[i][word_index] += 1

        return count_matrix
    

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(count_matrix)