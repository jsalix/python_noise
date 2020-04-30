import random

GRADIENT = ["░", "▒", "▓"]

SIZE_X = 30
SIZE_Y = 10

random.seed("helloworld!")

for y in range(SIZE_Y):
    for x in range(SIZE_X):
        random_num = random.randrange(0, len(GRADIENT))
        gradient_char = GRADIENT[random_num]
        print(gradient_char, end='')
    print()

print("Done!")
