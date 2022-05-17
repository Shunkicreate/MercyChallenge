# 問3
# 2人でビンゴゲームをやる。ビンゴのマス目は3×3で数字は1～40とする。ランダムに数字が一つずつ番号をあけていくとき、どちらかがビンゴになったタイミングで勝者を出力するプログラムを作成せよ。
from operator import truediv
from os import remove
from pickle import FALSE
import random
from traceback import print_tb


# #dirction 上:0 右:3 下:2 左:1
# def serch0(card:list, index: int, dir: int):
#   if(dir == 1 or dir == 3):
#     try:
#       next_index = index + dir - 2
#     except(IndexError):
#       return False
#     num = card[next_index]
#     if(num) == 0:
#       serch0(card, next_index, dir)
#     return False
#   elif(dir == 0 or dir == 2):
#     try:
#       next_index = index + (dir - 1)* len(card)
#     except(IndexError):
#       return True
#     num = card[next_index]
#     if(num) == 0:
#       serch0(card, next_index, dir)
#     return True
#   return False

# def bingo(card: list):
#   dir = 0
#   for i in card:
#     if(i == 0): #0の場所を探す
#       for j in range(4):
#         if(serch0(card, dir, j)):
#           print('bingo')
#           break

def bingo(card:list):
  length = len(card)
  #横判定
  for i in range(length):
    for j in range(length):
      if(card[i][j] != 0):
        break
      elif(j + 1 == length):
        return True
  #縦判定
  for i in range(length):
    for j in range(length):
      if(card[j][i] != 0):
        break
      elif(j + 1 == length):
        return True
  #斜め判定
  for j in range(length):
    if(card[j][j] != 0):
      break
    elif(j + 1 == length):
      return True
  for j in range(length):
    if(card[length - j - 1][j] != 0):
      break
    elif(j + 1 == length):
      return True
  return False
        
    # print(card(i))
def main(length):
  p1 = [[int(random.random()*39 + 1) for j in range(length)] for i in range(length)]
  p1.sort()
  p2 = [[int(random.random()*39 + 1) for j in range(length)] for i in range(length)]
  p2.sort()
  # p2 = [[0 for j in range(3)] for i in range(3)]
  flagp1 = False
  flagp2 = False
  while(flagp1 == False and flagp2 == False):
    flagp1 = bingo(p1)
    flagp2 = bingo(p2)
    num = int(random.random()*39 + 1)
    for i in range(length):
      for j in range(length):
        if(p1[i][j] == num):
          p1[i][j] = 0
          print('nice player1!')
          if(p2[i][j] == num):
            p2[i][j] = 0
            print('nice player2!')
            break
        if(p2[i][j] == num):
          p2[i][j] = 0
          print('nice player2!')
        
  if(flagp1):
    print('win player1')

  else:
    print('win player2')

  for i in(range(length)):
    print(p1[i])
  print("\n")
  for i in(range(length)):
    print(p2[i])
      
if( __name__ == '__main__'):
  length = 3
  main(length)