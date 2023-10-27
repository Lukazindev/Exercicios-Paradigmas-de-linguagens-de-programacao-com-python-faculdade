p = float(input('Qual seu peso?'))
alt = eval(input('Qual sua altura?'))
imc = p / (alt ** 2)
print('O seu IMC é: {imc}'.format())