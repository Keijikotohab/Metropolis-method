import random
import math
import numpy as np
import matplotlib.pyplot as plt

#1.------------------------------------

#n=表の出る数
def P(n):
    if n==0:
        return 1/1024#(1/2**10)
    elif n==1:
        return 10/1024#(1/2**10)*10C1
    elif n==2:
        return 45/1024#(1/2**10)*10C2
    elif n==3:
        return 120/1024#(1/2**10)*10C3
    elif n==4:
        return 210/1024#(1/2**10)*10C4
    elif n==5:
        return 252/1024#(1/2**10)*10C5
    elif n==6:
        return 210/1024#(1/2**10)*10C6
    elif n==7:
        return 120/1024#(1/2**10)*10C7
    elif n==8:
        return 45/1024#(1/2**10)*10C8
    elif n==9:
        return 10/1024#(1/2**10)*10C9
    elif n==10:
        return 1/1024#(1/2**10)

left = np.array([0,1,2,3,4,5,6,7,8,9,10])#62~69行目 matplotlibでヒストグラム表示
height = np.array([1/1024,10/1024,45/1024,120/1024,210/1024,\
252/1024,210/1024,120/1024,45/1024,10/1024,1/1024])#10000で割り100分率(割合)に変換
plt.plot(left, height)
plt.title('Probability distribution')
plt.xlabel('Number of front')
plt.ylabel('Percentage of front')
plt.show()

#2.------------------------------------------

def calculate(N):#N=10000
    zero=0#8~18行目 結果記録用変数を定義
    once=0
    twice=0
    three_times=0
    four_times=0
    five_times=0
    six_times=0
    seven_times=0
    eight_times=0
    nine_times=0
    ten_times=0

    for i in range(N):#n=10000
        true_1=0 #表の数、10回コインを投げるごとにここで初期化
        for a in range(10):#試行回数10回（０〜９）
            n=random.choice([1,0])#コインを投げる。表（１）と裏（０）からランダムで選択
            if n==1:#もし表(1)が出たなら表の数のカウントを増やす
                true_1+=1

        if true_1==0:#27~48行目 10回コインを投げるごとに結果記録用変数にカウント
            zero+=1
        elif true_1==1:
            once+=1
        elif true_1==2:
            twice+=1
        elif true_1==3:
            three_times+=1
        elif true_1==4:
            four_times+=1
        elif true_1==5:
            five_times+=1
        elif true_1==6:
            six_times+=1
        elif true_1==7:
            seven_times+=1
        elif true_1==8:
            eight_times+=1
        elif true_1==9:
            nine_times+=1
        elif true_1==10:
            ten_times+=1

    print(zero)#50~60行目結果表示
    print(once)
    print(twice)
    print(three_times)
    print(four_times)
    print(five_times)
    print(six_times)
    print(seven_times)
    print(eight_times)
    print(nine_times)
    print(ten_times)

    left = np.array([0,1,2,3,4,5,6,7,8,9,10])#62~69行目 matplotlibでヒストグラム表示
    height = np.array([zero/N,once/N,twice/N,\
    three_times/N,four_times/N,five_times/N,six_times/N,\
    seven_times/N,eight_times/N,nine_times/N,ten_times/N])#10000で割り100分率(割合)に変換
    plt.plot(left, height)
    plt.title('Probability distribution')
    plt.xlabel('Number of front')
    plt.ylabel('Percentage of front')
    plt.show()

calculate(10000)#試行回数（１００００回）を指定して実行

#3.------------------------------------------

def metoro(n):#n=初期値（0 or 5）
    zero=0#100~110行目 結果記録用変数を定義
    once=0
    twice=0
    three_times=0
    four_times=0
    five_times=0
    six_times=0
    seven_times=0
    eight_times=0
    nine_times=0
    ten_times=0
    count=0#カウンターを定義、最初の１０００個の切り捨てに使用

    for a in range(11000):#確率分布生成用１００００個+切り捨て用の１０００個の合計
        count+=1#現在の試行回数のカウント
        t=n#遷移前の値を計算用に保存
        n+=random.choice([-1,1])#nを１個または-1個遷移する
        if n==-1:#n=0のとき-1側に遷移してしまった場合に１側に戻す処理
            n+=2
        elif n==11:#n=0のとき11側に遷移してしまった場合に9側に戻す処理
            n-=2
        a=P(n)/P(t)#確率分布を関数化したP(n)に遷移前、遷移後の値を代入し計算
        #aが１以上の場合。遷移を確定----この時点で次のforループへ--
        if a<1:#aが１以下の場合
            choice = list(range(0,2))#確率aの場合(0)と確率1-aの場合(1)の選択を定義
            w = [a, 1-a]#確率αと確率1-aの重みを定義
            samples = random.choices(choice, weights = w)#1次元１個の配列として出力
            #確率aの場合、遷移決定----この時点で次のforループへ--
            if samples[0]==1:#確率1-aの場合、同じ状態に遷移する（遷移しない）
                n=t

        if n==0 and count>1000:#133~１５４行目 初めの１０００個を切り捨てカウント
            zero+=1
        elif n==1 and count>1000:
            once+=1
        elif n==2 and count>1000:
            twice+=1
        elif n==3 and count>1000:
            three_times+=1
        elif n==4 and count>1000:
            four_times+=1
        elif n==5 and count>1000:
            five_times+=1
        elif n==6 and count>1000:
            six_times+=1
        elif n==7 and count>1000:
            seven_times+=1
        elif n==8 and count>1000:
            eight_times+=1
        elif n==9 and count>1000:
            nine_times+=1
        elif n==10 and count>1000:
            ten_times+=1

    print(zero)#156~166行目結果表示
    print(once)
    print(twice)
    print(three_times)
    print(four_times)
    print(five_times)
    print(six_times)
    print(seven_times)
    print(eight_times)
    print(nine_times)
    print(ten_times)

    left = np.array([0,1,2,3,4,5,6,7,8,9,10])#168~177行目matplotlibでヒストグラム
    height = np.array([zero,once,twice,\
    three_times,four_times,five_times,\
    six_times,seven_times,eight_times,\
    nine_times,ten_times])
    plt.plot(left, height)
    plt.title('Probability distribution')
    plt.xlabel('Number of front')
    plt.ylabel('Percentage of front')
    plt.show()

metoro(0)#初期値0
metoro(5)#初期値5
