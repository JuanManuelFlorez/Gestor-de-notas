#encoding: utf-8
import os

def ajuda():
  print "Metode d'ús: [notes]: [opció] [arguments]\n\n"
  print "Las opciones son:"
  print "m\t\t\t\tMostra les notes."
  print "n «nom_antic» «nom_nou»\t\tCanvia el nom del primer alumne amb 'nom_nou'."
  print "c «nom» «eval» «n»\t\tCanvia la nota de la posició p per n."
  print "a\t\t\t\tAfegeix una nova nota al final de la llista."
  print "r\t\t\t\tRecuperar datos "
  print "d\t\t\t\tGuardar dadtos"
  print "o [alumnes|1|2|3] [ASC/DESC]\tOrdena les llistes segons les opcions"
  print "b\t\t\t\tBuida les notes de la llista."
  print "t\t\t\t\tAprova a tothom segons l'exercici de llistes."
  print "?\t\t\t\tMostra una ajuda amb un resum de les comandes disponibles."
  print "x\t\t\t\tFinalitza l'execució"

def error_de_opcion(op):
  print "Opció invàlida -- '%s'" %(op)
  print "Proba la opció '?' per més informació."

def error_de_validacion():
  try:
    n1 = float(raw_input("T1: "))
    n2 = float(raw_input("T2: "))
    n3 = float(raw_input("T3: "))
    fail = False
    return fail,n1,n2,n3
  except ValueError:
    fail = True
    return fail,0,0,0

def error_de_nombre():
  try:
    na = raw_input("Nom: ")
    pos = alumnes.index(na)
    fail = False
    return fail,pos
  except ValueError:
    fail = True
    return fail,0

def error_de_rango(n1,n2,n3):
  if (n1>=0 and n1<=10) and (n2>=0 and n2<=10) and (n3>=0 and n3<=10):
    return False
  else:
    return True

def fun_ordena(op,op1):
  if op == '1':
    zipped = zip(t1, t2, t3, alumnes)
  elif op == '2':
    zipped = zip(t2, t1, t3, alumnes)
  elif op == '3':
    zipped = zip(t3, t2, t1, alumnes)
  elif op == "alumnes":
    zipped = zip(alumnes, t1, t2, t3)
  
  if op1 in ("ASC","asc"):
    zipped.sort()
  elif op1 in ("DESC","desc"):
    zipped.sort(reverse = True)
    
  return zipped

def ordena():
  global t1, t2, t3, alumnes
  
  op = raw_input("Opcio: ")
  aod = raw_input("ASC/DESC:")
  if op in ('1','2','3',"alumnes") and aod in ("asc","ASC","desc","DESC"):
    pack = fun_ordena(op,aod)
    if op == '1':
      f1, f2, f3, alumnes2 = zip(*pack)
    elif op == '2':
      f2, f1, f3, alumnes2 = zip(*pack)
    elif op == '3':
      f3, f2, f1, alumnes2 = zip(*pack)
    elif op == 'alumnes':
      alumnes2, f1, f2, f3 = zip(*pack)
    t1 = list(f1)
    t2 = list(f2)
    t3 = list(f3)
    alumnes = list(alumnes2)
  else:
    os.system("clear")
    print "Error! Opcions incorrectes!"

def buida():
  for i in range(len(alumnes)):
    alumnes.pop(0)
    t1.pop(0)
    t2.pop(0)
    t3.pop(0)

def afegeix():
  nom = raw_input("Nom: ")
  fail,n1,n2,n3 = error_de_validacion()
  os.system("clear")
  if fail == True:
      print "Error! Tipus de dade no vàlida!"
  else:
    if error_de_rango(n1,n2,n3) == False:
      alumnes.append(nom)
      t1.append(n1)
      t2.append(n2)
      t3.append(n3)
      os.system("clear")
    else:
      print "La nota no es vàlida!"

