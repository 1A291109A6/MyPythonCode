from time import sleep
print("何秒間増やしますか?")
n = int(input())

while n < 0:
    print(">>マイナスにならないようにして下さい!!")
    n = int(input())

print()
print("最初は何個から始めますか?")
s = round(int(input()))

while s <= 0:
    print(">>0よりも多くして下さい!!")
    s = round(int(input()))

print()
print("描画しますか(y/n)")
j = input()

while j != "y" and j != "n":
    print(">>yかnで指定して下さい!!")
    j = input()

for i in range(-1,round((n - (n % 3)) / 3 - 1)):
    print()
    sleep(3)
    if j == "y":
        print("●" * 2 ** (i + s))
    else:
        print(round(2 ** (i + s)))

print()
print("最終結果:",str(round(2 ** (i + s))),"個")
n = input()
