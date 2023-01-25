# PyBDD : Système de gestion de base de données en Python

## Introduction :

Mon projet PyBDD est un système de gestion de base de donnée que j'ai coder en Python. L'idée que j'ai eu de concevoir et coder un système de gestion BDD, est pour un principal but d'apprendre et decouvrir son fonctionnement, et ainsi, me poser des questions notamment sur comment le securisé. Ensuite, question d'avoir plus de matière en terme de sécurité, j'ai decider de mettre mon système BDD python en tant que serveur, pour pouvoir y acceder à travers le web (avec un client php), et donc, je me metterai en défi d'etre capable de fournir une solution client/serveur fonctionnelle et sécurisée pour pouvoir exploiter et manipuler mes données à distance.

## Sommaire:

### I - Conception et code de PyBDD   

#### 1- Conception des méthodes et fonctions de manipulation des donnée (Fonctionnelle)

##### 1.1- Fonction de création d'une base de donnée
##### 1.2- Fonction d'affichage des bases de données
##### 1.3- Fonction de création d'une table

##### 1.4- Fonction d'affichage de tables

##### 1.5- Fonction verification de table
##### 1.6- Fonction d'insertion
##### 1.7- Fonction de selection

#### 2- Conception de la notion utilisateurs, droits et sessions (en cours):

### II - Exploitation et manipulation des données à distance (en cours):

#### 1- Création d'un serveur de base de donnée en python

#### 2- Créer des fonctions pour faciliter la connection client en php

#### 3- Tests et réflexion de sécurité


## I - Conception et code de PyBDD

### 1- Conception des méthodes et fonctions de manipulation des donnée (Fonctionnelle)
#### 1.1- Fonction de création d'une base de donnée
```python
def createdb(nom): #Fonction pour créer une base de donnée

    os.system("mkdir /home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+nom)

    file1 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+nom+"/tables.txt", "a")
    file1.close()

    file2 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/test.txt", "a")

    file2.write(nom+'\n')

    file2.close()

    print('La base de donnée '+nom+' à été créer avec succès.')
```
#### 1.2- Fonction d'affichage des bases de données

```python
def printdb(): #Fonction pour afficher les base de données
 file1 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/test.txt", "r")
 Lines = file1.readlines()
 liste = []
 for line in Lines:
      liste.append(line.strip())
 file1.close()
 print("---------------------------")
 print("|   Mes bases de données  |")
 print("---------------------------")
 for i in range(0,len(liste)):
    s = ""
    for j in range(0,25-len(liste[i])):
      s = s+" "
    print("|                         |")
    print("|"+liste[i]+s+"|")
 print("|                         |")  
 print("---------------------------")
```

