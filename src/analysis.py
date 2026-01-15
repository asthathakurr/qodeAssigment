from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

class Analyzer:
    def vectorize(self, df):
        tfidf = TfidfVectorizer(max_features=500)
        X = tfidf.fit_transform(df['content']).toarray()
        return X

    def plot_sample(self, X, sample=200):
        X_small = X[:sample]
        pca = PCA(n_components=2)
        pts = pca.fit_transform(X_small)
        os.makedirs('output', exist_ok=True)
        plt.scatter(pts[:,0], pts[:,1])
        plt.title("Tweet Signal Scatter Plot (sample)")
        plt.savefig("output/signal_plot.png")
