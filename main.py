import random

from lectureDictionnaire import ouvertureFichier
import tkinter as tk
import string
from tkinter import ttk
from tkinter import filedialog, messagebox


class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bonhomme Pendu")
        self.create_widgets()
        self.dictionnaire = None
        self.partiDemarrer = False

    def ouvrirListMot(self):
        file = filedialog.askopenfilename()
        self.dictionnaire = ouvertureFichier(file)
        messagebox.showinfo("Dictionnaire", "Le dictionnaire a bien été sélectionné")

    def abondonnerPartie(self):
        self.partiDemarrer = False
        self.lblVariableMotDeviner.config(text="")
        self.lblVariableGuessRestant.config(text="")
        self.lblTxtFaux.config(text="")

    def nouvellePartie(self):
        if self.dictionnaire is None:
            self.ouvrirListMot()
        self.secret = random.choice(self.dictionnaire)
        self.lettres_devinees = []
        self.lettres_erronees = []
        self.lblVariableGuessRestant.config(text=99)
        self.lblVariableMotDeviner.config(text="")
        self.lblTxtFaux.config(text="")

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5
        # defaultGuessRestant = 5

        frameEntrerUtilisateur = ttk.LabelFrame(self.window, text="Entrer", relief=tk.RIDGE)
        frameEntrerUtilisateur.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        lblSaisiLettre = ttk.Label(frameEntrerUtilisateur, text="Veuillez entrer une lettre: ")
        lblSaisiLettre.grid(row=1, column=1, sticky=tk.W, pady=3)

        lblValidation = ttk.Label(frameEntrerUtilisateur, text="Insertion de lettre:")
        lblValidation.grid(row=2, column=1, sticky=tk.W, pady=3)

        self.entrerUtilisateur = ttk.Entry(frameEntrerUtilisateur, width=40)
        self.entrerUtilisateur.grid(row=1, column=2, sticky=tk.W, pady=3)
        self.entrerUtilisateur.insert(tk.END, "")

        btmValidation = tk.Button(frameEntrerUtilisateur, text="Valider", command=self.btmClickValidation)
        btmValidation.grid(row=2, column=2)

        frameDevinette = ttk.LabelFrame(self.window, text="Devinette", relief=tk.RIDGE)
        frameDevinette.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        lblTxtTemp = ttk.Label(frameDevinette, text="Mot à deviner: ")
        lblTxtTemp.grid(row=1, column=1, sticky=tk.W, pady=3)

        self.lblVariableMotDeviner = ttk.Label(frameDevinette, text="")
        self.lblVariableMotDeviner.grid(row=1, column=2, sticky=tk.W, pady=3)

        lblTxtLettre = ttk.Label(frameDevinette, text="Lettre erronée: ")
        lblTxtLettre.grid(row=2, column=1, sticky=tk.W, pady=3)

        self.lblTxtFaux = ttk.Label(frameDevinette, text="")
        self.lblTxtFaux.grid(row=2, column=2, sticky=tk.W, pady=3)

        lblGuessRestant = ttk.Label(frameDevinette, text="Nombre d'essais restant:")
        lblGuessRestant.grid(row=3, column=1, sticky=tk.W, pady=3)

        self.lblVariableGuessRestant = ttk.Label(frameDevinette, text="")
        self.lblVariableGuessRestant.grid(row=3, column=2, sticky=tk.W, pady=3)

        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Ouvrir une liste de mots", command=self.ouvrirListMot)
        filemenu.add_command(label="Débuter une nouvelle partie", command=self.nouvellePartie)
        filemenu.add_separator()
        filemenu.add_command(label="Abandonner la partie courante", command=self.abondonnerPartie)
        filemenu.add_command(label="Quitter l'application", command=self.window.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)

        self.window.config(menu=menubar)

    def run(self):
        self.window.mainloop()

    def btmClickValidation(self):
        lettre = self.entrerUtilisateur.get()
        longeurLettre = len(lettre)
        if self.dictionnaire is None:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dictionnaire à partir du menu.")
        elif ((longeurLettre != 1) or (
                lettre not in (string.ascii_letters + "âêîôûéàèùÂÊÎÔÛÉÀÈÙ"))) and self.dictionnaire is not None:
            messagebox.showerror("Erreur", "Veuillez insérer une lettre.")
        else:
            lettre = lettre.upper()
            if self.partiDemarrer is False:
                self.nouvellePartie()
                self.partiDemarrer = True

            if lettre in self.secret:
                self.lettres_devinees.append(lettre)
                mot_a_devoiler = []
                for c in self.secret:
                    if c in self.lettres_devinees:
                        mot_a_devoiler.append(c)
                    else:
                        mot_a_devoiler.append("_")
                self.lblVariableMotDeviner.config(text=mot_a_devoiler)
                self.entrerUtilisateur.delete(0, "end")
                if "_" not in mot_a_devoiler:
                    messagebox.showinfo("Victoire", "Vous avez deviné le mot!")
            else:
                self.lettres_erronees.append(lettre)
                self.lblTxtFaux.config(text=self.lettres_erronees)
                txtLblGuess = (self.lblVariableGuessRestant['text'])
                nbrGuessRestant = txtLblGuess - 1
                self.lblVariableGuessRestant.config(text=nbrGuessRestant)
                self.entrerUtilisateur.delete(0, "end")
                if nbrGuessRestant <= 0:
                    messagebox.showinfo("Défaite", "Vous n'avez pas deviné le mot!")
                    self.abondonnerPartie()


if __name__ == '__main__':
    qw = App()
    qw.run()
