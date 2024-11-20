#Formulas
fEletrica = 0.0385
fGas = 466.609
fGasolina = 0.82*0.75*3.7
fEtanol = 1.72
fDiesel = 3.2
fViagem = 0.127

#Médias
motoG = 40
cpG = 14
cmG = 12
cgG = 8
cpA = cpG * 0.7
cmA = cmG * 0.7
cgA = cgG * 0.7
cD = 20
oD = 3

tf = 1

emissao = 0
emissaoA = 0
historico = {}

def calFormula(valor, formula, onibusTrue = 0):
    global emissao
    if onibusTrue == 0:
        emissao = emissao + (valor * formula)
        return emissao
    else:
        emissao = emissao + ((valor * formula)/30)
        return emissao

while tf == 1:
    try:
        print("Calcule sua emissão de carbono anual e mensal\n")
        nome = str(input("Qual o seu nome (Nomes iguais irão atualizar os valores já existentes no histórico)?\n"))
        
        eletrica = float(input("Qual a sua média de uso de energia elétrica mensalmente? (kwh)\n"))
        emissao = calFormula(eletrica, fEletrica)
        
        gas =  float(input("Quantos butijôes de gas você usa no mês?\n"))
        emissao =calFormula(gas, fGas)

        print("Quantos kilometros você percorre com cada tamanho de veículo movido a gasolina mensalmente? Escreva a quantidade de kilometros\n")
        moto = float(input("Motocicleta\n"))
        emissao= calFormula((moto/motoG), fGasolina)

        kgPequeno = float(input("Veículo de pequeno porte (até 1.4L)\n"))
        emissao = calFormula((kgPequeno/cpG), fGasolina)

        kgMedio = float(input("Veículo de médio porte (1.5 a 2.0L)\n"))
        emissao = calFormula((kgMedio/cmG), fGasolina)

        kgGrande = float(input("Veículo de grande porte (maior que 2.0L)\n"))
        emissao = calFormula((kgGrande/cgG), fGasolina)

        print("Quantos kilometros você percorre com cada tamanho de veículo movido a álcool mensalmente? Escreva a quantidade de kilometros\n")
        kaPequeno = float(input("Veículo de pequeno porte (até 1.4L)\n"))
        emissao = calFormula((kaPequeno/cpA), fEtanol)

        kaMedio = float(input("Veículo de médio porte (1.5 a 2.0L)\n"))
        emissao = calFormula((kaMedio/cmA), fEtanol)

        kaGrande = float(input("Veículo de grande porte (maior que 2.0L)\n"))
        emissao = calFormula((kaGrande/cmG), fEtanol)
        
        print("Quantos kilometros você percorre com cada tamanho de veículo movido a diesel mensalmente? Escreva a quantidade de kilometros\n")
        kdCarro = float(input("Carro\n"))
        emissao = calFormula(kdCarro/cD, fDiesel)

        kdOnibus = float(input("Ônibus\n"))
        emissao = calFormula((kdOnibus/oD), fDiesel, 1)

        viagem = float(input("Quantos kilometros você faz em suas viagens aérias anualmente?\n"))
        emissaoA = calFormula(viagem, fViagem)
        emissao = emissao + emissaoA/12
        emissaoA = emissaoA + emissao

        print(f"Seu total de emissões por mês são: {round(emissao, 3)}kg e por ano são: {round((emissaoA)/1000, 3)}T\n")
        print(f"Plante {round((emissaoA)/130, 0)} árvores na Mata Atlântica ou no Cerrado (crescimento das árvores em 30 anos) ou {round((emissaoA)/222,  0)} árvores na Amazônia (crescimento das árvores em 30 anos) para compensar a sua emissão anual\n")

        print(f"O valor do carbono, no dia 01/11/24, estava custando R$63,87 por tonelada de CO2 emitido (de acordo com o site br.investing.com).\n")

        print(f"Formas de reduzir as emissões de CO2:\nTransporte: Preferir o transporte público, a bicicleta ou caminhar. Também é possível escolher veículos que emitem menos CO2.\nConsumo: Reduzir o consumo de combustíveis fósseis, como petróleo e gasolina. Também é possível diminuir o consumo de carne e optar por alimentos orgânicos.\nEnergia: Economizar energia é uma das formas mais eficazes de reduzir a pegada de carbono. Algumas dicas são desligar a luz ao sair de uma sala, desconectar dispositivos eletrônicos e trocar lâmpadas incandescentes por LED.\nLixo: Reciclar o lixo.\n")
        print(f"Essas são algumas das alternativas para reduzir as suas emisões de carbono.\n")

        dic = {
                "nome": nome,
                "emissaoM": emissao,
                "emissaoA": emissaoA
            }
        historico[nome] = dic
        print(historico)
                
        while True:
            opcao = int(input("Deseja usar o programa novamente? (Digite o número da opção)\n1.Sim\n2.Não\n3.Ver histórico\n"))
            match opcao:
                case 1:
                    break
                case 2:
                    print("Obrigado por usar")
                    tf = 0
                    break
                case 3:
                    es = int(input("Deseja:\n1.Ver todo histórico\n2.Pesquisar por nome\n"))
                    match es:
                        case 1:
                            print(historico)
                            continue
                        case 2:
                            nomeH = str(input("Qual seu nome?\n"))
                            valor = historico.get(nomeH, "Não encontrado")
                            print(valor)
                            continue
                case _:
                    print("COLOQUE UMA OPÇÃO VÁLIDA!")
                    continue
    except:
        print("Ocorreu um erro durante a execução. Reiniciando o programa e apagando os dados")
        emissao = 0
        emissaoA = 0
        continue


