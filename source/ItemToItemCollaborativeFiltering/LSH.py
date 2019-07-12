import numpy as np
import pandas as pd
import pickle
import math
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections

class LSH:
    def __init__(self, path, dataSize):
        self.path = path
        self.dataSize = dataSize

    def preprocess(self):
        ids = []
        meta = []
        data = []

        for i in range(self.dataSize):
            with open(self.path + str(i) + ".data", "rb") as file:
                f_song_id = pickle.load(file)
                f_songMeta = pickle.load(file)
                f_data = pickle.load(file)
                ids.append(f_song_id)
                meta.append(f_songMeta)
                data.append(f_data)

        self.id = np.array(ids)
        self.meta = np.array(meta)
        self.data = np.array(data)

    def generate_hashtable(self):
        self.engine = Engine(self.data.shape[1], lshashes=[RandomBinaryProjections('rbp', 20)])

        for i in range(self.dataSize):
            self.engine.store_vector(self.data[i], data = self.id[i])
    
    def query(self, data):
        return self.engine.neighbours(data)

data_size = 1164
lsh = LSH("Dataset/", data_size)
lsh.preprocess()
lsh.generate_hashtable()
for i in range(data_size):
    print("id: " + str(lsh.id[i]) + "; metadata: " + str(lsh.meta[i]))
    print("neighbours: ")
    print(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i]))))