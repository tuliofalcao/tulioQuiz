import os

arquivo = open("quiz.txt", "r")

faceis = [arquivo.readline()[:-1] for x in range(11)]
del(faceis[0])
faceis = [x.split(",") for x in faceis]

intermediarias = [arquivo.readline()[:-1] for x in range(12,23)]
del(intermediarias[0])
intermediarias = [x.split(",") for x in intermediarias]

dificeis = [arquivo.readline()[:-1] for x in range(23,34)]
del(dificeis[0])
dificeis = [x.split(",") for x in dificeis]







