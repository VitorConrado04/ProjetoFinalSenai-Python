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

    pf1 = input('1 - EM QUAL PAÍS ESTÁ SENDO REALIZADA AS OLÍMPIADAS DE VERÃO DE 2024?\n').upper()
    listaRespostas.append(pf1)

    if pf1 == 'FRANÇA' or pf1 == 'FRANCA':
        print('Resposta correta! 🌍\n')
        contadorFacil += 1
    else:
        print('Resposta errada, a resposta correta era FRANÇA. 🌍\n')

    pf2 = input('2 - QUAL ESPORTE É PRATICADO PELA ESPORTISTA MARTA NESSAS OLÍMPIADAS? (Dica: é sua sexta olímpiada) \n').upper()
    listaRespostas.append(pf2)

    if pf2 == 'FUTEBOL':
        print('Resposta correta! ⚽\n')
        contadorFacil += 1
    else:
        print('Resposta errada, a resposta correta era FUTEBOL. ⚽\n')

    pf3 = input('3 - QUAL O NOME DA SKATISTA BRASILEIRA QUE COM APENAS 13 ANOS CONSEGUIU UMA MEDALHA?'
                     'NAS OLÍMPIADAS DE TÓQUIO 2020? \n').upper()
    listaRespostas.append(pf3)

    if pf3 == 'RAYSSA' or pf3 == 'RAYSSA LEAL':
        print('Resposta correta! 🛹\n')
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
    conf2 = input('Você selecionou o nível fácil, digite S para confirmar ou N para escolher novamente: \n').upper()
    while conf2 == 'N':
        dif = int(input('Selecione o nível de dificuldade que você deseja: \n1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n'))
        conf2 = input('Você selecionou o nível fácil, digite S para confirmar ou N para escolher novamente: \n').upper()

    contadorMedio = 0
    tuplaGabaritoM = ('FRANÇA', 'FUTEBOL', 'RAYSSA LEAL')
    listaRespostasM = []

    pm1 = input('CONTRA QUAL PAÍS O BRASIL JOGOU A FINAL DO FUTEBOL MASCULINO NAS OLIMPÍADAS DO RIO 2016? \n').upper()

    if pm1 == 'ALEMANHA':
        print('Resposta correta! ⚫🔴🟡')
        contadorMedio += 1

    else:
        print('Resposta errada, a resposta correta era ALEMANHA. ⚫🔴🟡')


    pm2 = input('QUAL O ESPORTE EM QUE O BRASIL POSSUI MAIS MEDALHAS NA HISTÓRIA DOS JOGOS OLÍMPICOS? \n').upper()

    if pm2 == 'VELA':
        print('Resposta correta! ⛵')

    else:
        print('Resposta errada, a resposta correta era VELA. ⛵')
