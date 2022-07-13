def menu():
    print("------------------")
    print("  Sistema de Notas  ")
    print("------------------")
    print("1- Cadastrar aluno")
    print("2- Total de alunos")
    print("3- Total de alunas sexo feminino")
    print("4- Total de alunos sexo masculino")
    print("5- Total de alunos aprovados")
    print("6- Total de alunos de exame")
    print("7- Total de alunos reprovados")
    print("8- Relatorio em porcentagem e valores absolutos")
    print("9- Boletim alunos")
    print("10- SAIR")
    print("------------------")
    print("Selecione uma opção: ")


def menu2():
    menu()
    return verificador_inteiro('', False)


def is_int(valor):
    try:
        int(valor)
    except:
        return False

    return True


def valida(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            if not valor < 0 and not valor > 10:
                ok = True
            else:
                print('Digite a nota entre 0 e 10!')
        else:
            print('Digite um numero!')
        if ok:
            break
    return valor


def verificador_inteiro(texto, imprimir=True):
    validador = False
    while not validador:
        if imprimir:
            print("Digite o valor", texto)
        entrada = input()
        validador = is_int(entrada)
    return int(entrada)


turma = list()
aluno = dict()
notas = list()


def cadastrarAluno():
    while True:
        aluno.clear()
        notas.clear()
        aluno['nome'] = str(input('Nome do aluno: '))
        while True:
            aluno['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
            if aluno['sexo'] in 'MF':
                break
            print('Digite apenas M ou F')

        for i in range(0, 3):
            notas.append(valida(f'Digite a nota {i + 1}: '))
            aluno['notas'] = notas[:]
            aluno['média'] = sum(notas) / 3

        media = aluno['média']
        if media >= 7:
            status = "Aprovado"
        elif media >= 4 and media < 7:
            status = 'Exame'
        elif media < 4:
            status = 'Reprovado'
        aluno['status'] = status

        turma.append(aluno.copy())
        while True:
            resp = str(input('Quer cadastrar outro aluno? [S/N]')).upper()[0]
            if resp in 'SN':
                break
        if resp == 'N':
            break
    return turma


def totalAlunos():
    cont = 0
    for i in turma:
        if i['nome']:
            cont = cont + 1
    return cont


def qtdMulheres():
    cont = 0
    for i in turma:
        if i['sexo'] in 'Ff':
            cont = cont + 1
    print("-" * 30)
    print('Total de mulheres cadastradas: ', cont)
    print("-" * 30)


def qtdHomens():
    cont = 0
    for i in turma:
        if i['sexo'] in 'Mm':
            cont = cont + 1
    print("-" * 30)
    print('Total de homens cadastrados: ', cont)
    print("-" * 30)


def statusHomens():
    aprov = 0
    exam = 0
    rep = 0
    for i in turma:
        if i['sexo'] in 'Mm':
            if i['status'] == 'Aprovado':
                aprov = aprov + 1
            elif i['status'] == "Exame":
                exam = exam + 1
            elif i['status'] == "Reprovado":
                rep = rep + 1
    print('Total de homens aprovados: ', aprov)
    print("-" * 30)
    print('Total de homens exame: ', exam)
    print("-" * 30)
    print('Total de homens reprovados: ', rep)
    print("-" * 30)


def statusMulheres():
    aprov = 0
    exam = 0
    rep = 0
    for i in turma:
        if i['sexo'] in 'Ff':
            if i['status'] == 'Aprovado':
                aprov = aprov + 1
            elif i['status'] == "Exame":
                exam = exam + 1
            elif i['status'] == "Reprovado":
                rep = rep + 1
    print('Total de mulheres aprovadas: ', aprov)
    print("-" * 30)
    print('Total de mulheres exame: ', exam)
    print("-" * 30)
    print('Total de mulheres reprovadas: ', rep)
    print("-" * 30)


def qtdAprovados():
    cont = 0
    for i in turma:
        if i['status'] == 'Aprovado':
            cont = cont + 1
    return cont


def qtdExame():
    cont = 0
    for i in turma:
        if i['status'] == 'Exame':
            cont = cont + 1
    return cont


def qtdReprovado():
    cont = 0
    for i in turma:
        if i['status'] == 'Reprovado':
            cont = cont + 1
    return cont


def porcentagem():
    aprovados = qtdAprovados()
    exame = qtdExame()
    reprovados = qtdReprovado()
    total = totalAlunos()

    if aprovados == 0:
        print("Não existe alunos aprovados!")
        print("-" * 30)
    else:
        percAprovado = aprovados * 100 / total
        print('Porcentual de alunos aprovados: ', percAprovado, '%')
        print("-" * 30)

    if exame == 0:
        print("Não existe alunos de exame!")
        print("-" * 30)
    else:
        percExame = exame * 100 / total
        print('Porcentual de alunos exame: ', percExame, '%')
        print("-" * 30)

    if reprovados == 0:
        print("Não existe alunos reprovados!")
        print("-" * 30)
    else:
        percReprovado = reprovados * 100 / total
        print('Porcentual de alunos reprovados: ', percReprovado, '%')
        print("-" * 30)


if __name__ == "__main__":
    opcao = 0
    while opcao != 10:
        opcao = menu2()

        if opcao == 1:
            cadastrarAluno()
        elif opcao == 2:
            print('Total de alunos:', totalAlunos())
        elif opcao == 3:
            qtdMulheres()
        elif opcao == 4:
            qtdHomens()
        elif opcao == 5:
            print('Total de alunos aprovados: ', qtdAprovados())
        elif opcao == 6:
            print('Total de alunos de exame: ', qtdExame())
        elif opcao == 7:
            print('Total de alunos reprovados: ', qtdReprovado())
        elif opcao == 8:
            statusHomens()
            statusMulheres()
            porcentagem()
        elif opcao == 9:
            if not turma:
                print('Não existe alunos cadastrados!')
            else:
                print("----------BOLETIM-------------")
                for i in turma:
                    print(i)
        elif opcao != 10:
            print('Opção inválida')
        elif opcao == 10:
            print('Bye guys!')
