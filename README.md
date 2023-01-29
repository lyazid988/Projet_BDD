# PyBDD : Système de gestion de base de données en Python

## Introduction :

Mon projet PyBDD est un système de gestion de base de donnée que j'ai coder en Python. L'idée que j'ai eu de concevoir et coder un système de gestion BDD, est pour un principal but d'apprendre et decouvrir son fonctionnement, et ainsi, me poser des questions notamment sur comment le securisé. Ensuite, question d'avoir plus de matière en terme de sécurité, j'ai decider de mettre mon système BDD python en tant que serveur, pour pouvoir l'exploiter et manipuler mes données à travers le web (avec un client php), et donc, je me metterai en défi d'etre capable de fournir une solution client/serveur BDD fonctionnelle et sécurisée.

## Sommaire:

### I - Conception et code de PyBDD   

#### 1- Conception des méthodes et fonctions de manipulation des donnée (Presque finie)
#### 2- Cryptage des donnnées (en cours)
#### 3- Conception de la notion utilisateurs, droits et sessions (en cours)


### II - Exploitation et manipulation des données à distance (en attente)

#### 1- Création d'un serveur de base de donnée en python

#### 2- Créer des fonctions pour faciliter la connection client en php

#### 3- Tests et réflexion de sécurité


## I - Conception et code de PyBDD
La conception logicielle de PyBDD est très simple. J'ai utiliser principalement deux concepts sur Python, qui m'ont été très utiles, on a :

**La manipulation des fichiers :** avec la classe file sur python, j'ai pu generer et ecrire sur des fichiers .txt, pour hiearchiser et remplir mes bases de données.

**Le traitement du texte :** J'ai utiliser la fonction split() sur python, qui est une fonction qui permet de diviser une chaine de caractère selon l'element de division choisie (espace, virgule, point virgule, slash...etc). Cela m'as été utile pour traiter les commandes de PyBDD
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
#### 1.3- Fonction de création d'une table
```python
def createtable(cmd,db): #Fonction pour créer une table
    
    if db == '':
     print("aucune base de données n'est selectionner")
    else:
     print(db)
     print(str((cmd.split()[2].split(":"))[0]))
     file2 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/table_"+str(cmd.split()[2])+".txt", "a")
     file3 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/tables.txt", "a")
     file2.write(cmd.split()[3][1:-1]+'\n')
     file3.write(cmd.split()[2]+"\n")
```
#### 1.4- Fonction d'affichage de tables
```python
def showtables(db): #Fonction pour afficher les tables dans une base de donnée

 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/tables.txt", 'r')

 c='|   Tables de "'+db+'"   |'
 j = ""
 m ='|'
 for k in range(0,len(c)):
    j=j+"-"
    m=m+' '
 m = m[:-2]
 m=m+'|'
 print(j)
 print(c)
 print(j)
 for i in file.readlines():
    k='|'+i[0:-1]
    print(m)
    for l in range(0,len(j)-len(k)-1):
        k=k+' '
    k=k+'|'
    print(k)
    print(m)
 print(j)
```
#### 1.5- Fonction verification de table
```python
def verifie_table(db,table): #Fonction pour verifier si une table existe dans une base de donnée

 c=[]
 filer = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/tables.txt", 'r')
 for j in filer.readlines():
   c.append(j[0:-1])
 if table in c:
   return True
 else:
   return False
```
#### 1.6- Fonction d'insertion
```python
def insert(db,table,ent,val): #Fonction pour inserer des données dans une table
   
   filew = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/table_"+table+".txt", 'a')
   
   filer = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/table_"+table+".txt", 'r')
   
   c=[]

   for k in filer.readlines()[0][0:-1].split(','):

      if k.split(";")[0] in ent:

         c.append(val[ent.index(k.split(";")[0])])

      else:

         c.append('NULL')

   filew.write(c)
   filew.close()
   filer.close()

```
#### 1.7- Fonction de selection
Fonction de select *:
```python
def selectet(db,table): #Fonction pour faire un select * d'une table
 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/table_"+table+".txt", 'r')
 m=[]
 for k in file.readlines():
    m.append(k[:-1])

 o = m[0].split(',')
 c=''
 s=''
 for i in range(0,len(o)): 
    s=s+'|'+o[i].split(';')[0]
    for e in range(0,25-len(s)):
        s=s+' '
    c=c+s
    s=''
 c=c+'|'
 d=''

 for h in range(0,len(c)):
    d=d+'-'

 print(d)
 print(c)
 print(d)
 x=''
 z=''
 for y in range(1,len(m)):
  
    z=''
    for p in range(0,len(m[y].split(','))):
        x=""
        x=x+'|'+str(m[y].split(',')[p])
        for n in range(0,25-len(m[y].split(',')[p])-1):
                x=x+' '
        z=z+x
    print(z+'|')
    print(d)
```
Fonction de selection d'elements d'une table:
```python
def selectse(db,table,li): #Fonction pour selectionner que des elements dans une table

 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/databases/"+db+"/table_"+table+".txt", 'r')

 m=[]
 a=[]


 for k in file.readlines():
    m.append(k[:-1])
 jn = []
 jc = []
 tes = []
 nc = m[0].split(',')
 for f in range(0,len(nc)):
   if nc[f].split(';')[0] in li:
      jn.append(f)
      tes.append(nc[f])
   else:
      continue
 
 jc.append(','.join(tes)) 

 for b in range(1,len(m)):
   z=[]
   for s in jn:
      z.append(m[b].split(',')[s])
   jc.append(','.join(z))
 
 o = jc[0].split(',')
 c=''
 s=''
 for i in range(0,len(o)): 
    s=s+'|'+o[i].split(';')[0]
    for e in range(0,25-len(s)):
        s=s+' '
    c=c+s
    s=''
 c=c+'|'
 d=''
 for h in range(0,len(c)):
    d=d+'-'

 print(d)
 print(c)
 print(d)
 x=''
 z=''
 for y in range(1,len(jc)):
    z=''
    for p in range(0,len(jc[y].split(','))):
        x=""
        x=x+'|'+str(jc[y].split(',')[p])
        for n in range(0,25-len(jc[y].split(',')[p])-1):
                x=x+' '
        z=z+x
    print(z+'|')
    print(d)

```
#### 1.8 - Tests de fonctionnement
##### Affichage des bases de données
<img src=img1.png>
##### Selection des elements dans une table
<img src=img2.png>
