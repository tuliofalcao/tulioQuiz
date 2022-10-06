from random import shuffle

facil = []
medio = []
dificil = []

class Pergunta:
    
    def __init__(self,questao,certa,errada1,errada2,errada3,nivel,feita=False):
        
        self.questao = questao
        self.certa = certa
        self.errada1 = errada1
        self.errada2 = errada2
        self.errada3 = errada3
        self.nivel = nivel
        self.feita = False
        
    
def perguntasFaceis(lista):
    
    for x in range(10):
        a = lista
        for y in range(5):
            if y == 0:
                questao = a[x][y]
            elif y == 1:
                certa = a[x][y]
            elif y == 2:
                errada1 = a[x][y]
            elif y == 3:
                errada2 = a[x][y]
            else:
                errada3 = a[x][y]
            nivel = "facil"
            feita = False
        f = Pergunta(questao,certa,errada1,errada2,errada3,nivel,feita)
        listaFacil(f)
        
def listaFacil(f):
    facil.append(f)
        
def perguntasMedias(lista):
    for x in range(10):
        a = lista
        for y in range(5):
            if y == 0:
                questao = a[x][y]
            elif y == 1:
                certa = a[x][y]
            elif y == 2:
                errada1 = a[x][y]
            elif y == 3:
                errada2 = a[x][y]
            else:
                errada3 = a[x][y]
            nivel = "medio"
            feita = False
        m = Pergunta(questao,certa,errada1,errada2,errada3,nivel,feita)
        listaMedia(m)
        
def listaMedia(m):
    medio.append(m)
    
def perguntasDificeis(lista):
    for x in range(10):
        a = lista
        for y in range(5):
            if y == 0:
                questao = a[x][y]
            elif y == 1:
                certa = a[x][y]
            elif y == 2:
                errada1 = a[x][y]
            elif y == 3:
                errada2 = a[x][y]
            else:
                errada3 = a[x][y]
            nivel = "dificil"
            feita = False
        d = Pergunta(questao,certa,errada1,errada2,errada3,nivel,feita)
        listaDificil(d)
        
def listaDificil(d):
    dificil.append(d)

def retornaPergunta(lista):
    while True:
        shuffle(lista)
        if lista[0].feita == True:
            continue
        else:
            lista[0].feita = True
            break
    return lista[0]






    
    