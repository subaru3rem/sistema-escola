def exibir (listaAlunos):
    nome, nota1, nota2, nota3=0,1,2,3
    for aluno in listaAlunos:
        print("nome: ", aluno[nome])
        print("primeira nota: ", aluno[nota1])
        print("segunda nota: ", aluno[nota2])
        print("terceira nota: ", aluno[nota3])
        print("Média", aluno[4])
        print("situação", aluno[5])
