cpf = '62246766150'
cpf_fatiado = cpf[0:9]
contador = 11
soma = 0

for d in cpf_fatiado:
    contador = contador - 1
    d_convertido = int(d)
    x = d_convertido * contador
    soma = soma + x
    resto = (soma * 10) % 11
print(resto)

    
    