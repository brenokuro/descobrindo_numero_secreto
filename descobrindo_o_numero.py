#Crie um algoritmo em Português ou qualquer outra linguagem onde o usuário deve 
# adivinhar um número secreto (ex: 7)
#O sistema informa se o número digitado é maior ou menor até acertar.

numeroSecreto = 9


while True:
    

    tentativa = int(input("Digite o número e descubra se é o NÚMERO SECRETO... "))
    
    if tentativa > numeroSecreto:
        print("Quase lá seu número foi maior que o NÚMERO SECRETO")
    elif tentativa < numeroSecreto:
        print("Quase lá seu número foi menor que o NÚMERO SECRETO")
   
        
    else:
        print("Parbéns!!! você acertou o NÚMERO SECRETO")
        break
