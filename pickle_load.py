import pickle

dbfile = open('save.p', 'rb')
db = pickle.load(dbfile)
for keys in db:
    print(keys, '=>', db[keys])
    dbfile.close()
