# 問2
# 第n項までのフィボナッチ数列の和を計算するプログラムを作成せよ
# - ポイント
# 正直ネット上にたくさん情報があるのでできれば調べずにやってみよう。
pre_1 = 1
pre_2 = 0
num = 1
sum = 0
n = 10
for i in range(n):
  print(num)
  num = pre_1 + pre_2
  pre_2 = pre_1
  pre_1 = num
  sum += num

print(num)
print(sum)