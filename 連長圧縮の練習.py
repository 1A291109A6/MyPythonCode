n = [1,1,1,0,1,1,0]
n_result = []
temp = n[0]
if temp == 1:
    n_result.append(0)
num = 1
for i in range(1,len(n)):
  if n[i] == temp:
    num += 1
  else:
    n_result.append(num)
    num = 1
    temp = n[i]
n_result.append(num)
print(n_result)
