# Exercício 2: Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e que esse programa
# decida se a pessoa está apta a ser do Exército Brasileiro. Para entrar no Exército Brasileiro é necessário
# possuir mais de 18 anos de idade, pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70m.

idade = input('Insira sua idade: ')
peso = input('Insira seu peso: ')
altura = input('Insira sua altura: ')

if (idade >= '18') and (peso >= '60') and (altura >= '1.70'):
    print('Você atende a todos requisitos para entrar no Exército Brasileiro.')

elif (idade >= '18') and (peso >= '60') and (altura < '1.70'):
    print('Você atende a maioria dos requisitos, porém, não possui altura o suficiente. Você não está apto.')

elif (idade >= '18') and (peso < '60') and (altura >= '1.70'):
    print('Você atende a maioria dos requisitos, porém, não possui peso suficiente para ingressar. Você não está apto.')

elif (idade < '18') and (peso >= '60') and (altura >= '1.70'):
    print('Você atende a maioria dos requisitos, porém, não possui idade o suficiente. Volte mais tarde.')

elif (idade >= '18') and (peso < '60') and (altura < '1.70'):
    print('Você possui idade o suficiente, mas não possui o peso nem a altura necessária. Volte mais tarde.')

elif (idade < '18') and (peso >= '60') and (altura < '1.70'):
    print('Você não possui idade e nem altura suficiente para ingressar no Exército Brasileiro.')

else:
    print('Você não pode ingressar no Exército Brasileiro, pois não atende aos requisitos necessários.')