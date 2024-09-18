import numpy as np
from scipy import sparse as sp

from rlscore.utilities import multiclass

def load_newsgroups():
    T = np.loadtxt("train.data")
    #map indices from 1...n to 0...n-1
    rows = T[:,0] -1
    rows = rows.astype(int)
    cols = T[:,1] -1
    cols = cols.astype(int)
    vals = T[:,2]
    vals = vals.astype(int)
    X_train = sp.coo_matrix((vals, (rows, cols)))
    X_train = X_train.tocsc()
    T = np.loadtxt("test.data")
    #map indices from 1...n to 0...n-1
    rows = T[:,0] -1
    rows = rows.astype(int)
    cols = T[:,1] -1
    cols = cols.astype(int)
    vals = T[:,2]
    vals = vals.astype(int)
    X_test = sp.coo_matrix((vals, (rows, cols)))
    X_test = X_test.tocsc()
    #X_test has additional features not present in X_train
    X_test = X_test[:,:X_train.shape[1]]
    Y_train = np.loadtxt("train.label", dtype=int)
    Y_train = multiclass.to_one_vs_all(Y_train, False)
    Y_test = np.loadtxt("test.label", dtype=int)
    Y_test = multiclass.to_one_vs_all(Y_test, False)
    return X_train, Y_train, X_test, Y_test

def print_stats():
    X_train, Y_train, X_test, Y_test = load_newsgroups()
    print("Train X dimensions %d %d" %X_train.shape)
    print("Test X dimensions %d %d" %X_test.shape)
    print("Number of labels %d" %Y_train.shape[1])
    

if __name__=="__main__":
    print_stats()
