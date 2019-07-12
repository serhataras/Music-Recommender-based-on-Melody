import pickle
import math
import numpy as np
from sklearn.manifold import TSNE
from scipy.spatial import KDTree

class NNRecommendation:
    def __init__(self, path, dataSize, leafSize):
        self.path = path
        self.dataSize = dataSize
        self.leafSize = leafSize

    def preprocess(self):
        self.id = []
        self.meta = []
        self.data = []

        for i in range(self.dataSize):
            with open(self.path + str(i) + ".data", "rb") as file:
                f_song_id = pickle.load(file)
                f_songMeta = pickle.load(file)
                f_data = pickle.load(file)
                self.id.append(f_song_id)
                self.meta.append(f_songMeta)
                self.data.append(f_data)

        self.id = np.array(self.id)
        self.meta = np.array(self.meta)
        self.data = np.array(self.data)

    def generate_kdtree(self):
        tsne = TSNE()
        self.tsne = tsne.fit_transform(self.data)
        self.kdtree = KDTree(self.tsne, leafsize=self.leafSize)

    def query(self, data):
        return self.kdtree.query(data, self.leafSize)

data_size = 662
nnr = NNRecommendation("Dataset/", data_size, 21)
nnr.preprocess()
nnr.generate_kdtree()
for i in range(data_size):
    print("id: " + str(nnr.id[i]) + "; metadata: " + str(nnr.meta[i]) + "\nneighbours:")
    print(nnr.query(nnr.tsne[i]))