import numpy as np
import pickle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def normalize_euclidean(matrix):
    mag = np.square(matrix)
    mag = np.sum(mag, axis=1, keepdims=True)
    mag = np.sqrt(mag)
    matrix = matrix / mag
    return matrix

def cosine_similarity(transformed):
    transformed = normalize_euclidean(transformed)
   # test_transformed = normalize_euclidean(test_transformed)
   # cosine_score = transformed * test_transformed
    print("enter")
    cosine_score=np.dot(transformed,transformed.transpose())
    print("exit")
    return cosine_score

def construct_matrix():
    with open('paths.pickle', 'rb') as handle:
         urls = pickle.load(handle)
    location = "../Data/usersessions.csv"
    file = open(location, encoding="utf8")
    lines = file.readlines()
    file.close()
    matrix = np.zeros((len(lines), len(urls)))
    for i in range(0,len(lines)):
        l=lines[i].replace('"','')
        l=l.replace("\n",'')
        split=l.split(",")
        for j in range(0,len(split)):
            try:
                matrix[i][urls.index(split[j])] = len(split)-j
            except:
                print(split[j])

    return matrix

def main():
    dimensionality_reduction_algo = PCA(n_components=20)


  #  matrix = construct_matrix()

  #  with open('matrix.pickle', 'wb') as handle:
   #     pickle.dump(matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('matrix.pickle', 'rb') as handle:
         matrix = pickle.load(handle)
    print(len(matrix))
    print("enter")
    transformed = dimensionality_reduction_algo.fit_transform(matrix)
    print("exit")
    cosine_matrix = cosine_similarity(transformed)

    with open('similarity.pickle', 'wb') as handle:
        pickle.dump(cosine_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)
   # # cosine_matrix=np.matrix(cosine_matrix)
   #  print("k_means")
   #  km = KMeans(n_clusters=3, init='k-means++')
   #  eigen_values, eigen_vectors = np.linalg.eigh(cosine_matrix)
   #  km.fit(eigen_vectors[:, 2:4])
   #  print("enter")
   #  labels = km.predict(cosine_matrix)
   #  print(labels)

main()
