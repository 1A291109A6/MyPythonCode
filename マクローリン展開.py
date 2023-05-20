import sys
sys.setrecursionlimit(5000)
s = 1
o = 1
def k(n):
    if n == 1:
       return n
    else:
       return n * k(n-1)

print("計算中...")

while s < 1000:
      o = o + 1 / k(s)
      s = s + 1

print("計算が終了しました。")
print("結果を表示します。")
print("e","(ネイピア数)","は、",o,"です。")
print("これは、マクローリン展開で計算した結果です。")
print("ありがとうございました。")
a = input()
