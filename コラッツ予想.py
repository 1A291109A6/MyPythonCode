print("コラッツ予想を確かめます。")
a = int(input("値を入力してください>>"))
print(a)
print("|")
while a != 1:
    if a % 2 == 0:
        a = a / 2
    else:
        a = a * 3 + 1
    print(a)
    if a != 1:
        print("|")
print("END")
b = input()
