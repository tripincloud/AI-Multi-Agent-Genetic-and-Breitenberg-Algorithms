# Projet "robotique" IA&Jeux 2021
#
# Trinome :
#  Prénom Nom: Achraf JDAY
#  Prénom Nom: Doan LE
#  Prénom Nom: Rida TALEB

def get_team_name():
    return "The great pretenders"  # à compléter (comme vous voulez)


import random
import math

score_actuel = []
param = []

parametres = []
historique_comportements = []

numero_evaluation = []

for i in range(0, 8):
    param.append([])
    score_actuel.append(0)
    numero_evaluation.append(0)

    for j in range(0, 8):
        param[i].append(random.randint(-1, 1))

meilleur_score = 0

def step(robotId, sensors, score):
    global param, score_actuel, parametres, historique_comportements, numero_evaluation, meilleur_score

    robotId = int(robotId)
    liste = []

    data = "data_genetic_4.txt"

    fichier = open(data, 'a+')
    t = open(data)

    for ligne in t:
        l = ligne.strip()
        l = l.split(";")
        liste.append(l)

    t.close()

    if liste and numero_evaluation[robotId] == 0:
        for j in liste:
            if int(j[0]) == robotId:
                param[robotId] = list(map(int, j[2:][0].split()))
                meilleur_score = int(j[1])

    # print(parametres)

    meilleur = []

    for i in range(0, 8):
        meilleur.append(False)

    if score > score_actuel[robotId] and score > meilleur_score:
        meilleur[robotId] = True
        score_actuel[robotId] = score

    if numero_evaluation[robotId] % 3 == 0:
        indice_au_hasard = random.randint(0, 7)
        param[robotId][indice_au_hasard] = random.randint(-1, 1)

    if meilleur[robotId]:
        parametres = param[robotId]
        historique_comportements.append((robotId, score_actuel[robotId], parametres))
        meilleur[robotId] = False

        fichier.write("{};{};".format(robotId, score_actuel[robotId]))
        for p in parametres:
            fichier.write("{} ".format(parametres[p]))
        fichier.write("\n")

    numero_evaluation[robotId] += 1

    # fonction de contrôle (qui dépend des entrées sensorielles, et des paramètres)
    translation = math.tanh(
        param[robotId][0] + param[robotId][1] * sensors["sensor_front_left"]["distance"] + param[robotId][2]
        * sensors["sensor_front"]["distance"] + param[robotId][3] * sensors["sensor_front_right"]["distance"]);
    rotation = math.tanh(
        param[robotId][4] + param[robotId][5] * sensors["sensor_front_left"]["distance"] + param[robotId][6]
        * sensors["sensor_front"]["distance"] + param[robotId][7] * sensors["sensor_front_right"]["distance"]);

    fichier.close()

    return translation, rotation
