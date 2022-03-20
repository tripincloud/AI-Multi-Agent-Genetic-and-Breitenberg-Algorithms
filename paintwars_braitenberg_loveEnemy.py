# Projet "robotique" IA&Jeux 2021
#
# Trinome :
#  Prénom Nom: Achraf JDAY
#  Prénom Nom: Doan LE
#  Prénom Nom: Rida TALEB

def get_team_name():
    return "The great pretenders"  # à compléter (comme vous voulez)


def step(robotId, sensors):
    translation = 1  # vitesse de translation (entre -1 et +1)
    rotation = 0  # vitesse de rotation (entre -1 et +1)

    # initialisation
    enemy_detected_by_front_sensor = False
    enemy_detected_by_front_right_sensor = False
    enemy_detected_by_front_left_sensor = False
    enemy_detected_by_right_sensor = False
    enemy_detected_by_left_sensor = False
    enemy_detected_by_back_sensor = False
    enemy_detected_by_back_right_sensor = False
    enemy_detected_by_back_left_sensor = False

    ally_detected_by_front_sensor = False
    ally_detected_by_front_right_sensor = False
    ally_detected_by_front_left_sensor = False
    ally_detected_by_right_sensor = False
    ally_detected_by_left_sensor = False

    wall_detected_left = False
    wall_detected_right = False
    wall_detected_front = False
    wall_detected_front_right = False
    wall_detected_front_left = False

    # détection d'un robot de l'équipe adversaire
    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True
    if sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False:
        enemy_detected_by_front_right_sensor = True
    if sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False:
        enemy_detected_by_front_left_sensor = True
    if sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == False:
        enemy_detected_by_right_sensor = True
    if sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == False:
        enemy_detected_by_left_sensor = True
    if sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        enemy_detected_by_back_sensor = True
    if sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False:
        enemy_detected_by_back_right_sensor = True
    if sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False:
        enemy_detected_by_back_left_sensor = True

    # détection d'un robot de la même équipe
    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True:
        ally_detected_by_front_sensor = True
    if sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True:
        ally_detected_by_front_right_sensor = True
    if sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True:
        ally_detected_by_front_left_sensor = True
    if sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True:
        ally_detected_by_right_sensor = True
    if sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True:
        ally_detected_by_left_sensor = True

    # détection des murs
    if sensors["sensor_left"]["distance"] < 1 and sensors["sensor_left"]["isRobot"] == False:
        wall_detected_left = True
    if sensors["sensor_right"]["distance"] < 1 and sensors["sensor_right"]["isRobot"] == False:
        wall_detected_right = True
    if sensors["sensor_front"]["distance"] < 1 and sensors["sensor_front"]["isRobot"] == False:
        wall_detected_front = True
    if sensors["sensor_front_right"]["distance"] < 1 and sensors["sensor_front_right"]["isRobot"] == False:
        wall_detected_front_right = True
    if sensors["sensor_front_left"]["distance"] < 1 and sensors["sensor_front_left"]["isRobot"] == False:
        wall_detected_front_left = True

    # évite les alliés
    if ally_detected_by_right_sensor:
        rotation = -0.5
    elif ally_detected_by_left_sensor or ally_detected_by_front_sensor:
        rotation = 0.5
    elif ally_detected_by_front_right_sensor:
        rotation = -0.5
    elif ally_detected_by_front_left_sensor:
        rotation = 0.5

    # suivre les ennemis
    elif enemy_detected_by_front_sensor:
        rotation = 0
    elif enemy_detected_by_front_right_sensor:
        rotation = 0.25
    elif enemy_detected_by_front_left_sensor:
        rotation = -0.25
    elif enemy_detected_by_right_sensor:
        rotation = 0.5
    elif enemy_detected_by_left_sensor:
        rotation = -0.5
    elif enemy_detected_by_back_sensor:
        rotation = 1
    elif enemy_detected_by_back_right_sensor:
        rotation = 0.75
    elif enemy_detected_by_back_left_sensor:
        rotation = -0.75

    # évite les murs
    elif (wall_detected_front and wall_detected_front_right) or (wall_detected_right and wall_detected_front_right):
        rotation = -0.5
    elif (wall_detected_front and wall_detected_front_left) or (wall_detected_left and wall_detected_front_left):
        rotation = 0.5
    elif wall_detected_right or wall_detected_front_right:
        rotation = -0.25
    elif wall_detected_left or wall_detected_front_left or wall_detected_front:
        rotation = 0.25

    return translation, rotation
