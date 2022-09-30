import arquivos

facil = []
medio = []
dificil = []
feitas = []
feitasMedio = []
feitasDificil = []

class Pergunta:
    
    def __init__(self,questao,certa,errada1,errada2,errada3):
        
        self.questao = questao
        self.certa = certa
        self.errada1 = errada1
        self.errada2 = errada2
        self.errada3 = errada3
        
    
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
        f = Pergunta(questao,certa,errada1,errada2,errada3)
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
        m = Pergunta(questao,certa,errada1,errada2,errada3)
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
        d = Pergunta(questao,certa,errada1,errada2,errada3)
        listaDificil(d)
        
def listaDificil(d):
    dificil.append(d)


perguntasFaceis(arquivos.faceis)
perguntasMedias(arquivos.intermediarias)
perguntasDificeis(arquivos.dificeis)



    
    