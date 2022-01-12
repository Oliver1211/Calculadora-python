v1 = input('Insira o primeiro Valor ')
op = input('Insira o operador ')
v2 = input('Insira o segundo valor ')

while True:

    if not v1.isnumeric() or not v2.isnumeric():
        print('Isso  não é um numero, digite apenas numeros')
        break

    v1 = int(v1)
    v2 = int(v2)

    if op == '+':
        print(f'Resultado da soma é {v1 + v2}')
        break
    elif op == '*':
        print(f'Valor da multiplicação é {v1 * v2}')
        break
    elif op == '/' :
        print(f'Valor da divisão é {v1 / v2[2]}')
        break
    elif op == '-':
        print(f'Valor da subtração é {v1 - v2}')
        break
    else:
        print('Imprima valores em numeros')
