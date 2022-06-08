
def checkin():
    #Jogando tudo do arquivo txt pra variavel listaUsuarios
    arquivo = open("reservas.txt", "r")
    listaUsuarios = arquivo.readlines()
    arquivo.close()

    listaBusca = list()
    respostinha = input('Para realizar a busca, digite o CPF cadastrado: ')
    for usuario in listaUsuarios:
        titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = usuario.split(',')
        #print(titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status)
        #Compara a resposta do usuário com todos os CPFs do arquivo txt, aqueles que forem iguais serão adicionados na listaBusca.
        if respostinha == cepef: 
            listaBusca.append(usuario)

        #FOCO: preciso puxar a lista toda e mudar só o elemento que eu quero, que no caso é o status R. Como?

    if len(listaBusca) >1:
        auxiliar = 0
        for z in listaBusca:
            print('-'*50)
            print('|{}º - {}'.format(auxiliar+1, listaBusca[auxiliar]))
            auxiliar+=1
        answear = int(input('Qual das reservas você gostaria de realizar o Check-In? '))
        if answear >= 1 and answear <= len(listaBusca):
            print('abacaxi')
       #     print(listaBusca[answear-1])                         #EMPACADO
       #     fragmentando = listaBusca[answear-1].split(',')
       #     print(fragmentando[-1])
        else:
            print('Por favor, escolha um número presente na tabela.')
    else:
        print('Se entrou aqui significa que só tem 1 registro com o CPF, tem que editar esse único')
        pass 

    return listaBusca
            

def cadastroReservas():
    print('-'*50)
    print('A seguir, preencha as informações para realizar o cadastro.\n')

    #Solicitando Nome//Para fins de praticidade, coloca tudo maiusculo e remove os Espaços.
    titular = input('Nome da pessoa titular: ')
    if titular.find(' ') == -1:
        titular = titular.upper()
    else:
        titular = titular.replace(' ','')
        titular = titular.upper()

    #Solicitando/Validando CPF
    cepef = input('CPF: ')
    if len(cepef) == 11:
        pass
    else:
        cepef = 'None'

    #Numero de Pessoas//Verificação para não haver vaga fantasma.
    numeroPessoas = int(input('Quantas pessoas vão ir? '))
    if numeroPessoas >0:
        pass
    else:
        print('Voce não pode alugar para {} pessoa(s).'.format(numeroPessoas))
        numeroPessoas = 'None' #Esse None é uma jambrada que eu fiz pra validar mais pra frente

    #Tipo do Quarto//Identifica qual tipo de quarto+informa caso não tenha escolhido algúm da tabela
    tipoQuarto = input('''
    -----SELECIONE O TIPO DE QUARTO-----
    |S- Standard     (100p/dia p/pessoa)
    |D- Deluxe       (200p/dia p/pessoa)
    |P- Premium      (300p/dia p/pessoa)
    Opção Desejada: ''')
    tipoQuarto = tipoQuarto.upper()
    if tipoQuarto == 'S':
        pass
    elif tipoQuarto == 'D':
        pass
    elif tipoQuarto == 'P':
        pass
    else:
        print('Tipo: "{}" não identificado.\nPor favor, siga a tabela.'.format(tipoQuarto))
        tipoQuarto = 'None'
    
    #Numero de dias, já faz validação para não ter aluguel fantasma.
    numeroDias = int(input('Quantos dias? '))
    if numeroDias >0:
        pass
    else:
        print('Você não pode alugar um quarto por "{}" dias.\n'.format(numeroDias))
        numeroDias = 'None'
    
    #Calculando valor. Se uma das 3 variáveis necessárias para o calculo for 'None', define o próprio calculoValor para None, assim não passa na validação final.
    if tipoQuarto == 'None' or numeroPessoas == 'None' or numeroDias == 'None':
        calculoValor = 'None'
    else:
        if tipoQuarto == "S":
            calculoValor = (numeroPessoas*100)*numeroDias
            calculoValor = str(calculoValor)
        elif tipoQuarto == "D":
            calculoValor = (numeroPessoas*200)*numeroDias
            calculoValor = str(calculoValor)
        elif tipoQuarto == "P":
            calculoValor = (numeroPessoas*300)*numeroDias
            calculoValor = str(calculoValor)

    #Status padrão
    status = 'R'
    
    #Transformando em lista
    test = "{} {} {} {} {} {} {}".format(titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status)
    test = test.split(' ')
    print(test)
    
    #Aqui é a validação final. Se alguma das variáveis anteriores foram definidas para None, não será adicionado no txt, vai cair no else.
    if 'None' in test:
        print('-'*50)
        print('>>>Erro ao realizar cadastro. Por favor, tente novamente.')
    else:
        arquivo = open("reservas.txt", "a")#Abrir arquivo com 'a', para dar append
        #Deve ter uma forma mais elegante de fazer esses writes aqui, mas eu não sei e não to mto afim de buscar :p
        arquivo.write('\n'+test[0]+',')
        arquivo.write(test[1]+',')
        arquivo.write(test[2]+',')
        arquivo.write(test[3]+',')
        arquivo.write(test[4]+',')
        arquivo.write(test[5]+',')
        arquivo.write(test[6])
        arquivo.close()
        print('-'*50)
        print('>>>Cadastro realizado com sucesso!')
        return arquivo


#Menu Principal
menup = ('''
    ------MENU PRINCIPAL------
    |1- Cadastrar uma reserva.
    |2- Entrada do Cliente(Check=in).
    |3- Saída do Cliente(Check-out).
    |4- Alterar reserva.
    |5- Relatórios.
    |6- Sair.
    ''')

numero = 0 #Auxiliar para funcionamento do while
opcoes = [1,2,3,4,5,6] #Opcoes disponíveis

print(menup)
while numero >=0 and numero <=6:
    resposta = int(input('Qual opção você deseja realizar? '))
    if resposta in opcoes:
        if resposta == 1:
            arquivo = cadastroReservas()
            #arquivo = open("reservas.txt", "r")
            #print(arquivo.readlines())
            #arquivo.close()
            print(menup)
        elif resposta ==2:
            listaBusca = checkin()
            #print(listaBusca)
            print(menup)
        elif resposta == 3:
            print('3')
        elif resposta == 4:
            print('4')
        elif resposta ==5:
            print('5')
        elif resposta == 6:
            print('>>>Saindo...')
            break
    else:
        print('Escolha um número presenta na tabela.\n{}'.format(menup))
        
