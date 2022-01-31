# takes half an hour or something but it works

combos = 0
for penny in range(201):
    if penny % 10 == 0:
        print(penny)
    for twocent in range(101):
        for nickel in range(41):
            for dime in range(21):
                for fifth in range(11):
                    for halfdollar in range(5):
                        for dollar in range(3):
                            if penny + 2 * twocent + 5 * nickel + 10 * dime + 20 * fifth + 50 * halfdollar + 100 * dollar == 200:
                                combos += 1

# one combo for 1 200 cent coin
combos += 1
print(combos)