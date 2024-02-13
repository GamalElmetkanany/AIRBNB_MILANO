from os import path
from sys import argv

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib.pyplot import xlabel,ylabel,plot,show,title


def k_cluster(dataframe,k,max):
    """
    Crea i cluster utilizzando l'algoritmo K-Means.

    :param dataframe: Dataframe con le features da utilizzare per il clustering.
    :type dataframe: pd.DataFrame
    :param k: Numero di cluster.
    :type k: int
    :param max_it: Numero massimo di iterazioni.
    :type max_it: int
    :return: Etichette dei cluster assegnate a ciascuna riga del dataframe.
    :rtype: array
    """
    print("Creazione clusters...")

    km = KMeans(n_clusters=k, max_iter=max, n_init=10)
    km.fit(dataframe)
    clusters = km.fit_predict(dataframe)
    return clusters

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.pyplot import title, xlabel, ylabel, plot, show

def elbow_plot(dataframe, max_iter):
    """
    Genera un grafico dell'elbow per aiutare a determinare il numero ideale di cluster.

    :param dataframe: Il dataframe contenente le features per il clustering.
    :type dataframe: pd.DataFrame
    :param max_iter: Il numero massimo di iterazioni per ogni esecuzione di K-Means.
    :type max_iter: int
    """
    sum_of_squared_errors = []

    # Range da 1 al massimo numero di cluster
    num_clusters_range = range(1, max_iter + 1)

    for num_clusters in num_clusters_range:
        kmeans = KMeans(n_clusters=num_clusters, max_iter=max_iter, n_init=10)
        kmeans.fit(dataframe)
        sum_of_squared_errors.append(kmeans.inertia_)

    # Plot dell'elbow
    plt.figure(figsize=(10, 6))
    plt.plot(num_clusters_range, sum_of_squared_errors, marker='o', linestyle='-', color='b')
    plt.title("Elbow Method for Optimal Cluster Number")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Sum of Squared Error (SSE)")
    plt.xticks(num_clusters_range)
    plt.grid(True)
    plt.show()

def main():
    try:
        dataframe = pd.read_csv(argv[1])
        k = int(argv[2])  # number of cluster
        it = int(argv[3]) # number of iterations
        cluster_centroids = k_cluster(dataframe, k, it)
        df_prolog = pd.read_csv('./datasets/prolog_dataframe.csv')
        df_prolog['cluster'] = cluster_centroids
        df_prolog.to_csv('./datasets/prolog_dataframe.csv',index = False)
        #elbow_plot(dataframe,it)
        print("Clustering eseguito.")

    except FileNotFoundError as e:
        print("File not found",e)
    except Exception as e:
        print(e)


main()