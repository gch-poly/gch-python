import json
import numpy as np
import pickle  # Librairie pour sauvegarder des objets Python
import matplotlib.pyplot as plt


def get_json_data(path):
    """
    Fonction qui ouvre les fichiers json et renvoie le contenu sous forme d'un dictionnaire
    Args:
        - path: Emplacement du fichier json
    Returns:
        - Données sous forme de dictionnaire
    """
    # Lire le fichier JSON
    with open(path, "r") as u:
        raw_data = json.load(u)

    # Transforme les dates en objet datetime (utile pour les graphiques)
    raw_data["date"] = np.array(raw_data["date"], dtype="datetime64[s]")

    return raw_data


def temp_save_graph(axs, temp, msg):
    """
    Fonction qui sauvegarde un état dans la constuction d'un graphique
    Args:
        axs: objet qui contient les axes du graphique
        temp: liste qui contient les différents états du graphique
        msg: description de l'état
    """
    state = {"pickle": pickle.dumps(axs), "msg": msg}
    temp.append(state)


def temp_show_graphs(temp):
    """
    Fonction qui affiche les graphiques enregistrés avec la fonction temp_save_graph
    Args:
        temp: liste qui contient les différents états du graphique
    """
    global axs
    for t in temp:
        print(t["msg"])
        axs = pickle.loads(t["pickle"])
        plt.show()


def get_vortex_data(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data
