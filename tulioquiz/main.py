import PySimpleGUI as sg
import janelas
import jogador
import perguntas

#tema
sg.theme('DarkBlue17')

#gerenciamento de janelas
abertura,pergunta1,pergunta2,pergunta3,pergunta4,pergunta5,pergunta6,pergunta7,pergunta8,pergunta9,pergunta10,final = janelas.abertura(),None,None,None,None,None,None,None,None,None,None,None

while True:
    window,event,values = sg.read_all_windows()
    
    #abertura
    if window == abertura and event == 'INICIAR':
        
        #abre o arquivo ranking.txt
        rank = open('ranking.txt','r')
        ranking = [rank.readline()[:-1] for x in range(6)]
        del(ranking[0])
        ranking = [x.split('-') for x in ranking]
        ranking = [[x[0][:-1],x[1][1:-1],x[2][1:]] for x in ranking]
        rankingOrdem = {}
        for x in range(5):
            rankingOrdem[ranking[x][1]] = int(ranking[x][2][0:2].strip())
        rank.close()
        
        #abre o arquivo com perguntas
        arquivo = open("quiz.txt", "r")

        faceis = [arquivo.readline()[:-1] for x in range(11)]
        del(faceis[0])
        faceis = [x.split(",") for x in faceis]
        print(f'main/abertura/faceis: {faceis}')

        intermediarias = [arquivo.readline()[:-1] for x in range(12,23)]
        del(intermediarias[0])
        intermediarias = [x.split(",") for x in intermediarias]

        dificeis = [arquivo.readline()[:-1] for x in range(23,34)]
        del(dificeis[0])
        dificeis = [x.split(",") for x in dificeis]
        
        #recebe as listas com perguntas para criar os objetos-pergunta
        perguntas.perguntasFaceis(faceis)
        perguntas.perguntasMedias(intermediarias)
        perguntas.perguntasDificeis(dificeis)
        
        #dados da tela
        nome = values['nome']
        pontuacao = 0
        usuario = jogador.Jogador(nome,pontuacao)
        jogador.jogadores.append(usuario)
        abertura.hide()
        pergunta1 = janelas.pergunta1()
        
    #primeira pergunta
    if window == pergunta1 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.facil[0].certa:
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
        if window[event].get_text() == perguntas.facil[0].certa:
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
        if window[event].get_text() == perguntas.facil[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta3.hide()
            pergunta4 = janelas.pergunta4()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta3.hide()
            pergunta4 = janelas.pergunta4()
                    
    #quarta pergunta
    if window == pergunta4 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.medio[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta4.hide()
            pergunta5 = janelas.pergunta5()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta4.hide()
            pergunta5 = janelas.pergunta5()
                    
    #quinta pergunta
    if window == pergunta5 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.medio[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta5.hide()
            pergunta6 = janelas.pergunta6()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta5.hide()
            pergunta6 = janelas.pergunta6()
                    
    #sexta pergunta
    if window == pergunta6 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.medio[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta6.hide()
            pergunta7 = janelas.pergunta7()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta6.hide()
            pergunta7 = janelas.pergunta7()
                    
    #sétima pergunta
    if window == pergunta7 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.dificil[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta7.hide()
            pergunta8 = janelas.pergunta8()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta7.hide()
            pergunta8 = janelas.pergunta8()
                    
    #oitava pergunta
    if window == pergunta8 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.dificil[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta8.hide()
            pergunta9 = janelas.pergunta9()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta8.hide()
            pergunta9 = janelas.pergunta9()
                    
    #nona pergunta
    if window == pergunta9 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.dificil[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta9.hide()
            pergunta10 = janelas.pergunta10()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta9.hide()
            pergunta10 = janelas.pergunta10()
                    
    #décima pergunta
    if window == pergunta10 and (event == 'r1' or event == 'r2' or event == 'r3' or event=='r4'):
        if window[event].get_text() == perguntas.dificil[0].certa:
            sg.Popup("Parabéns! Ganhou um ponto!")
            jogador.jogadores[0].pontuacao += 1
            pergunta10.hide()
            final = janelas.final()
        else:
            sg.Popup("Que pena! Resposta incorreta! Tente na próxima!")
            pergunta10.hide()
            final = janelas.final()
    
    #ranking
    if window == final and event == 'cabou':
        nome = jogador.jogadores[0].nome
        pontos = jogador.jogadores[0].pontuacao
        rankingOrdem[nome] = pontos
        ordem = sorted(rankingOrdem.items(), key=lambda x: x[1], reverse=True)
        print(rankingOrdem)
        print(ordem)
        rankingOrdem = {}        
        
        sg.popup_scrolled(f"========== RANKING ==========\n\n1º - {ordem[0][0]} - {ordem[0][1]} pontos\n2º - {ordem[1][0]} - {ordem[1][1]} pontos\n3º - {ordem[2][0]} - {ordem[2][1]} pontos\n4º - {ordem[3][0]} - {ordem[3][1]} pontos\n5º - {ordem[4][0]} - {ordem[4][1]} pontos\n")
        
        rank = open('ranking.txt','w')
        rank.writelines(['========== RANKING ==========',f"\n1º - {ordem[0][0]} - {ordem[0][1]} pontos",f"\n2º - {ordem[1][0]} - {ordem[1][1]} pontos",f"\n3º - {ordem[2][0]} - {ordem[2][1]} pontos",f"\n4º - {ordem[3][0]} - {ordem[3][1]} pontos",f"\n5º - {ordem[4][0]} - {ordem[4][1]} pontos"])
        rank.close()
        
        jogador.jogadores = []
        
        final.hide()
        abertura = janelas.abertura()
        
              
       
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
        
        
window.close()
    
        
