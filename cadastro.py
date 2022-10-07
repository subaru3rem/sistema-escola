from media import media
from situacao import situacao

def cadastro():
    nome = input("Nome: ")
    nota1 = input("nota1: ")  
    nota2 = input("nota2: ")
    nota3 = input("nota3: ")
    media = 0
    situação = ""
    return[nome,nota1,nota2,nota3,media,situação]
