from src.monthly_income import get_monthly_income
import pandas as pd
from os.path import join as osjoin
import os

if __name__ == "__main__":
    # Les chemins entre les fichiers étant differents sous Windows et MacOS/Linux nous devons utiliser
    # os.path.join (ici renommé osjoin) pour naviguer entre les dossiers
    path_source = osjoin(osjoin("data", "raw"), "toy_dataset.csv")
    path_result = osjoin(osjoin("data", "process"), "toy_dataset.csv")
    # Si data/process n'existe pas on le créé
    if not os.path.exists(osjoin("data", "process")):
        os.makedirs(osjoin("data", "process"))

    # Lecture et traitement des données
    df = pd.read_csv(path_source)
    get_monthly_income(df)
    df.to_csv(path_result)