power_level = int(input())

for i in range(power_level):
    N = int(input())
    if N > 8000:
        print("Over 8000!")
    else:
        print("Insect!")
