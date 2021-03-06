import mincemeat
import glob
import csv

text_files = glob.glob("data\\*")

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def mapfn(k, v):
    print('map ' + k)
    from stop_words import get_stop_words
    allStopWords = get_stop_words('en')

    for line in v.splitlines():
        authors = line.split(':::')[1].split('::')
        title = line.split(':::')[2].replace(',', '').replace('.', '')

        for word in title.split():
            if (word not in allStopWords):
                yield word, 1

def reducefn(k, v):
    print('reduce' + k)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("Result.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])