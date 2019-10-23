from pathlib import Path

import nltk
from nltk.corpus import stopwords
from nltk import RegexpTokenizer
from datetime import datetime, timedelta
from datetimerange import DateTimeRange
import numpy as np
import matplotlib.pyplot as plt
import Soal2

nltk.download('punkt')
nltk.download('stopwords')

stopwords = set(stopwords.words('indonesian'))

path = Path()
tokenizer = RegexpTokenizer(r'\w+')

big_data = dict()

for path in path.rglob('data*.txt'):
    with open(path,'r') as file:
        data = file.read()
        data = tokenizer.tokenize(data)
        for word in data:
            word = word.lower()
            if word in stopwords:
                continue
            if big_data.get(word, None):
                big_data[word] += 1
            else:
                big_data[word] = 1

big_data = sorted(big_data.items(), key = lambda  kv: kv[1], reverse=True)
data_terbanyak = big_data[:10]

kata = [word[0] for word in data_terbanyak]
jumlah = [word[1] for word in data_terbanyak]



#  bar chart (soal no 1)
def poinOne():
    plt.rcdefaults()
    y_pos = [n for n in range(len(kata))]
    plt.bar(y_pos, jumlah, align='center', alpha=0.5)
    plt.xticks(y_pos, kata)
    plt.xlabel("\nkata")
    plt.ylabel('Jumlah kata')
    plt.title('10 Kata terbanyak')
    plt.show()

def poinTwo():
    Soal2.point2()

# pie chart (soal no 3)
def poinThree():
    colors = ['red','green','gray','plum','purple','navy','blue','brown','coral','orange']
    explode = (0,0,0,0,0,0,0,0,0,0,)
    plt.pie(jumlah, explode=explode, labels=kata, colors= colors, autopct='%1.1f%%',shadow=False,startangle=140)
    plt.title("Pie chart dalam persentase\n")
    plt.axis('equal')
    plt.show()

# Tampilan
def choose():
    inputNumber = input("Masukkan input Soal yang ingin ditampilkan: ")
    print(type(inputNumber))
    if inputNumber == "1":
            print("Anda memilih soal no 1")
            poinOne()
            choose()
    elif inputNumber == "2":
            print("Anda memilih soal no 2")
            poinTwo()
            choose()
    elif inputNumber == "3":
            print("Anda memilih soal no 3")
            poinThree()
            choose()
    elif inputNumber == "4":
        print("Anda sudah keluar dari program")
        exit()
    else:
            print("input hanya tersedia 1 sampai 3\n silahkan input ulang")
            choose()


print("Data Soal:")
print("Soal no 1: Tampilkan 10 kata dalam bentuk histogram (bar chart) yang paling banyak ditemukan dalam minimal 2.000 file teks tersebut. Susun secara descending order dalam chart.\n")
print("Soal no 2: Tampilkan tren 10 kata yang paling sering muncul tersebut dalam durasi waktu 14 hari. Pastikan garis tren berbeda untuk setiap kata dan penjelasannya ada dalam legend.\n")
print("Soal no 3: Ubah histogram pada poin 1 dalam bentuk pie-chart dengan nilai diubah menjadi persentase.\n")
choose()