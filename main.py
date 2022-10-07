import escola
cad=""
MediaAlunos = []
alunos = {}
while cad !="0":
    cad=input("""1 - cadastrar novo aluno
    2 - exibir alunos
    3 - aplicar media
    4 - aplicar situação
    0 - sair
    """)
    if cad == "1":
        nome=input("nome")
        alunos.update(aluno = escola.cadastro())
    elif cad == "2":
        print(alunos)
    elif cad == "3":
        for i in range(len(alunos)):
         m = escola.media(alunos[i][1],alunos[i][2],alunos[i][3])
         alunos[i][4]=m
    elif cad == "4":
       for i in range(len(alunos)):
         alunos[i][5]=escola.situacao(alunos[i][4])
    else:
        if cad !="0":
            print("voce n digitou oq foi pedido")