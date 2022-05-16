# 問1
# りゅうのすけはストラックアウトでしゅんきくんと対戦しました。
# ストラックアウトは9マスで左上から順に123456789と並んでいます。
# 得点はマス目の数で同じマス目は1回のみ得点になります。
# 10回ランダムにミスアリで投げた時勝者とそれぞれの得点を出力するプログラムを作成せよ。
import random
def select():
  num = int(random.random()*10)
  return num

ryunosuke = [i+1 for i in range(10)]
shunki = [i+1 for i in range(10)]
ryunosuke_score = []
shunki_score = []
for i in range(10):
  shot = select()
  shunki[shot] = 0
  shot = select()
  ryunosuke[shot] = 0

print("ryunosuke: ", 45 - sum(ryunosuke))
print("shunki: ", 45 - sum(shunki))