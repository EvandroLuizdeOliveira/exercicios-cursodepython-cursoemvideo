"""
programa que imprime x números da sequência de fibonacci

Resolução 1:

numero = int(input('Digite um número: '))
seq_fibo = 0
cont = 0
while numero > 0:
    if seq_fibo == 0:
        print(seq_fibo, end=' ')
        seq_fibo = 1
        print(seq_fibo, end=' ')
        numero -= 2
    else:
        cont_posterior = seq_fibo
        seq_fibo = seq_fibo + cont
        print(seq_fibo, end=' ')
        cont = cont_posterior
        numero -= 1
"""
print(f'{"-" * 30}'
      f'\n Sequência de Fibonacci'
      f'\n{"-" * 30}')
termos = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
print(f'{"~" * 30}')
print(f'{t1} → {t2} → ', end='')
cont = 3
while cont != termos:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')
print(f'{"~" * 30}')
