# Recette familiale echine d'entrecôte porc grillé servit avec un sauce de tomate accompagner de couscous.

import webbrowser
img = webbrowser.open('repas.png')

print()
print()

recette_entrecote_sauce_couscous = (
    "échine d'entrecôte porc grillé au couscou", # nom de la recette
    {"entrecôte": (2, "unités"),
    "curcuma moulu": (1, "pincée(s)" ),
"gingembre moulu": (1, "pincée(s)"),
"moutarde de dijon traditionnelle": (1, "cuillère(s) à café"),
    "purée de tomate": (25, "millilittre(s)"),
"oignon": (1/6,"boule(s)"),
"ail": (1, "quartier(s)"),
"sel": (1, "pincéé(s)"),
"huile d'olive": (2, "millilitres"),
    "couscous": (50,"gramme(s)"),
"beurre": (1/2, "noisette(s) de beurre"),
"eau": (70, "millilitres")},#quantité pour une personne 
    [
        "Dans un récipient creux, mélanger tous les éléments de marinade et enduisez généreusement les entrecôteS. Couvrez d\'un film alimentaire et réservez au réfrigérateur minimum 1 heure. ",
        "Sortez les entrecôtes du réfrigérateur 30 min avant de les griller.",
        "Faites chauffer le poêle à feu vif et mettre les entrecôtes à griller. Retournez à mi-cuisson sans piquer la viande. Faites cuire environ 2 à 3 min par face selon l'épaisseur de la viande. Les mettre de côté pour la suite. " 
    , #préparation des entrecôtes     
    
        "Découpez les oignons et ails en tout petits morceaux.",
        "Faites chauffer le poêle à feu vif, mettrez  d'huile, puis les mettez les morceaux coupés et versez la purée de tomate. Remuez pendant 3 à 4min. Mettez de côté pour le dressage."
    ,
    
        "Dans un saladier adapté au four à Micro-ondes, verser l'eau tiède salée sur la graine de couscous avec l'huile.",
        "Laisser gonfler les graines 3 à 4 min puis mélanger à la fourchette.",
        "Couvrir et mettre au four à Microonde pendant 2 min à puissance max (800watts).",
        "Ajouter le beurre et égrener soigneusement à la fourchette.",
    ]
)

nombre_personnes = int(input("Combien de personnes mangeront votre plat d\'échine d'entrecôte porc grillé au couscou? "))

quantites_finales = {ingredient: (quantite[0] * nombre_personnes, quantite[1]) for ingredient, quantite in recette_entrecote_sauce_couscous[1].items()}

print("Recette :", recette_entrecote_sauce_couscous[0])
print()
print("Ingrédients pour", nombre_personnes, "personne(s) :")
print()

for ingredient, quantite in quantites_finales.items():
    print("- ", ingredient, ":", quantite[0], quantite[1])
print()
print("Préparation :")
print()
for index, etape in enumerate(recette_entrecote_sauce_couscous[2], start=1):
    if "{" in etape:
        print(f"{index}. {etape.format(**quantites_finales)}")
    else:
        print(f"{index}. {etape}")
print()
print("Dressez")
print("servez")

print(img)
