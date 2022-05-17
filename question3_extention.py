# 問3
# 2人でビンゴゲームをやる。ビンゴのマス目は3×3で数字は1～40とする。 -> マス目の三倍にした．なんか普通のビンゴがそうらしい．ランダムに数字が一つずつ番号をあけていくとき、どちらかがビンゴになったタイミングで勝者を出力するプログラムを作成せよ。
from operator import truediv
from os import remove
from pickle import FALSE
import random
from traceback import print_tb


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
   
def make_card(length, player_num):
  cards = []
  for i in range(player_num):
    nums = random.sample(range(1, length * length * 3 + 1), k=length ** 2)
    nums.sort()
    card = [ nums[i*length : i * length + length] for i in range(length)]
    cards.append(card)
  return cards

def game_select():
  # length = 3
  # player_num = 2 
  length = "len" 
  player_num = "num" 
  while(type(length) != int):
    try:
      length = int(input('マス目の数を入力してください: '))
    except TypeError:
      print("数値を入力してください")
  while(type(player_num) != int):
    try:
      player_num = int(input('プレイヤー数を入力してください: '))
    except TypeError:
      print("数値を入力してください")
  return length, player_num

def play_game(cards, flags, length):
  player_num = len(flags)
  num_pool = [ i for i in range(1, length * length * 3 + 1)]
  while(True not in flags):
    num = num_pool.pop(int(random.random()*len(num_pool)))
    for i in range(player_num):
      card = cards[i] #ここなんかcards[i]を直接bingoに渡すと上手く動かなかった
      flags[i] = bingo(card) #ビンゴ判定
      for j in range(length):
        for k in range(length):
          if(cards[i][j][k] == num):
            cards[i][j][k] = 0
  return cards, flags

def result(cards, flags, player_num, length):
  for i in(range(player_num)):
    if(flags[i] == True):
      print('win player{0}\n'.format(i))
  for i in(range(player_num)):
    print('player{0}'.format(i))
    for j in(range(length)):
      print(cards[i][j])  
    print('\n')


def main():
  length, player_num = game_select()
  cards = make_card(length, player_num)
  flags = [ False for i in range(player_num)]
  cards, flags = play_game(cards, flags, length)
  result(cards, flags, player_num, length)
  

if( __name__ == '__main__'):
  main()