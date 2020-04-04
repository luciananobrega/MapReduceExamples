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
    for line in v.splitlines():
        if k == "data\\sells.csv":
            yield line.split(';')[0], 'Sells' + ':' + line.split(';')[5]
        if k == "data\\branch.csv":
            yield line.split(';')[0], 'Branch' + ':' + line.split(';')[1]

def reducefn(k, v):
    print('reduce' + k)
    total = 0
    for item in v:
        if item.split(":")[0] == 'Sells':
            total += int(item.split(':')[1])
        if item.split(":")[0] == "Branch":
            nameBranch = item.split(":")[1]
    L = list()
    L.append(nameBranch + " , " + str(total) )
    return L

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("Result.csv", "w"))
for k, v in results.items():
    x = str(v).replace("[", "").replace("'", "").replace(']', '')
    w.writerow([k, x])