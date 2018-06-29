from xml.etree import ElementTree as ET
from pre_processing import tokenize, remove_stop_words, stemming, remove_lf_words
import os
import json


key_word = 'Method'
word_list = ['Introduction', 'Results', 'Discussion']


def file2text(file):
    try:
        tree = ET.parse(file)
    except:
        return {'text': '',
                'format': 'error'}
    root = tree.getroot()
    texts = ''
    file_format = ''
    if root.tag == 'plain_text':
        for child in root:
            if child.text:
                texts += child.text
        file_format = 'text'
    elif root.tag == 'body':
        for child in root:
            if child.text:
                texts += child.text
        file_format = 'xml'
    else:
        file_format = 'other'

    return {'text': texts,
            'format': file_format}


def get_methods(input_text):
    text = ''
    if key_word.upper() in input_text:
        text = input_text.split(key_word.upper())[1]
        for word in word_list:
            if word.upper() in text:
                text = text.split(word.upper())[0]
    if key_word in input_text:
        text = input_text.split(key_word)[1]
        for word in word_list:
            if word in text:
                text = text.split(word)[0]
    return text


def load_file(path):
    texts = []
    num_files = 0
    num_methods = 0
    for file in os.listdir(os.path.join(path, 'data')):
        num_files += 1
        parsed_result = file2text(os.path.join(path, 'data', file))
        method_text = get_methods(parsed_result['text'])
        if method_text:
            token_text = stemming(remove_stop_words(tokenize(method_text)))
            texts.append(token_text)
            num_methods += 1
        if num_files % 1000 == 0:
            print(num_files, num_methods)
    with open(os.path.join(path, 'text', 'method_6272'), 'w') as f:
        json.dump(texts, f)
    print(num_files, num_methods)


if __name__ == '__main__':
    load_file(os.getcwd())

