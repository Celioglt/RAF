from tkinter import *
from tkinter import filedialog
import os
from tkinter import scrolledtext
import re

window = Tk()
CheminDossier='/'

def RechercheDossier():
    global CheminDossier
    CheminDossier = filedialog.askdirectory(title='Selectionnez le dossier')
    start_button.pack(pady=20, fill=X)
    return

def RechercheMot():
    dir_list = os.listdir(CheminDossier)
    liste_mots=entree_texte.get()
    liste_mots = liste_mots.split()
    for num_mot in range (len(liste_mots)):
        mot = liste_mots[num_mot]
        liste_mots[num_mot] = mot.lower()
    
    #Création d'une liste vide de la taille 
    sorted_list = []
    for k in range (len(dir_list)):
        sorted_list.append("")

    #Tri parcour
    for k in dir_list:
        nugget = k.split('. ')
        sorted_list[int(nugget[0])-1] = k

    #lecture
    #num_txt=0
    tab_vals=[]
    for adresse in sorted_list:
        texte = open(CheminDossier + "/" + adresse, "r", encoding='utf-8', errors='ignore')
        tab_txt = texte.readlines()
        
        #num_mot = 0
        sous_tab = []
        for mot_cherche in liste_mots:
            compteur = 0
            for lignes in tab_txt:
                ligne_separee = lignes.split()
                for mot in ligne_separee:       #on nettoie chaque mot pour l'analyser (on garde uniquement les lettres)
                    mot_test = mot.lower()
                    mot_test = re.sub(r'[^a-z]', '', mot_test)
                    if mot_test == mot_cherche:      #mot_cherche = liste_mots[mot_cherche]
                        compteur += 1
            #print(num_mot)
            sous_tab.append(compteur)
            #num_mot += 1
        tab_vals.append(sous_tab)
        #num_txt += 1
        texte.close


    #Ecriture
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Fichier texte','.txt')])
    #file = open(chemin, "w+")
    num_jour=0
    file.write("jour")
    for mot in liste_mots:
        file.write(" " + mot)
    file.write("\n")
    for jour in sorted_list:
        copie_jour = jour.split()
        copie_jour.pop(0)
        copie_jour = " ".join(copie_jour)
        copie_jour = copie_jour[0:len(copie_jour)-4]

        file.write(copie_jour)
        for num_mot in range (len(liste_mots)):
            file.write(":" + str(tab_vals[num_jour][num_mot]))
        file.write("\n")
        num_jour += 1
    file.write("Total des mots:\n")
    for num_mot in range (len(liste_mots)):
        total_mots = 0
        for num_jour in range (len(sorted_list)):
            total_mots += tab_vals[num_jour][num_mot]
        file.write("le mot " + liste_mots[num_mot] + " apparaît " + str(total_mots) + " fois\n")

    file.close
    return


#Paramètres fenêtre
window.title("Augustin.exe")
window.geometry("1080x720")
window.minsize(600, 560)
window.config(background='#41B77F')

#Création de la frame
frame = Frame(window, bg='#41B77F')

#contenu
label_title = Label(frame, text="Moteur de recherche Augustin", font=("Courrier", 30), bg='#41B77F', fg='white')
label_title.pack()

label_subtitle = Label(frame, text="Entrez le texte à chercher", font=("Courrier", 20), bg='#41B77F', fg='white')
label_subtitle.pack(fill=X)

entree_texte = Entry(frame, font=("Courrier", 20), bg='#41B77F', fg='white')
entree_texte.pack(fill=X)

search_button = Button(frame, text="Selection dossier", font=("Arial", 18), bg='white', fg='#41B77F', command=RechercheDossier)
search_button.pack(fill=X)



start_button = Button(frame, text="Rechercher", font=("Arial", 18), bg='white', fg='#41B77F', command=RechercheMot)

#disposition en grid
frame.pack(expand="YES")

#frame.pack(expand=YES)

window.mainloop()