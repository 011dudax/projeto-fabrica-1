nota1 = float(input("digite a nota1"))
nota2 = float(input("digite a nota2"))
nota3 = float(input("digite a nota3"))
nota4 = float(input("digite a nota4"))
media = (nota1 + nota2 + nota3 + nota4) /4

if media >=7:
    print(f"media:(media:.2f) situação: aprovado(a)")
elif media >=5.0 and media <7.0:
    print(f"media:.2f)- situação aprovado(a)")
elif media <5.8:
    print(f"media:.2f") - situação: aprovado (a) ")