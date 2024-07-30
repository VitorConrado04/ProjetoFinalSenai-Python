#PROGRAMA CRIADO POR VITOR CONRADO PARA FINS ACADÊMICOS.

print('Olá, bem-vindo ao quiz de perguntas dos jogos olímpicos!\n')
dif = int (input('Selecione o nível de dificuldade que você deseja: \n1️⃣ - FÁCIL\n2️⃣ - MÉDIO\n3️⃣ - DIFÍCIL\n'))


#DIF DE NÍVEL FÁCIL SELECIONADA
if dif == 1:
    conf1 = input('Você selecionou o nível fácil, digite S para confirmar ou N para escolher novamente: \n').upper()
    while conf1 == 'N':
        dif = int(input('Selecione o nível de dificuldade que você deseja: \n1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n'))
        conf1 = input('Você selecionou o nível fácil, digite S para confirmar ou N para escolher novamente: \n').upper()

    contadorFacil = 0
    tuplaGabarito = ('FRANÇA', 'FUTEBOL', 'RAYSSA LEAL')
    listaRespostas = []

    pf1 = input('1️⃣ - EM QUAL PAÍS ESTÁ SENDO REALIZADA AS OLÍMPIADAS DE VERÃO DE 2024?\n').upper()
    listaRespostas.append(pf1)

    if pf1 == 'FRANÇA' or pf1 == 'FRANCA':
        print('Resposta correta! 🌍\n')
        contadorFacil += 1
    else:
        print('Resposta errada, a resposta correta era FRANÇA. 🌍\n')

    pf2 = input('2️⃣ - QUAL ESPORTE É PRATICADO PELA ESPORTISTA MARTA NESSAS OLÍMPIADAS? (Dica: é sua sexta olímpiada) \n').upper()
    listaRespostas.append(pf2)

    if pf2 == 'FUTEBOL':
        print('Resposta correta! ⚽\n')
        contadorFacil += 1
    else:
        print('Resposta errada, a resposta correta era FUTEBOL. ⚽\n')

    pf3 = input('3️⃣ - QUAL O NOME DA SKATISTA BRASILEIRA QUE COM APENAS 13 ANOS CONSEGUIU UMA MEDALHA?'
                     'NAS OLÍMPIADAS DE TÓQUIO 2020? \n').upper()
    listaRespostas.append(pf3)

    if pf3 == 'RAYSSA' or pf3 == 'RAYSSA LEAL':
        print('Resposta correta! 🛹\n')
        contadorFacil += 1

    elif pf3 == 'RAISSA' or pf3 == 'RAISSA LEAL':
        print('Na verdade é RAYSSA, com Y, mas vou te dar uma colher de chá! 🛹')
        contadorFacil += 1

    else:
        print('Resposta errada, a resposta correta era RAYSSA LEAL. 🛹\n')

    print('QUIZ ENCERRADO! \n')
    if contadorFacil == 0:
        print(f'Puxa, você foi o bola murcha da rodada, a sua pontuação foi de {contadorFacil} pontos. 😭\n')

    elif contadorFacil == 1:
        print(f'Poderia ter ido melhor ein jogador, a sua pontuação foi de {contadorFacil} pontos. 😢\n')

    elif contadorFacil == 2:
        print(f'Quase gabaritou, mas ficou impedido por um teco, a sua pontuação foi de {contadorFacil} pontos. 😙\n')

    else:
        print(f'DEITOU MEU 10, VOCÊ GABARITOU O QUIZ! a sua pontuação foi de {contadorFacil} pontos. 🥳\n')


    print(f'SEGUE O GABARITO DAS PERGUNTAS: {tuplaGabarito}\n')
    print(f'SEGUE SUAS RESPOSTAS PARA COMPARAÇÃO: {listaRespostas}\n')

#DIF DE NÍVEL MÉDIO SELECIONADA

