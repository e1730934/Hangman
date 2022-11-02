# 420-2C3-MA Programmation Objet

## Hangman

#### Groupes 1 et 4

#### Prof.: Denis Rinfret

- **Travail à faire individuellement ou en équipe de 2**. Vous pouvez utiliser
  vos notes, les exemples présentés en classe, faire des recherches sur le web,
  mais vous ne pouvez pas obtenir d'aide d'une autre personne, sauf le
  professeur ou les tuteurs.

- **Date de remise** : 2021-05-30, avant minuit.

- **À remettre** : sur Léa, un fichier zip, contenant 1 dossier et tous vos 
  fichiers Python, tel que décrit plus bas.

- Vérifiez la taille du fichier zip que vous remettez : si elle est trop grande,
  si elle se compte en Mo, vous avez probablement inclus des fichiers et/ou
  dossiers non-essentiels, comme par exemple un dossier nommé
  `venv` qui contient un environnement virtuel Python.

- **Assurez-vous de suivre les consignes**, sinon, une pénalité pourrait être
  appliquée.

### Préparation

1. Créez un dossier nommé `tp2_1234567` ou `tp2_1234567_12345678`, dans lequel 
   vous devez remplacer `1234567` par votre numéro d'étudiant (c.-à-d. votre 
   numéro de dossier), et `1234568` par celui de votre partenaire (le cas 
   échéant).
2. Si vous travaillez en équipe, chaque membre de l'équipe devrait soumettre 
   le fichier zip sur Léa par mesure d'assurance.
3. Un formulaire d'enregistrement des équipes va être partagé ultérieurement. 
   SVP, le remplir même si vous avez décidé de travailler seul. Il y aura 
   une option pour cette situation.
4. Organisez votre code correctement. Utilisez, entre autres, la commande
   PyCharm "*Reformat Code*" (`Ctrl+Alt+L`) pour vous aider.

### Description générale

Vous devez construire une application avec une interface graphique simple 
utilisant *Tkinter*. Vous pouvez faire l'application décrite plus bas, ou 
choisir votre propre application. Vous devriez faire approuver votre idée 
d'application par le professeur pour vous assurer que le sujet et la 
difficulté sont appropriés.

Peu importe le sujet choisi, vous devrez inclure les éléments suivants dans 
votre application :

- lire ou écrire dans un fichier (fichier texte, CSV, image, ...)
- utiliser des listes et/ou des dictionnaires de façon appropriée
- définir une ou des classes, avec leurs attributs et méthodes appropriés

### Application suggérée

Faites un jeu de type *"Bonhomme Pendu"* avec une interface graphique simple.
Il n'est pas nécessaire de dessiner de beaux graphiques, mais il devrait y 
avoir quelques éléments d'interface graphique dans l'application, comme 
quelques boutons, étiquettes, ...

#### Fonctionnalités à inclure dans l'application
- Un bouton, ou un menu, 
    - pour lire une liste de mots à partir d'un fichier
    - pour débuter une nouvelle partie
    - pour abandonner la partie courante
    - pour quitter l'application
- Un endroit (étiquette, canvas, ...) qui montre le mot à être deviné 
  (peut-être avec des `"_"` pour remplacer les lettres non découvertes)
- Afficher, d'une façon logique, les lettres déjà devinées
- Demander une lettre au joueur
- Afficher la progression du jeu (par exemple, le nombre d'essais restant)
