import os

def conv(): #Fonction qui convertie les données dans le fichier test.txt (qui contient le nom des bases de données crées), en liste, pour pouvoir les utiliser dans la fonction d'affichage des bases de données

    file1 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/test.txt", "r")
    Lines = file1.readlines()
    liste = []
    for line in Lines:
      liste.append(line.strip())
    file1.close()
    return liste


def createdb(nom): #Fonction pour créer une base de donnée

    os.system("mkdir /home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+nom)

    file1 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+nom+"/tables.txt", "a")
    file1.close()

    file2 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/test.txt", "a")

    file2.write(nom+'\n')

    file2.close()

    print('La base de donnée '+nom+' à été créer avec succès.')

def printdb(): #Fonction pour afficher les base de données
 mydb = conv()
 print("---------------------------")
 print("|   Mes bases de données  |")
 print("---------------------------")
 for i in range(0,len(mydb)):
    s = ""
    for j in range(0,25-len(mydb[i])):
      s = s+" "
    print("|                         |")
    print("|"+mydb[i]+s+"|")
 print("|                         |")  
 print("---------------------------")

def createtable(cmd,db): #Fonction pour créer une table
    if db == '':
     print("aucune base de données n'est selectionner")
    else:
     print(db)
     print(str((cmd.split()[2].split(":"))[0]))
     file2 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/table_"+str(cmd.split()[2])+".txt", "a")
     file3 = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/tables.txt", "a")
     file2.write(cmd.split()[3][1:-1]+'\n')
     file3.write(cmd.split()[2]+"\n")

def verifie_table(db,table): #Fonction pour verifier si une table existe dans une base de donnée

 c=[]
 filer = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/tables.txt", 'r')
 for j in filer.readlines():
   c.append(j[0:-1])
 if table in c:
   return True
 else:
   return False

def insert(db,table,ent,val): #Fonction pour inserer des données dans une table
   
   filew = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/table_"+table+".txt", 'a')
   
   filer = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/table_"+table+".txt", 'r')
   
   c=[]

   for k in filer.readlines()[0][0:-1].split(','):

      if k.split(";")[0] in ent:

         c.append(val[ent.index(k.split(";")[0])])

      else:

         c.append('NULL')

   filew.write(c)
   filew.close()
   filer.close()


def selectet(db,table): #Fonction pour faire un select * d'une table
 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/table_"+table+".txt", 'r')
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

def selectse(db,table,li): #Fonction pour selectionner que des elements dans une table

 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/table_"+table+".txt", 'r')

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


def showtables(db): #Fonction pour afficher les tables dans une base de donnée

 file = open("/home/r00ted/Desktop/Projets_Python/Base_de_donnée/Projet_BDD/databases/"+db+"/tables.txt", 'r')

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
    
def printddb():
    print('----------------------------------------------------------------------------')
    print("|                                                                          |")
    print("|                                  PyBDD                                   |")
    print("|                                                                          |")
    print("|                               version 1.0                                |")
    print("|                                                                          |")
    print("|                 Projet BDD : Campus YNOV B3 Cybersécurité                |")
    print("|                                                                          |")
    print("|                         By : Lyazid aka r00ted                           |")
    print("|                                                                          |")
    print('----------------------------------------------------------------------------')

sessdb=''
sess=''

printddb()
while(True):
    cmd=str(input('PyBDD > '+sessdb))

    if cmd =='':
        continue
    elif cmd in ('affiche les databases','affiche les db','show db','show databases'):
        printdb()

    elif cmd.split()[0] in ('utilise','use'):
        cmdt = cmd.split()
        sessdb = cmdt[1]+" > "
        sess=cmdt[1]
    
        if cmdt[1] in conv():
            print("Vous utilisez maintenant la base de donnée '"+cmdt[1]+"'")
        else:
            print("La base de donnée que vous avez preciser n'existe pas")

    elif ' '.join(cmd.split()[0:2]) in ('crée ba','crée db','create database','create db'):
        createdb(cmd.split()[2])

    elif cmd.split()[0] in ('create','crée'):
          if sess == '':
            print("Aucune base de donnée n'est selectionnée")
          else:
            createtable(cmd,sess)

    elif cmd[0:6] == "insert":
        print('Fonctionnalité pas encore disponible')


    elif cmd in ("affiche les tables","show tables","show tb"):
         if sess == '':
            print("Aucune base de donnée n'est selectionnée")
         else:
            showtables(sess)

    elif cmd.split()[0] == 'selectionne':
         if len(cmd.split()) == 4:
          if cmd.split()[0] == "selectionne" and cmd.split()[2] == 'de':
            if verifie_table(sess, cmd.split()[3]):
                if cmd.split()[1] == "*":
                    selectet(sess, cmd.split()[3])
                elif len(cmd.split()[1].split(',')) > 1:
                    selectse(sess, cmd.split()[3], cmd.split()[1].split(','))
                else:

                    selectse(sess, cmd.split()[3], [cmd.split()[1]])

            else:

                print("La table '"+cmd.split()[3]+"' n'existe pas")

          else:

            print('Erreur dans votre commande')

         elif len(cmd.split()) > 4:

            print("en cours de developpement")

         else:

            print("Commande incomplete")

    elif cmd=='help':
        print('')
        print('Commandes : ')
        print('')
        print("- 'affiche les databases', 'affiche les db', 'show db' : permet d'afficher les bases de données")
        print('')
        print("- 'crée database madatabase', 'create database madatabase' : permet de créer une base de données")
        print('')
    elif cmd == 'exit':
        print("A la prochaine bg ;)")
        break

    elif cmd=='clear':
        os.system("clear")
        printddb()

    else:
        print('Erreur dans la commande')