if dif == 2:
    conf2 = input('Você selecionou o nível médio, digite S para confirmar ou N para escolher novamente: \n').upper()
    while conf2 == 'N':
        dif = int(input('Selecione o nível de dificuldade que você deseja: \n1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n'))
        conf2 = input('Você selecionou o nível médio, digite S para confirmar ou N para escolher novamente: \n').upper()

    contadorMedio = 0
    tuplaGabaritoM = ('ALEMANHA', 'VELA', 'FELPS')
    listaRespostasM = []

    pm1 = input('1️⃣ - CONTRA QUAL PAÍS O BRASIL JOGOU A FINAL DO FUTEBOL MASCULINO NAS OLIMPÍADAS DO RIO 2016? \n').upper()
    listaRespostasM.append(pm1)

    if pm1 == 'ALEMANHA':
        print('Resposta correta! ⚫🔴🟡')
        contadorMedio += 1

    else:
        print('Resposta errada, a resposta correta era ALEMANHA. ⚫🔴🟡')


    pm2 = input('2️⃣ - QUAL O ESPORTE EM QUE O BRASIL POSSUI MAIS MEDALHAS NA HISTÓRIA DOS JOGOS OLÍMPICOS? \n').upper()
    listaRespostasM.append(pm2)

    if pm2 == 'VELA':
        print('Resposta correta! ⛵')
        contadorMedio += 1

    else:
        print('Resposta errada, a resposta correta era VELA. ⛵')

    pm3 = input('3️⃣ - QUAL O NOME DO ATLETA AMERICANO QUE MAIS GANHOU MEDALHAS NA HISTÓRIA DOS JOGOS OLÍMPICOS? \n').upper()
    listaRespostasM.append(pm3)

    if pm3 == 'FELPS' or pm3 == 'MICHAEL FELPS':
        print('Resposta correta! 🏊🏻')
        contadorMedio += 1

    else:
        print('Resposta errada, a resposta correta era MICHAEL FELPS. 🏊🏻')

    print('QUIZ ENCERRADO! \n')
    if contadorMedio == 0:
        print(f'Puxa, você foi o bola murcha da rodada, a sua pontuação foi de {contadorMedio} pontos. 😭\n')

    elif contadorMedio == 1:
        print(f'Poderia ter ido melhor ein jogador, a sua pontuação foi de {contadorMedio} pontos. 😢\n')

    elif contadorMedio == 2:
        print(f'Quase gabaritou, mas ficou impedido por um teco, a sua pontuação foi de {contadorMedio} pontos. 😙\n')

    else:
        print(f'DEITOU MEU 10, VOCÊ GABARITOU O QUIZ! a sua pontuação foi de {contadorMedio} pontos. 🥳\n')

    print(f'SEGUE O GABARITO DAS PERGUNTAS: {tuplaGabaritoM}\n')
    print(f'SEGUE SUAS RESPOSTAS PARA COMPARAÇÃO: {listaRespostasM}\n')

    # DIF DE NÍVEL FÁCIL SELECIONADA

if dif == 3:
    conf3 = input('Você selecionou o nível difícil, digite S para confirmar ou N para escolher novamente: \n').upper()
    while conf3 == 'N':
        dif = int(input('Selecione o nível de dificuldade que você deseja: \n1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n'))
        conf3 = input('Você selecionou o nível difícil, digite S para confirmar ou N para escolher novamente: \n').upper()

    contadorDificil = 0
    tuplaGabaritoD = ('LONDRES', 'ROMA', 'PADRE')
    listaRespostasD = []

    pd1 = input('1️⃣ - QUAL A ÚNICA CIDADE QUE SEDIOU 3 VEZES OS JOGOS OLÍMPICOS DE VERÃO? \n').upper()
    listaRespostasD.append(pd1)

    if pd1 == 'LONDRES':
        print('RESPOSTA CORRETA! 👑')
        contadorDificil += 1

    else:
        print('Resposta errada, a resposta correta era LONDRES. 👑')

    pd2 = input('2️⃣ - EM QUE CIDADE FOI SEDIADO OJ JOGOS OLÍMPICOS DE VERÃO DE 1960? \n').upper()
    listaRespostasD.append(pd2)

    if pd2 == 'ROMA':
        print('RESPOSTA CORRETA! 🐺')
        contadorDificil += 1

    else:
        print('Resposta errada, a resposta correta era ROMA. 🐺')

    pd3 = input('3️⃣ - QUAL ERA A OCUPAÇÃO PROFISSIONAL DO TORCEDOR QUE ATRAPALHOU O BRASILEIRO WANDERLEI CORDEIRO NAS OLÍMPIADAS\n'
                    'DE VERÃO DE 2000 NA MODALIDADE DE MARATONA? \n').upper()
    listaRespostasD.append(pd3)

    if pd3 == 'PADRE':
        print('RESPOSTA CORRETA! ⛪')
        contadorDificil += 1

    else:
        print('Resposta errada, a resposta correta era PADRE. ⛪')

    print('QUIZ ENCERRADO! \n')
    if contadorDificil == 0:
        print(f'Puxa, você foi o bola murcha da rodada, a sua pontuação foi de {contadorDificil} pontos. 😭\n')

    elif contadorDificil == 1:
        print(f'Poderia ter ido melhor ein jogador, a sua pontuação foi de {contadorDificil} pontos. 😢\n')

    elif contadorDificil == 2:
        print(f'Quase gabaritou, mas ficou impedido por um teco, a sua pontuação foi de {contadorDificil} pontos. 😙\n')

    else:
        print(f'DEITOU MEU 10, VOCÊ GABARITOU O QUIZ! a sua pontuação foi de {contadorDificil} pontos. 🥳\n')

    print(f'SEGUE O GABARITO DAS PERGUNTAS: {tuplaGabaritoD}\n')
    print(f'SEGUE SUAS RESPOSTAS PARA COMPARAÇÃO: {listaRespostasD}\n')













