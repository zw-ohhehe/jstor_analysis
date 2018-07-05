import glob
import os


def move_txt(path, new_path):
    n = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                journal_name = root.split(path)[1].split('/')[2]
            except:
                print(os.path.join(root, file))
            if file.endswith('.txt') and 'NGRAMS' not in file:
                n += 1
                if not os.path.exists(os.path.join(new_path, journal_name)):
                    os.mkdir(os.path.join(new_path, journal_name))
                    print(journal_name)
                os.rename(os.path.join(root, file), os.path.join(new_path, journal_name, file))
                if n % 10000 == 0:
                    print(n)


if __name__ == '__main__':
    move_txt('/home/renzi/Documents/Jstor_data', '/home/renzi/Documents/Jstor_txt_data')