def guardar():
		arxiu = raw_input("Escriu el nom del arxiu:")
		fitxer = open(arxiu+".txt", "w")
		for i in range (len(alumnes)):
			fitxer.write("\n"+alumnes[i] +","+`t1[i]` +","+  `t2[i]` +","+ `t3[i]`)
		print "Notas guardas"

def recuperar():	
	global alumnes
	global t1
	global t2
	global t3
	ver = True
	while ver:
		arxiu = raw_input("Escriu el nom del arxiu:")
		try:
			fitxer = open(arxiu+".txt", "r")
			ver = False
		except:
			print "El archivo no existe"
		
	linea = fitxer.readline()
	while linea!="":
		alumnes.append(linea.split(",")[0])
		t1.append(int(float(linea.split(",")[1])))
		t2.append(int(float(linea.split(",")[2])))
		t3.append(int(float(linea.split(",")[3])))
		linea = fitxer.readline()


def mostra():
  if len(alumnes)!=0:
    print "\nalumnes\t\t\t1ra\t2na\t3ra\tfinal"
    print "-----------------------------------------------------"
    for i in range(len(alumnes)):
      if len(alumnes[i])>20:
        print "%s\t%i\t%i\t%i\t%0.1f" %(alumnes[i],t1[i],t2[i],t3[i],(t1[i]+t2[i]+t3[i])/3)
      elif len(alumnes[i])>13:
        print "%s\t\t%i\t%i\t%i\t%0.1f" %(alumnes[i],t1[i],t2[i],t3[i],(t1[i]+t2[i]+t3[i])/3)
      else:
        print "%s\t\t\t%i\t%i\t%i\t%0.1f" %(alumnes[i],t1[i],t2[i],t3[i],(t1[i]+t2[i]+t3[i])/3)
  else:
    print "Cap nota!"

def aprova():
  for i in range(len(alumnes)):
    if (t1[i]+t2[i]+t3[i])/3 < 5:
      if t1[i] < 5:
        t1[i] = 5
      if t2[i] < 5:
        t2[i] = 5
      if t3[i] < 5:
        t3[i] = 5

def nom_nou():
  fail,pos = error_de_nombre()
  
  if fail == True:
    print "No s'ha trobat aquest nom!"
  else:
    nn = raw_input("Nom nou: ")
    alumnes[pos] = nn
    os.system("clear")

def canvia():
  fail,pos = error_de_nombre()
  
  if fail == True:
    os.system("clear")
    print "No s'ha trobat aquest nom!"
  else:
    aval = int(raw_input("Avaluació: "))
    if aval not in (1,2,3):
      os.system("clear")
      print "Avaluació incorrecte!"
    else:
      nota = float(raw_input("Nota: "))
      if error_de_rango(nota,0,0) == False:
        if aval == 1:
          t1[pos]=nota
        elif aval == 2:
          t2[pos]=nota
        else:
          t3[pos]=nota
        os.system("clear")
      else:
        os.system("clear")
        print "Nota incorrecte!"

def menu(op):
  if op == 'm':
    os.system("clear")
    mostra()
  elif op == 'c':
    os.system("clear")
    canvia()
  elif op == 'a':
    os.system("clear")
    afegeix()
  elif op == 'n':
    os.system("clear")
    nom_nou()
  elif op == 'b':
    os.system("clear")
    buida()
  elif op == 't':
    os.system("clear")
    aprova()
  elif op == 'o':
    os.system("clear")
    ordena()
  elif op == '?':
    os.system("clear")
    ajuda()
  elif op == 'd':
	  os.system("clear")
	  guardar()
  elif op=='r':
	  os.system("clear")
	  recuperar()
  elif op == 'x':
    os.system("clear")
    quit()
  else:
    os.system("clear")
    error_de_opcion(op)

def programa():
  print "\n[notes]:",
  opcio = raw_input()
  print ""
  menu(opcio)

alumnes = []
t1 = []
t2 = []
t3 = []
os.system("clear")

while True:
  programa()
