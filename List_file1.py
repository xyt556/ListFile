import os
import xlsxwriter

### FONCTION QUI PARCOURS TOUS LES DOSSIERS D'UN REPERTOIRE ET QUI ECRIT DANS UNE SHEET EXCEL
def routine(pth, ws, row):
	for path, dirs, files in os.walk(pth):
		for filename in files:
			ws.write(row, 0, path)
			ws.write(row, 1, filename)
			ws.write_url(row, 2, path+"\\"+filename)
			row=row+1
	return row


###### TENTATIVE DE SUPPRESSION DE L'ANCIEN RESULTAT #########
try :
	os.remove('result.xlsx')
###### ERREUR DE PERMISSION PROVOQUER MAJORITAIREMENT PAR LA NON-FERMETURE DU FICHIER result.xlsx, DANS CE CAS ON QUITTE LE PROGRAMME ######
except PermissionError :
	print("Une erreure est survenue !\n\nÊtes-vous sûr d'avoir fermé correctement le fichier result.xlsx avant d'éxectuer le programme ?")
	exit()
###### FICHIER IMPOSSIBLE A SUPRRIMER CAR INEXISTANT : CELA N'EST PAS UN PROBLEME POUR LA SUITE, ON IGNORE/PASS L'ERREUR
except FileNotFoundError :
	pass

### ON CREE LE FICHIER EXCEL DANS LE REPERTOIRE COURANT
wb = xlsxwriter.Workbook('result.xlsx')
### ON CREE UNE SHEET sheet1
ws = wb.add_worksheet('sheet1')
### INITIALISATION DES LIGNES
row = 0

### ROUTINE 1
root1='D:' 	### /!\ NE PAS OUBLIER DE METTRE 2 ANTISLASH POUR QUE PYTHON INTERPETRE UN SEUL ANTISLASH DANS LE PATH
row=routine(root1, ws, row)
root2='D:'	### /!\ NE PAS OUBLIER DE METTRE 2 ANTISLASH POUR QUE PYTHON INTERPETRE UN SEUL ANTISLASH DANS LE PATH
row=routine(root2, ws, row)

### APRES OPERATION ON FERME LE FICHIER EXCEL
wb.close()

### AFFICHAGE DU RESULTAT DE FIN DE PROGRAMME
print("\nLes résultats sont affichés dans result.xlsx dans "+os.getcwd())
print("\n --> Column A : Path")
print(" --> Column B : Filename")
print(" --> Column C : Path et filename en hyperlien \n")
print("Jobs done ! Enjoy :) ")

#eats-b503nq