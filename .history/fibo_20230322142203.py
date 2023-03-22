def fibo_check(number):
    primeiro_valor = 0
    segundo_valor = 1
    while segundo_valor < number:
        primeiro_valor, segundo_valor = segundo_valor, primeiro_valor + segundo_valor
    if segundo_valor == number:
        return f'O número {number} pertence à sequência de Fibonacci.'
    else:
        return f'O número {number} não pertence à sequência de Fibonacci.'

print(fibo_check(4181))  # O número 4181 pertence à sequência de Fibonacci.
print(fibo_check(256))   # O número 256 não pertence à sequência de Fibonacci.