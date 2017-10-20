import sys
import gensim
from gensim.models import Word2Vec

print("training model loading...")
try:
    model = Word2Vec.load("mymodel")
except FileNotFoundError:
    print("training data is not found.")
    print("training start:")
    sentences = gensim.models.word2vec.Text8Corpus("text8")
    model = gensim.models.word2vec.Word2Vec(sentences, size=200)
    model.save("mymodel")

print("model loading complete.")


def find_similar_word(word, similarity):
    # print(similarity)
    temp = model.most_similar(word, topn=50)
    similar_words = {word}
    for i in temp:
        if i[1] >= similarity:
            similar_words.add(i[0])
    # print(similar_words)
    while True:
        temp = similar_words.copy()
        for w in similar_words:
            for i in model.most_similar(w, topn=50):
                if model.similarity(i[0], word) >= similarity:
                    temp.add(i[0])
        if temp == similar_words:
            break
        similar_words = temp.copy()
    return similar_words


if __name__ == '__main__':
    word = input("Which word do you want to find its similar words?").strip()
    similarity = input("What is your desired similarity?").strip()
    if float(similarity) < 0 or float(similarity) > 1:
        print("similarity should be digit in [0,1], give up.")
        sys.exit()
    s1 = model.most_similar(word)
    print("The top ten  most similar word is:\n", s1)
    s2 = find_similar_word(word, float(similarity))
    print("The similar word in given similarity is:\n", s2)
