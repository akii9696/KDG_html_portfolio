dan=1
kazu=1

for dan in range(1,10):
    for kazu in range(1,9):
        print(str(dan) + "×" + str(kazu) + "=" + str(dan*kazu) + "  ",end="")
    kazu += 1
    print(str(dan) + "×" + str(kazu) + "=" + str(dan*kazu) + "  \n")