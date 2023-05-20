from tqdm import tqdm
ba = 1
bb = 1 / 2 ** 0.5
bt = 1 / 4
bp = 1

print('ガウス＝ルジャンドルのアルゴリズムを使って円周率を計算します。')
print('↓には1024以内の値を入力して下さい。')
n = int(input('何回計算しますか >>'))
for i in tqdm(range(n)):
    aa = (ba + bb) / 2
    ab = (ba * bb) ** 0.5
    at = bt - bp * (ba - aa) ** 2
    ap = bp * 2
    ba = aa
    bb = ab
    bt = at
    bp = ap

print('結果','π =',str((aa + ab) ** 2 / (4 * at)))
a = input()
