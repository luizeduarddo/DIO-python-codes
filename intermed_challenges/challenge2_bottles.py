def calculate_full_bottles(N, K):
    exchanged_bottles = N // K
    remaining_bottles_day_1 = N % K
    full_bottles_day_2 = exchanged_bottles + remaining_bottles_day_1
    return full_bottles_day_2

repetitions = int(input())

for i in range(repetitions):
    N, K = map(int, input().split())
    result = calculate_full_bottles(N, K)
    print(result)
