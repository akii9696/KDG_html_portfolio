### インポート
import sys
import random
 
### 行動パターン
act_dic = {"a":"攻撃", "b":"防御", "c":"魔法"}
 
### キャラクターパラメーター
### 名前,HP,攻撃力,防御力,魔力,素早さ
play_lst = [["プレイヤーA", "-", 30, 9, 8, 1, 3],
            ["プレイヤーB", "-", 25, 7, 6, 4, 7],
            ["プレイヤーC", "-", 20, 4, 4, 8, 5]]
mons_lst = [["モンスターA", "A", 40, 9, 6, 1, 2],
            ["モンスターB", "A", 38, 8, 5, 1, 3],
            ["モンスターC", "A", 36, 7, 6, 1, 5],
            ["モンスターD", "B", 31, 6, 6, 4, 4],
            ["モンスターE", "B", 28, 6, 6, 4, 6],
            ["モンスターF", "B", 26, 5, 5, 5, 8],
            ["モンスターG", "C", 22, 3, 3, 8, 5],
            ["モンスターH", "C", 20, 4, 4, 6, 7],
            ["モンスターI", "C", 18, 1, 3, 9, 4]]
 
### 行動の重み
### グループ,攻撃,防御,魔法
wegt_lst = [["A",4,1,0],
            ["B",2,1,1],
            ["C",1,1,4]]
 
### クラス定義 ###
class Charpram:
 
    ### 初期化メソッド
    def __init__(self, name, grup, hitp, atck, dfns, magc, agil):
 
        ### パラメーター
        self.name = name    # 名前
        self.grup = grup    # 行動グループ
        self.hitp = hitp    # HP
        self.atck = atck    # 攻撃力
        self.dfns = dfns    # 防御力
        self.magc = magc    # 魔力
        self.agil = agil    # 素早さ
        self.actn = None    # 行動
        self.stat = None    # 状態
 
    ### ダメージ計算メソッド
    def cal_damage(self):
 
        ### ローカル変数
        f_damage = 0
 
        ### 行動分岐
        if   self.actn == "攻撃":
            f_damage = round(self.atck * (1 + random.randrange(100) / 100))
        elif self.actn == "防御":
            f_damage = 0
        elif self.actn == "魔法":
            f_damage = round(self.magc * (1 + random.randrange(100) / 100))
 
        return f_damage
 
    ### 素早さ補正メソッド
    def cal_agil(self):
 
        ### ローカル変数
        f_agil = 0
 
        ### 行動分岐
        if   self.actn == "攻撃":
            f_agil = self.agil * (1 + random.randrange(100) / 100)
        elif self.actn == "防御":
            f_agil = self.agil * 1.5 * (1 + random.randrange(100) / 100)
        elif self.actn == "魔法":
            f_agil = self.agil * 0.5 * (1 + random.randrange(100) / 100)
 
        return f_agil
 
### 戦闘関数定義 ###
def battle(arg1, arg2):
 
    ### ローカル変数
    f_damage = 0
 
    ### 対象キャラのHPが0の場合は終了
    if arg2.hitp == 0:
 
        ### メッセージ表示
        if arg1.actn == "防御":
            print("＋＋ {}は{}を実行！".format(arg1.name, arg1.actn))
        else:
            print("＋＋ {}の{}が失敗！".format(arg1.name, arg1.actn))
 
        return
 
    ### 攻撃
    if   arg1.stat == "攻撃":
 
        ### 相手が防御
        if arg2.stat == "防御":
            dfns = arg2.dfns * 2
        else:
            dfns = arg2.dfns
 
        ### ダメージ計算
        f_damage = max(0, arg1.cal_damage() - dfns)
        arg2.hitp -= f_damage
        arg2.hitp = max(0, arg2.hitp)
 
    ### 防御
    elif arg1.stat == "防御":
 
        ### ダメージ0
        f_damage = 0
 
    ### 魔法
    elif arg1.stat == "魔法":
 
        ### ダメージ計算
        f_damage = max(0, arg1.cal_damage())
        arg2.hitp -= f_damage
        arg2.hitp = max(0, arg2.hitp)
 
    ### メッセージ表示
    if arg1.actn == "防御":
        print("＋＋ {}は{}を実行！".format(arg1.name, arg1.actn))
    else:
        print("＋＋ {}は{}を実行！ {}は{}のダメージ".format(arg1.name, arg1.actn, arg2.name, f_damage))
 
### キャラクター削除関数定義 ###
def obj_del(arg):
 
    ### リストの要素数分ループ
    for x in arg:
 
        ### 対象のHPが0の場合
        if x.hitp == 0:
 
            ### 対象の要素を削除
            arg.remove(x)
 
### モンスター疲労度表示関数定義 ###
def mons_stat(arg):
 
    ### モンスターの最大HPを取得
    for x in mons_lst:
        if x[0] == arg.name:
            break
 
    ### 残HPの割合を取得
    r_hp = arg.hitp / x[2]
 
    ### 状態を返す
    if   r_hp > 0.9:
        return "元気"
    elif r_hp > 0.3:
        return "疲労"
    else:
        return "瀕死"
 
### メイン処理 ###
 
