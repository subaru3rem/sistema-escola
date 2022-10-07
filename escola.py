def cadastro():
    nota1 = input("nota1: ")  
    nota2 = input("nota2: ")
    nota3 = input("nota3: ")
    media = 0
    situação = ""
def exibir(listaAlunos):
    nome, nota1, nota2, nota3=0,1,2,3
    for aluno in listaAlunos:
        print("nome: ", aluno[nome])
        print("primeira nota: ", aluno[nota1])
        print("segunda nota: ", aluno[nota2])
        print("terceira nota: ", aluno[nota3])
        print("Média", aluno[4])
        print("situação", aluno[5])
def media(nota1,nota2,nota3):
      (float(nota1)+float(nota2)+float(nota3))/3
def situacao(media):
     if media >=7:
        return"aprovado"