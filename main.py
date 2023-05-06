# Online Python - IDE, Editor, Compiler, Interpreter

def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_max_counter = 0

    for value in A:
        counters_position = value - 1
        if 1 <= value <= N:
            if counters[counters_position] < last_max_counter:
                counters[counters_position] = last_max_counter
            counters[counters_position] += 1
            if counters[counters_position] > max_counter:
                max_counter = counters[counters_position]
        elif value == N + 1:
            last_max_counter = max_counter

    for i in range(N):
        if counters[i] < last_max_counter:
            counters[i] = last_max_counter

    return counters

N = int(input('Ingresa N:  '))
A = list(map(int, input("Ingrese los valores de A (Ejemplo: 1 2 3 4): ").strip().split()))

print(solution(N, A))

# Developer: Ivy Saskia Sejas Rocabado
