import json
import os


def load_file(path):
    metadata = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') and 'NGRAMS' not in file:
                try:
                    journal_name = root.split(path)[1].split('/')[2]
                except:
                    continue
                year = root.split(path)[1].split('/')[3]
                jstor_id = file.split('.txt')[0]
                metadata[jstor_id] = {'journal': journal_name,
                                      'year': year}
    with open(os.path.join(os.getcwd(), 'metadata', 'year_journal_3.json'), 'w') as f:
        json.dump(metadata, f)


if __name__ == '__main__':
    load_file('/home/renzi/Documents/Jstor_data')



