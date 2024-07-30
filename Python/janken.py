print("じゃんけんゲームを開始します")
aiko = 1
kati = 0
cpkati = 0

while kati < 1 and cpkati < 1:
    you = input("最初はグー！")
    print(you)
    import random
    hand = ["グー" , "チョキ" ,"パー"]
    mk = ["上","下","左","右"]
    muki = random.randint(0,3)
    janken = random.randint(0,2)
    print("CP " + hand[janken])

    if hand[janken] == you:
            print("あいこだからもう一回")
    elif janken == 0:
        if you == "チョキ":
            print("負け")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("lose")    
                cpkati += 1
            else:
                print("win")
        elif you == "パー":
            print("勝ち")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("win")    
                kati += 1
            else:
                print("lose")
    elif janken == 1:
        if you == "グー":
            print("勝ち")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("win")    
                kati += 1
            else:
                print("lose")
        elif you == "パー":
            print("負け")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("lose")    
                cpkati += 1
            else:
                print("win")
    elif janken == 2:
        if you == "グー":
            print("負け")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("lose")
                cpkati += 1    
            else:
                print("win")
            cpkati += 1
        elif you == "チョキ":
            print("勝ち")
            aiko = 0
            muki2 = input("あっち向いてホイ")
            print("anata " + str(muki2))
            print("cp " + mk[muki])
            if mk[muki] == muki2:
                print("win")    
                kati += 1
            else:
                print("lose")
    print("you " + str(kati))
    print("cp " + str(cpkati))

