import random
import time
from tqdm import tqdm
s = 0
x = 0
y = 0
o = 0
円内 = 0
円周率 = 0
n = int(input("何回計算しますか>>"))
tmb = time.time()
for s in tqdm(range(n)):
    x = random.randint(0,1000000000000) / 1000000000000
    y = random.randint(0,1000000000000) / 1000000000000
    o = (x**2 + y**2)**0.5
    if o < 1:
        円内 = 円内 + 1
    円周率 = 円内 / (s + 1) * 4
print("円周率 =", 円周率)
print("計算時間:",str(time.time() - tmb),"sec")
print("END")
a = input()
