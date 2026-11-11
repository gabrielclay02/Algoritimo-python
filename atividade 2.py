#  pedindo os dados

consumo= int(input("digite seu consumo de energia em kwh: "))
bandeira= input("bandeira(v,a,r): ").upper()
social= input("tarifa social(s,n): ").upper()


# colocado as condicoes para não aceitar valores invalidos
if consumo < 0.0:
    print("voce não pode digitar um valor menor que 0")
elif bandeira not in {"V","A","R"} or social not in {"S","N"}:
    print("voce digitou um valor invalido")


# calculando o valor consumo * faixa de a cordo com a bandeira

else:
    valor_faixa =0.0
if consumo <= 100:
    valor_faixa =consumo*0.60
elif consumo <=200:
    valor_faixa= (100*0.60) + ((consumo-100)*0.80)
else:
    valor_faixa= (100*0.60) + (100*0.80) + ((consumo-200)*1.10)

if social=="s" and consumo <=220:
 valor_faixa= valor_faixa*0.60
 taxa_iluminação= 0.0

else:
   taxa_iluminação= 12.00

if bandeira == "V":
    adicional_bandeira = consumo * 0.00
elif bandeira == "A":
    adicional_bandeira = consumo * 0.02
elif bandeira == "R":
    adicional_bandeira = consumo * 0.05

total= valor_faixa + taxa_iluminação + adicional_bandeira

print(f"o valor total que voce vai pagar e:r${total:.2f} ")

    
