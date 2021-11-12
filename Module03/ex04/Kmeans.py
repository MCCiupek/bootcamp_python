import numpy as np
import matplotlib.pyplot as plt

debug = True


def L1(x, y):
    """
    Compute L1 distance between 2 points
    """
    return np.sum(np.abs(y - x), axis=1)

def distortion(X, Y):
    """
    Compute distortion score
    """
    return -np.sum(np.abs(X - Y) ** 2)

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        assert isinstance(max_iter, int) and max_iter > 0, "Error: max_iter"
        assert isinstance(ncentroid, int) and ncentroid > 0, "Error: ncentroid"
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def compute_distance(self, X, func):
        res = np.zeros((X.shape[0], self.centroids.shape[0]))
        for i in range(0, self.ncentroid):
            res[:, i] = func(X, self.centroids[i])
        return res

    def evaluate_prediction(self, X, y, func):
        Y = self.centroids.take(y, axis=0).reshape(X.shape)
        return func(X, Y)
    
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        score = []
        idx = []

        for i in range(0, self.max_iter):
            idx.append(np.random.choice(X.shape[0], self.ncentroid, replace=False))
            self.centroids = X[idx[i],:]
            score.append(self.evaluate_prediction(X, self.predict(X), distortion))

        self.centroids = X[idx[np.argmax(score)],:]
        return

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        dist = self.compute_distance(X, L1)
        return np.argmin(dist, axis=1).reshape((X.shape[0], 1))


def plot_res_3d(X, y, header, km):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(0, km.ncentroid):
        ax.scatter(X[np.where(y==i),0], X[np.where(y==i),1], X[np.where(y==i),2])
    
    for i in range(0, km.ncentroid):
        plt.scatter(km.centroids[i,0], km.centroids[i,1], km.centroids[i,2])

    ax.set_xlabel(header[1])
    ax.set_ylabel(header[2])
    ax.set_zlabel(header[3])

    plt.show()

def plot_res_2d(X, Y, header, km, ax, x=0, y=1):

    colors = ['r', 'b', 'g', 'y']

    for i in range(0, km.ncentroid):
        ax.scatter(X[np.where(Y==i),x], X[np.where(Y==i),y], color=colors[i], alpha=0.5)
    
    for i in range(0, km.ncentroid):
        ax.scatter(km.centroids[i,x], km.centroids[i,y], marker='o', s=50, color=colors[i])

    ax.set(xlabel=header[x], ylabel=header[y])


def main(**kwargs):

    try:
        max_iter = int(kwargs['max_iter'])
        ncentroid = int(kwargs['ncentroid'])
        filepath = str(kwargs['filepath'])
    except KeyError:
        return
    except ValueError:
        return

    with CsvReader(filepath, header=True) as myfile:
        data = myfile.getdata()
        header = myfile.getheader()

    X = np.delete(np.array(data).astype(float), 0, 1)
    
    km = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)

    km.fit(X)
    y = km.predict(X)

    plot_res_3d(X, y, header, km)

    fig, axs = plt.subplots(1, 3)

    plot_res_2d(X, y, header[1:], km, axs[0], 0, 1)
    plot_res_2d(X, y, header[1:], km, axs[1], 0, 2)
    plot_res_2d(X, y, header[1:], km, axs[2], 1, 2)

    plt.show()

if __name__=="__main__":

    from csvreader import CsvReader
    import sys

    kwargs = dict(arg.split('=') for arg in sys.argv[1:])
    main(**kwargs)