### プレイヤーインスタンス生成
play_obj = []
for x in play_lst:
    play_obj.append(Charpram(*x))
 
### モンスターの出現数設定
mons_num = random.randint(1, 3)
 
### モンスターをリストからランダムで取得
mons_tmp = random.sample(mons_lst, k=mons_num)
 
### モンスターインスタンス生成
mons_obj = []
for x in mons_tmp:
    mons_obj.append(Charpram(*x))
 
### 出現モンスター表示
print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
for x in mons_obj:
    print("＋＋ {}が現れた！".format(x.name))
print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
 
### 戦闘が終了するまでループ
while True:
 
    ### エラーフラグ
    err_flg = 0
 
    ### プレイヤー行動辞書定義
    p_act_dic = {}
 
    ### 行動入力
    print(">>> 行動を選択してください")
    print(">>> a:攻撃 b:防御 c:魔法 q:終了")
    for x in play_obj:
        print("[" + x.name + "] ", end="")
        player = input(">>> ")
 
        ### 終了
        if   player == "q":
            sys.exit()
 
        ### 入力エラー
        elif player not in list(act_dic.keys()):
            print("＋＋ a:攻撃 b:防御 c:魔法 q:終了 を入力してください")
            print()
            err_flg = 1
            break
 
        ### 行動辞書に保存
        p_act_dic[x.name] = act_dic[player]
 
    ### 入力エラーは最初からやり直す
    if err_flg == 1:
        continue
 
    ### 行動順辞書定義
    order_dic = {}
 
    ### 行動順辞書にプレイヤーの行動を保存
    for x in p_act_dic.items():
        for p_obj in play_obj:
            if p_obj.name == x[0]:
                p_obj.actn = x[1]
                if p_obj.stat != "死亡":
                    p_obj.stat = "待機"
 
                ### 素早さ補正
                order_dic[p_obj.name] = p_obj.cal_agil()
 
    ### 行動順辞書にモンスターの行動を保存
    for m_obj in mons_obj:
        if   m_obj.grup == "A":
            act_grup = wegt_lst[0][1:]
        elif m_obj.grup == "B":
            act_grup = wegt_lst[1][1:]
        elif m_obj.grup == "C":
            act_grup = wegt_lst[2][1:]
        else:
            act_grup = [1,1,1]
 
        m_obj.actn = random.choices(list(act_dic.values()),weights=act_grup)[0]
        if m_obj.stat != "死亡":
            m_obj.stat = "待機"
 
        ### 素早さ補正
        order_dic[m_obj.name] = m_obj.cal_agil()
 
    ### 行動
    for character in sorted(order_dic.items(), key=lambda arg: arg[1], reverse=True):
 
        ### プレイヤー行動
        for play in play_obj:
 
            if character[0] == play.name:
 
                ### 行動キャラクターのHPが0の場合はスキップ
                if play.hitp == 0:
                    break
 
                ### 状態に行動を設定
                play.stat = play.actn
 
                ### 戦う相手をランダムで選択
                mons = random.choice(list(mons_obj))
 
                ### 戦闘
                battle(play, mons)
 
                ### HPが0ならメッセージ表示
                if mons.hitp == 0 and mons.stat != "死亡":
                    mons.stat = "死亡"
                    print("＜＜ {}を倒しました!!!!! ＞＞".format(mons.name))
 
        ### モンスター行動
        for mons in mons_obj:
 
            if character[0] == mons.name:
 
                ### 行動キャラクターのHPが0の場合はスキップ
                if mons.hitp == 0:
                    break
 
                ### 状態に行動を設定
                mons.stat = mons.actn
 
                ### 戦う相手をランダムで選択
                play = random.choice(list(play_obj))
 
                ### 戦闘
                battle(mons, play)
 
                ### HPが0ならメッセージ表示
                if play.hitp == 0 and play.stat != "死亡":
                    play.stat = "死亡"
                    print("＜＜ {}は倒されました... ＞＞".format(play.name))
 
    ### プレイヤー辞書から削除
    for i in range(len(play_obj)):
        obj_del(play_obj)
 
    ### モンスター辞書から削除
    for i in range(len(mons_obj)):
        obj_del(mons_obj)
 
    ### プレイヤーのHPを表示
    if len(play_obj) > 0:
        print("－－－－－－－－－－－－－－－－－")
        for x in play_obj:
            print("＋＋ {}：HP[{}]".format(x.name, x.hitp))
        print("－－－－－－－－－－－－－－－－－")
 
    ### モンスターを表示
    if len(mons_obj) > 0:
        print("－－－－－－－－－－－－－－－－－")
        for x in mons_obj:
            print("＋＋ {}：[{}]".format(x.name, mons_stat(x)))
        print("－－－－－－－－－－－－－－－－－")
 
    ### どちらかが全滅であれば終了
    if len(play_obj) == 0:
        print()
        print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
        print("＋＋ プレイヤーは全滅しました ＋＋")
        print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
        break
 
    if len(mons_obj) == 0:
        print()
        print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
        print("＋＋ モンスターは全滅しました ＋＋")
        print("＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋")
        break
 
    ### 空行
    print()