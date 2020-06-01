import matplotlib.pyplot as plt
import pandas as pd
from os.path import join as osjoin

if __name__ == "__main__":
    # Les chemins entre les fichiers étant differents sous Windows et MacOS/Linux nous devons utiliser
    # os.path.join (ici renommé osjoin) pour naviguer entre les dossiers

    path_df = osjoin(osjoin("data", "process"), "toy_dataset.csv")
    df = pd.read_csv(path_df)

    plt.hist(df["monthly"])

    path_fig = osjoin(osjoin("rapport", "image"), "hist.png")
    plt.savefig(path_fig)
