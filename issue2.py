def tf_transform(count_matrix):
    tf_matrix = []
    for vector in count_matrix:
        total_words = sum(vector)
        tf_vector = [f"{round(count / total_words, 3):.3f}".rstrip('0').rstrip('.') if total_words > 0 else "0" for count in vector]
        tf_matrix.append(tf_vector)
    return tf_matrix
count_matrix = [
   [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]

tf_matrix = tf_transform(count_matrix)

for vector in tf_matrix:
    print(f"[{', '.join(vector)}]")