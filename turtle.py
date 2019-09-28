# DOIT ETRE UTILISER DANS LE MEME DOSSIER QUE LE FICHIER TURTLE DU HOME DE THOR !

from re import findall

src = open("./turtle", "r")
dst = open("result.py", "w+b")
x = 0
y = 350
if not src or not dst:
	exit()
dst.write("from turtle import *\n")
dst.write("penup("")\n")
dst.write("begin_fill()\n")
dst.write("speed(0)\n")
dst.write("sety(" + str(y) + ")\n")
dst.write("setx(" + str(0) + ")\n")
dst.write("seth(" + str(0) + ")\n")		
dst.write("pendown("")\n")
bite = src.readline()
while (bite):
	if "Avance" in bite:
		dst.write("forward(" + findall("\d+", bite)[0] + ")\n")
	elif "Recule" in bite:
		dst.write("backward(" + findall("\d+", bite)[0] + ")\n")
	elif "Tourne" in bite:
		if "droite" in bite:
			dst.write("right(" + findall("\d+", bite)[0] + ")\n")
		elif "gauche" in bite:
			dst.write("left(" + findall("\d+", bite)[0] + ")\n")
	elif not bite.strip():
		y -= 100
		dst.write("penup("")\n")
		dst.write("sety(" + str(y) + ")\n")
		dst.write("setx(" + str(0) + ")\n")
		dst.write("seth(" + str(0) + ")\n")
		dst.write("pendown("")\n")
	else:
		print("Syntax error in: " + bite)
	bite = src.readline()
  
dst.write("done()\n")
src.close()
dst.close()
