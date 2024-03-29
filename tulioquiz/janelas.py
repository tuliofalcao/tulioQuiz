import PySimpleGUI as sg 
import perguntas
import jogador
from random import shuffle

listaQuestoes = []


def abertura():
    
    layout = [
        [sg.Text("Bem-vindo ao Quiz!")],
        [sg.Push()],
        [sg.Push()],
        [sg.Text('Digite seu nome:'),sg.Input(key='nome')],
        [sg.Push()],
        [sg.Button('INICIAR')]
    ]   
    return sg.Window('QUIZ',layout,element_justification='center',finalize=True)

def pergunta1():
    #while True:
    #    shuffle(perguntas.facil)
    #    if perguntas.facil[0].feita == True:
    #        continue
    #    else:
    #        break
    #perguntas.facil[0].feita = True
    p = perguntas.retornaPergunta(perguntas.facil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes.append(certa)
    listaQuestoes.append(errada1)
    listaQuestoes.append(errada2)
    listaQuestoes.append(errada3)
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 1 - Nível: FÁCIL")],
        [sg.Push()],
        [sg.Text(perguntas.facil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta2():
    #while True:
    #    shuffle(perguntas.facil)
    #    if perguntas.facil[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.facil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 2 - Nível: FÁCIL")],
        [sg.Push()],
        [sg.Text(perguntas.facil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta3():
    #while True:
    #    shuffle(perguntas.facil)
    #    if perguntas.facil[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.facil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 3 - Nível: FÁCIL")],
        [sg.Push()],
        [sg.Text(perguntas.facil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)
    
def pergunta4():
    
    p = perguntas.retornaPergunta(perguntas.medio)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 4- Nível: INTERMEDIÁRIO")],
        [sg.Push()],
        [sg.Text(perguntas.medio[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)        
    
def pergunta5():
    #while True:
    #    shuffle(perguntas.medio)
    #    if perguntas.medio[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.medio)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 5 - Nível: INTERMEDIÁRIO")],
        [sg.Push()],
        [sg.Text(perguntas.medio[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta6():
    #while True:
    #    shuffle(perguntas.medio)
    #    if perguntas.medio[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.medio)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 6 - Nível: INTERMEDIÁRIO")],
        [sg.Push()],
        [sg.Text(perguntas.medio[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta7():
    p = perguntas.retornaPergunta(perguntas.dificil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 7 - Nível: DIFÍCIL")],
        [sg.Push()],
        [sg.Text(perguntas.dificil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)
    
def pergunta8():
    #while True:
    #    shuffle(perguntas.dificil)
    #    if perguntas.dificil[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.dificil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 8 - Nível: DIFÍCIL")],
        [sg.Push()],
        [sg.Text(perguntas.dificil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta9():
    #while True:
    #    shuffle(perguntas.dificil)
    #    if perguntas.dificil[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.dificil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 9 - Nível: DIFÍCIL")],
        [sg.Push()],
        [sg.Text(perguntas.dificil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)

def pergunta10():
    #while True:
    #    shuffle(perguntas.dificil)
    #    if perguntas.dificil[0].feita == True:
    #        continue
    #    else:
    #        break
    
    p = perguntas.retornaPergunta(perguntas.dificil)
    certa = (p.certa, 'certa')
    errada1 = (p.errada1, 'errada')
    errada2 = (p.errada2, 'errada')
    errada3 = (p.errada3, 'errada')
    listaQuestoes[0] = certa
    listaQuestoes[1] = errada1
    listaQuestoes[2] = errada2
    listaQuestoes[3] = errada3
    shuffle(listaQuestoes)
    
    layout = [
        [sg.Text(f"Jogador: {jogador.jogadores[0].nome}"), sg.Push(), sg.Text(f"Pontos: {jogador.jogadores[0].pontuacao}")],
        [sg.Text("Pergunta Nº 10 - Nível: DIFÍCIL")],
        [sg.Push()],
        [sg.Text(perguntas.dificil[0].questao)],
        [sg.Push()],
        [sg.Push()],
        [sg.Button(listaQuestoes[0][0],key='r1')],
        [sg.Button(listaQuestoes[1][0],key='r2')],
        [sg.Button(listaQuestoes[2][0],key='r3')],
        [sg.Button(listaQuestoes[3][0],key='r4')]
    ]
    return sg.Window("QUIZ", layout, element_justification='center',finalize=True)    

def final():
    
    layout = [
        [sg.Text(f"PARABÉNS, {jogador.jogadores[0].nome}!")],
        [sg.Text(f"Você fez {jogador.jogadores[0].pontuacao} pontos!")],
        [sg.Push()],
        [sg.Push()],
        [sg.Text("Clique no botão abaixo para visualizar o Ranking:")],
        [sg.Button('RANKING',key='cabou')]
    ] 
    return sg.Window('QUIZ', layout,element_justification='center',finalize=True)    
