n = int(input("\nWhat do you want to find the square root of? "))
error = int(input("How many decimal points do you need? "))
g = [1]
i = 0
while abs(n - g[-1] ** 2) > 10 ** (-error):
    g.append((n / g[-1] + g[-1]) / 2)

print("\nguesses:")

for j, guess in enumerate(g):
    print(" " + str(j) + ": " + str(round(guess, error)))

print("\nanswer: " + str(round(guess, error)) + "\n")
