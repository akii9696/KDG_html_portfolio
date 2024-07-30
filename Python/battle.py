# 4対のモンスターデータ
nlist = ["スライム","ホイミスライム","ばくだんいわ","キラーマシン"]
import random
def create_monster(nlist):
    monster_status = []

#HP,攻撃,防御を保持
    for i in nlist:
        status = []
        status.append(i)
        status.append(random.randint(50,100))
        status.append(random.randint(50,100))
        status.append(random.randint(50,100))
        status.append(random.randint(50,100))

        monster_status.append(status)
#戻り値もってくる
    return monster_status



#listing_monsterで形を整理
def listing_monster(monster_deta):
    for monster_status in monster_deta:
        for deta in monster_status:
            print(str(deta) + " " ,end="")
        print()

#ランダムに攻撃を受けるモンスターを決定
#被らなくなるまで繰り返し
def damage_monster(a,n):
    x = n[random.randint(0,len(nlist) -1)]
    while x == a:
        x = n[random.randint(0,len(nlist) -1)]
    return a,x


#ダメージ計算関数
#intで整数型にする
def damage(a,b):
    saitee = int((int(a) - int(b) / 2) / 4)
    saikoo = int((int(a) - int(b) / 2) / 2)
    c = random.randint(saitee,saikoo)
    return c


#呼び出しプログラム
monster_list = create_monster(nlist)
listing_monster(monster_list)

i = damage_monster("スライム",nlist)
print(i[0])
print(i[1])

print(damage(100,50))