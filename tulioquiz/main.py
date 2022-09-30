import PySimpleGUI as sg 
import janelas
import jogador
import pickle

#tema
sg.theme('DarkBlue17')

try:
    with open('ranking.pkl','rb') as arq:
        ranking = pickle.load(arq)
    print(ranking)
except:
    pass

#gerenciamento de janelas
abertura,pergunta1,pergunta2,pergunta3,pergunta4,pergunta5,pergunta6,pergunta7,pergunta8,pergunta9,pergunta10,final = janelas.abertura(),None,None,None,None,None,None,None,None,None,None,None

while True:
    window,event,values = sg.read_all_windows()
    
    #abertura
    if window == abertura and event == 'INICIAR':
        nome = values['nome']
        pontuacao = 0
        usuario = jogador.Jogador(nome,pontuacao)
        jogador.jogadores.append(usuario)
        abertura.hide()
        pergunta1 = janelas.pergunta1()
        
    #primeira pergunta
    if window == pergunta1 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta1.hide()
                    pergunta2 = janelas.pergunta2()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta1.hide()
                    pergunta2 = janelas.pergunta2()
                    
    #segunda pergunta
    if window == pergunta2 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta2.hide()
                    pergunta3 = janelas.pergunta3()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta2.hide()
                    pergunta3 = janelas.pergunta3()
    
    #terceira pergunta
    if window == pergunta3 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta3.hide()
                    pergunta4 = janelas.pergunta4()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta3.hide()
                    pergunta4 = janelas.pergunta4()
                    
    #quarta pergunta
    if window == pergunta4 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta4.hide()
                    pergunta5 = janelas.pergunta5()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta4.hide()
                    pergunta5 = janelas.pergunta5()
                    
    #quinta pergunta
    if window == pergunta5 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta5.hide()
                    pergunta6 = janelas.pergunta6()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta5.hide()
                    pergunta6 = janelas.pergunta6()
                    
    #sexta pergunta
    if window == pergunta6 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta6.hide()
                    pergunta7 = janelas.pergunta7()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta6.hide()
                    pergunta7 = janelas.pergunta7()
                    
    #sétima pergunta
    if window == pergunta7 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta7.hide()
                    pergunta8 = janelas.pergunta8()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta7.hide()
                    pergunta8 = janelas.pergunta8()
                    
    #oitava pergunta
    if window == pergunta8 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta8.hide()
                    pergunta9 = janelas.pergunta9()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta8.hide()
                    pergunta9 = janelas.pergunta9()
                    
    #nona pergunta
    if window == pergunta9 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta9.hide()
                    pergunta10 = janelas.pergunta10()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta9.hide()
                    pergunta10 = janelas.pergunta9()
                    
    #décima pergunta
    if window == pergunta10 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        for x in janelas.listaQuestoes:
            if window[event].get_text() == x[0]:
                if x[1] == 'certa':
                    sg.Popup("Parabéns! Ganhou mais um ponto!")
                    jogador.jogadores[0].pontuacao += 1
                    pergunta10.hide()
                    ranking = janelas.final()
                else:
                    sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
                    pergunta10.hide()
                    final = janelas.final()
    
    #ranking
    if window == final and event == 'cabou':
        nome = jogador.jogadores[0].nome
        print(nome)
        pontos = jogador.jogadores[0].pontuacao
        print(pontos)
        primeiroLugar = ''
        segundoLugar = ''
        terceiroLugar = ''
        quartoLugar = ''
        quintoLugar = ''
        primeiroLugarPontos = 0
        segundoLugarPontos = 0
        terceiroLugarPontos = 0
        quartoLugarPontos = 0
        quintoLugarPontos = 0
        print(primeiroLugar)
        print(primeiroLugarPontos)
        if pontos > primeiroLugarPontos:
            primeiroLugar, primeiroLugarPontos = nome, pontos
        elif pontos > segundoLugarPontos:
            segundoLugar, segundoLugarPontos = nome, pontos
        elif pontos > terceiroLugarPontos:
            terceiroLugar, terceiroLugarPontos = nome, pontos
        elif pontos > quartoLugarPontos:
            quartoLugar, quartoLugarPontos = nome, pontos
        elif pontos > quintoLugarPontos:
            quintoLugar, quintoLugarPontos = nome, pontos
        sg.popup_scrolled(f"===== RANKING =====\n\n1º - {primeiroLugar} - {primeiroLugarPontos} pontos\n2º - {segundoLugar} - {segundoLugarPontos} pontos\n3º - {terceiroLugar} - {terceiroLugarPontos} pontos\n4º - {quartoLugar} - {quartoLugarPontos} pontos\n5º - {quintoLugar} - {quintoLugarPontos} pontos\n")
        ranking = {}
        ranking[primeiroLugar] = primeiroLugarPontos
        ranking[segundoLugar] = segundoLugarPontos
        ranking[terceiroLugar] = terceiroLugarPontos
        ranking[quartoLugar] = quartoLugarPontos
        ranking[quintoLugar] = quintoLugarPontos
        final.hide()
        abertura = janelas.abertura()
        
              
       
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        with open('ranking.pkl','wb') as arq:
            arquivoPickle = pickle.dump(ranking,arq)
        break
        
        
window.close()
    
        
