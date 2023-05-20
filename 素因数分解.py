import time
print('指定した数値を素因数分解をします。')
a = 1
Alist = []
new = 2
msg = ''
jyou = 1
teigi = 1
hozonn = 0
import sys
def bunkai(n):
    global new
    global a
    if not n < 2 and n % 1 == 0:
        while n ** 0.5 >= new:
            if n % new == 0:
                Alist.append(new)
                bunkai(n / new)
                return Alist
                sys.exit()
            new += a
            a = 2
        Alist.append(n)

def kekka(x):
    global new
    global a
    global Alist
    global msg
    global hozonn
    a = 1
    Alist = []
    new = 2
    hozonn = bunkai(x)
    if len(hozonn) == 1:
        return hozonn[0]
    else:
        return hennkann(hozonn)
    

def hennkann(n):
    global msg
    global jyou
    global teigi
    global Alist
    msg = ''
    jyou = 1
    teigi = 0
    n.append(0)
    while not len(n) < teigi + 2:
        if n[teigi] == n[teigi + 1]:
            jyou += 1
        else:
            msg += str(n[teigi])
            if not jyou == 1:
                msg += '^' + str(jyou)
            if not teigi + 2 == len(n):
                msg += '×'
            jyou = 1
        teigi += 1
    return msg

d = 'y'
while d == 'y':
      n = int(input('素因数分解する数値を入力>>'))
      if not 2 <= n :
         print('エラーが発生しました。')
      else:
        befor = time.time()
        print('結果',kekka(n))
        print('かかった時間',str(time.time() - befor),'sec')
        now = 0
        awase = 1
        while len(Alist) > now + 1:
            now += 1
            awase *= Alist[now - 1]
        if n == awase:
            print('間違いはありません。')
        else:
            print('間違いがあります。')
      d = input('続けますか(y/n):')
      while d != 'y' and d != 'n':
         d = input('yかnで指定して下さい:')
      if d == 'y':
          print()

