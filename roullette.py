import random
import time
import os

gam = 1
fir = 0
second = 0
thi = 0
re = 1
ran = 0
money = 15000
X_1 = 0
item = 0
CHIL_Up = 0
two = 1000
pat = 5
X_2 = 0
pri = 5000
test = 0
X_money = 0
O_money = 0
P_money = - 2000
F_money = 0

while gam == 1 :
  P_money = P_money + 1000
  if X_money >= 1 :
    F_money = X_money
    money = money - int(F_money*0.05)
    F_money = F_money * 0.1
    X_money = X_money + int(F_money)
  re = 0
  money = money - 1000 - P_money
  if test != 1:
    if money < 0 :
      print("거어어어지 ㄱㅇ")
      quit()
  print("잔액 :", money)
  time.sleep(1.5)
  os.system('cls')
  fir = random.randint(1, 9)
  if X_1 == 1 :
    fir = random.randint(2, 9)
  if X_2 == 1 :
    fir = random.randint(2, 9)
  if CHIL_Up == 1 :
    if fir == 1 :
      fir = 7
    if X_2 == 1 :
      if fir == 2 :
        fir = 7
  second = random.randint(1, 9)
  if X_1 == 1 :
    second = random.randint(2, 9)
  if X_2 == 1 :
    second = random.randint(2, 9)
  if CHIL_Up == 1 :
    if second == 1 :
      second = 7
    if X_2 == 1 :
      if second == 2 :
        second = 7
  thi = random.randint(1, 9)
  if X_1 == 1 :
    thi = random.randint(2, 9)
  if X_2 == 1 :
    thi = random.randint(2, 9)
  if CHIL_Up == 1 :
    if thi == 1 :
      thi = 7
    if X_2 == 1 :
      if thi == 2 :
        thi = 7
  while re <= 7 :
    ran = random.randint(1, 9)
    print(ran, end = '')
    print(" | ", end = '')
    ran = random.randint(1, 9)
    print(ran, end = '')
    print(" | ", end = '')
    ran = random.randint(1, 9)
    print(ran, end = '')
    re = re + 1
    time.sleep(0.1)
    os.system('cls')
  re = 0
  while re <= 3 :
    print(fir, end = '')
    print(" | ", end = '')
    ran = random.randint(1, 9)
    print(ran, end = '')
    print(" | ", end = '')
    ran = random.randint(1, 9)
    print(ran, end = '')
    re = re + 1
    time.sleep(0.1)
    os.system('cls')
  re = 0
  while re <= 3 :
    print(fir, end = '')
    print(" | ", end = '')
    print(second, end = '')
    print(" | ", end = '')
    ran = random.randint(1, 9)
    print(ran, end = '')
    re = re + 1
    time.sleep(0.1)
    os.system('cls')
  print(fir,"|",second,"|",thi)
  time.sleep(0.5)
  if fir == 7 :
    if fir == second :
      if fir == thi :
        print("ㄹㅈㄷ 인생 역전 777 잭팟")
        money = money * pat * 10
        if X_money > 0 :
          print("님은 빛이 있어서 갚고 오세용 ㅋ")
        else :
          print("ㄹㅈㄷ 머찐 엔딩 크래딧")
          quit()
  if fir == 4 :
    if fir == second :
      if fir == thi :
        print("ㄹㅈㄷ 444 잭팟")
        money = 0
  if fir == second :
    if second == thi :
      print("ㄹㅈㄷ 잭팟")
      money = money * pat
    else :
      print("걍 2개 마즘 ㅇㅇ")
      money = money + two
  elif fir == thi :
    print("걍 2개 마즘 ㅇㅇ")
    money = money + two
  elif second == thi :
    print("걍 2개 마즘 ㅇㅇ")
    money = money + two
  print("다시? 1. ㅇ 2. 상점")
  cul = input()
  os.system('cls')
  if cul == '2' :
    print("1. 잭팟 확률 업 5000넌 2. 얻는 돈 업글 ",pri, "넌 3. 대출 4. 갚기 5. 나가기 잔액 :", money, "대출금 :", X_money)
    item = input()
    if item == 1010 :
      test = 1
    if item == '1' :
      if X_1 == 0 :
        X_1 = 1
        print("숫자 1 삭제")
        time.sleep(1.0)
        os.system('cls')
      elif X_1 == 1 :
        X_1 = 2
        CHIL_Up = 1
        print("7 확률 증가")
        time.sleep(1.0)
        os.system('cls')
      elif CHIL_Up == 1 :
        X_2 = 1
        print("숫자 2 삭제")
        time.sleep(1.0)
        os.system('cls')
      money = money - 5000

    if item == '2' :
     two = two + 500
     pat = pat + 2
     print(pri, "원 삭제")
     money = money - pri
     pri = pri + 1000

    if item == '3' :
      while True :
        print("얼마?")
        if X_money > 1000000 :
          print("님은 신용불량자라 못 빌려용")
          break
        X_money = int(input()) 
        money = money + X_money
        print("현재 대출금 :", X_money)
        print("대출금은 10%씩 늘어용")
        print("5%씩 돈도 사려져용")
        break
      time.sleep(1.5)
      os.system('cls')

    if item =='4' :
      while True :
        print("얼마나?")
        O_money = int(input())
        if O_money > money :
          print("???? ㅗㅗㅗㅗㅗ")
          time.sleep(1.0)
          os.system('cls')
          continue
        else :
          if O_money > X_money :
            money = money - X_money
            X_money = 0
          else :
            money = money - O_money
            X_money = X_money - O_money
          break


    elif item == '5' :
      continue