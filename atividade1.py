# calculo nota
print("ola, aluno!")

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    print("Erro: nota inválida.")

else:
    
if n1 >= n2 and n1 >= n3:
   maior = n1
if n2 >= n3:
   meio = n2
   menor = n3
else:
    meio = n3
    menor = n2

elif n2 >= n1 and n2 >= n3:
    maior = n2
 if n1 >= n3:
    meio = n1
    menor = n3
 else:
     meio = n3
     menor = n1

else:
    maior = n3
if n1 >= n2:
    meio = n1
    menor = n2
else:
     meio = n2
    menor = n1

 media = (maior * 5 + meio * 3 + menor * 2) / 10

 if media >= 6:
     print(f"Média: {media:.2f} - APROVADO")
else:
    print(f"Média: {media:.2f} - REPROVADO")
