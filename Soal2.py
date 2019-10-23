from pathlib import Path
from datetime import datetime, timedelta
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import pandas as pd
import locale
import nltk

nltk.download('punkt')
nltk.download('stopwords')

locale.setlocale(locale.LC_ALL, 'id_ID')

stopword = set(stopwords.words('indonesian'))
timeformat = f"%A, %d %B %Y - %H:%M"
tokenizer = RegexpTokenizer(r'\w+')

path = Path('data/')
data = dict()
data_all = dict()

pathlist = path.rglob('*.txt')

# membuat struktur data dengan membaca tanggal di file
try:
    for path in pathlist:
        with open(path, 'r') as file:
            data_file = file.readlines()
            if not data_file:
                continue
            raw_article = data_file[1:]
            rawtime = data_file[0][:-5]
            time = datetime.strptime(rawtime, timeformat)
            today = time.strftime(f'%#d')

            # print(today)

            if not data.get(today):
                data[today] = dict()

            data_article = []
            for article in raw_article:
                data_article += tokenizer.tokenize(article)

            for word in data_article:
                word = word.lower()
                if word in stopword:
                    continue
                if not data_all.get(word):
                    data_all[word] = 0
                data_all[word] += 1

                if data[today].get(word):
                    data[today][word] += 1
                else:
                    data[today][word] = 1
except IndexError:
    pass

# sorting data terbanyak
data_all = sorted(data_all.items(), key=lambda kv: kv[1], reverse=True)
data_terbanyak = data_all[:10]

# membuat struktur data terbanyak dalam 14 hari
kata_terbanyak = [word[0] for word in data_terbanyak]
jumlah_kata = [word[1] for word in data_terbanyak]


data_perhari = dict()
# print(data['10'])

# memasukkan data terbanyak per hari
for kata in kata_terbanyak:
    # print(kata)
    data_perhari[kata] = list()
    for i in range(30, 16, -1):
        if not data.get(str(i)):
            continue
        data_sehari = data[str(i)]

        if data[str(i)].get(kata):
            data_perhari[kata].append(data[str(i)][kata])
        else:
            data_perhari[kata].append(0)

data_perhari['x'] = range(1, 15)


# membuat histogram (soal no  2)
df = pd.DataFrame(data_perhari)
warna = ['red', 'black', 'gray', 'plum', 'purple', 'navy', 'blue',
         'brown', 'coral', 'orange', 'pink', 'green', 'yellow', 'cyan']

n = 0

for kata in kata_terbanyak:
    if kata == '1':
        continue
    plt.plot('x', kata, data=df, marker='', color=warna[n], linewidth=2)
    n += 1

plt.legend()

def point2():
    plt.show()
