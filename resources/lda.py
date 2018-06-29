from gensim import corpora, models

import json
import os

NUM_TOPICS = 25
PASSES = 100


def load_file(path):
    with open(os.path.join(path, 'text', 'small_sample.txt')) as f:
        texts = json.load(f)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=PASSES)
    #os.mkdir(os.path.join(path, 'lda_results', ))
    ldamodel.save(os.path.join(path, 'lda_results', 'lda_model'))
    dictionary.save(os.path.join(path, 'lda_results', 'dictionary'))


if __name__ == '__main__':
    load_file(os.getcwd())