from gensim import models
from gensim.corpora import Dictionary
import pyLDAvis.gensim
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import json


def visualize_lda(path):
    lda_model = models.LdaModel.load(os.path.join(path, 'lda_results', '100k', 'lda_model'))
    dictionary = Dictionary.load(os.path.join(path, 'lda_results', '100k', 'dictionary'))
    with open(os.path.join(path, 'text', 'method_100k.json')) as f:
        texts = json.load(f)
    corpus = [dictionary.doc2bow(text) for text in texts]
    vis_data = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    pyLDAvis.display(vis_data)
    pyLDAvis.save_html(vis_data, os.path.join(path, 'lda_html', 'lda_100k.html'))


if __name__ == '__main__':
    visualize_lda(os.getcwd())