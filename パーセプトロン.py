print('AIに2(A+B)の計算をさせます。')
import sys
import numpy as np
import random
import time
from tqdm import tqdm

def soroe(x):
    return round(x)

def AND(a, b):
    if a + b == 2:
       return 1
    else:
       return 0

def Relu(x):
    if 0 < x:
       return x
    else:
       return 0

def ze(g):
    if 0 < g:
       return g
    else:
       return g * -1

def AI(a, c):
    return soroe(Relu(w1 * a + w2 * c + b))

def jyun(a, c):
    return Relu(w1 * a + w2 * c + b)

d = 'y'
n = 0
z = 0
w1 = 0
w2 = 0
b = 0
s = 0
a = 0.0001
p = 0
st = time.time()
print('学習中...')
for s in tqdm(range(1000000)):
      x1 = random.randint(0, 100)
      x2 = random.randint(0, 100)
      y = jyun(x1, x2)
      t = (x1 + x2) * 2
      w1 = w1 + (t - y) * a * x1
      w2 = w2 + (t - y) * a * x2
      b = b + (t - y) * a
      p = p + ze((t - y))
      if (s + 1) % 1000 == 0:
         ph = p / 1000
         p = 0
print("学習完了!")
print("誤差平均 =",ph)
tm = time.time() - st
print('学習時間',tm,'sec')
while d == 'y':
      n = int(input('AをAIに入力 >>'))
      if 0 > n :
         print('負の数は入力しないで下さい。')
      else:
         z = int(input('BをAIに入力 >>'))
         if 0 > z :
            print('負の数は入力しないで下さい。')
         else:
            print('結果',AI(n,z))
            if AI(n,z) == 2*(n+z):
               print('AIは正解しました')
            else:
               print('AIは間違えました')
      d = input('続けますか(y/n):')
      while d != 'y' and d != 'n':
         d = input('yかnで指定して下さい:')
         
         
