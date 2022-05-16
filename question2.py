# 問2
# 第n項までのフィボナッチ数列の和を計算するプログラムを作成せよ
# - ポイント
# 正直ネット上にたくさん情報があるのでできれば調べずにやってみよう。
pre_1 = 0
num = 1
sum = 0
n = 15

sum += num #一回目の足し算
for i in range(1, n):
  esc = num
  num = pre_1 + num
  pre_1 = esc
  print(num)
  sum += num

print(num)
print(sum)