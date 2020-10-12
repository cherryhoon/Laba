from math import sqrt
a = int(input())
m = []
m.append(a)
max = a
min = a
g = 0
while a != "End":
  a = input()
  if a != "End":
    m.append(a)
k = len(m)
for i in m:
  g += int(i)
  if int(i)> max
     max = int(i)
  if int(i)< min
    min = int(i)
avg = g/k
s = 0
for i in m:
  s += (int(i) - avg)**2
stdev = sqrt(s/k)
print('Максимум',max)
print('Минимум',min)
print('Среднее',avg)
print('Среднеквадратичное',round(stdev,3))