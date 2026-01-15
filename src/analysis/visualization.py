import pandas as pd
import matplotlib.pyplot as plt


def plot_signals(csv_path):
    df = pd.read_csv(csv_path)
    sample = df.sample(frac=0.1)

    plt.plot(sample["signal_strength"])
    plt.title("Sample Trading Signal Strength")
    plt.xlabel("Sample Index")
    plt.ylabel("Signal Strength")
    plt.show()
