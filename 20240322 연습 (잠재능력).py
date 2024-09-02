# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:24:47 2024

@author: 김수연
"""
# random함수를 이용해 메이플스토리의 잠재능력 설정 구현
# 등업 확률 레어>에픽 50% 에픽>유니크 40% 유니크>레전드리 30% (상황의 빠른 발현 위해 높게 설정)


import random
import sys

list_rank = ["레어","에픽","유니크","레전드리"]
list_item = ["장갑", "모자", "신발", "무기"]

data_glove = ["str", "lck", "int", "dex" , "크리티컬 데미지"]
data_hat = ["str", "lck", "int", "dex", "쿨타임 감소"]
data_shoes = ["str", "lck", "int", "dex"]
data_weapon = ["str", "lck", "int", "dex" , "공격력", "마력"]

rare = [1,1,1,1,3]
epic = [3,3,3,3,6]
unique = [6,6,6,6,9]
regend = [9,12]
cri = 8
cool = [1,2]



pres_1 = random.randint(1,100)

rank = list_rank[0]

item_in = input(f"잠재능력을 설정할 아이템을 선택하시오 {list_item} : ")


check = input(f"{item_in}의 잠재능력을 설정하시겠습니까? (Y/N) : ")



if check in ["Y", "y"] :
    if item_in == list_item[0] :
        data1 = random.choice(data_glove[0:4])
        data_1 = f"{data1} {rare[4]}%"
        data2 = random.choice(data_glove[0:4])
        data_2 = f"{data2} {random.choice(rare)}%"
        data3 = random.choice(data_glove[0:4])
        data_3 = f"{data3} {random.choice(rare)}%"
        print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
    if item_in == list_item[1] :
        data1 = random.choice(data_hat[0:4])
        data_1 = f"{data1} {rare[4]}%"
        data2 = random.choice(data_hat[0:4])
        data_2 = f"{data2} {random.choice(rare)}%"
        data3 = random.choice(data_hat[0:4])
        data_3 = f"{data3} {random.choice(rare)}%"
        print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
    if item_in == list_item[2] :
        data1 = random.choice(data_shoes)
        data_1 = f"{data1} {rare[4]}%"
        data2 = random.choice(data_shoes)
        data_2 = f"{data2} {random.choice(rare)}%"
        data3 = random.choice(data_shoes)
        data_3 = f"{data3} {random.choice(rare)}%"
        print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")        
    if item_in == list_item[3] :
        data1 = random.choice(data_weapon)
        data_1 = f"{data1} {rare[4]}%"
        data2 = random.choice(data_weapon)
        data_2 = f"{data2} {random.choice(rare)}%"
        data3 = random.choice(data_weapon)
        data_3 = f"{data3} {random.choice(rare)}%"
        print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")              
else :
    print(f"{item_in}의 잠재능력을 설정하지 않습니다.")
    sys.exit()

again = input(f"{item_in}의 잠재능력을 재설정하시겠습니까? (Y/N) : ")

for again in ["N", "n"] :
    if rank == list_rank[0] :
        if pres_1 <= 50 :
            rank = list_rank[1]
            pres_1 = random.randint(1,100)
            if item_in == list_item[0] :
                data1 = random.choice(data_glove[0:4])
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_glove[0:4])
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_glove[0:4])
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[1] :
                data1 = random.choice(data_hat[0:4])
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_hat[0:4])
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_hat[0:4])
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[2] :
                data1 = random.choice(data_shoes)
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_shoes)
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_shoes)
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")        
            elif item_in == list_item[3] :
                data1 = random.choice(data_weapon)
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_weapon)
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_weapon)
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            
        elif  pres_1 > 50 :
            if item_in == list_item[0] :
                pres_1 = random.randint(1,100)
                data1 = random.choice(data_glove[0:4])
                data_1 = f"{data1} {rare[4]}%"
                data2 = random.choice(data_glove[0:4])
                data_2 = f"{data2} {random.choice(rare)}%"
                data3 = random.choice(data_glove[0:4])
                data_3 = f"{data3} {random.choice(rare)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[1] :
                data1 = random.choice(data_hat[0:4])
                data_1 = f"{data1} {rare[4]}%"
                data2 = random.choice(data_hat[0:4])
                data_2 = f"{data2} {random.choice(rare)}%"
                data3 = random.choice(data_hat[0:4])
                data_3 = f"{data3} {random.choice(rare)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[2] :
                data1 = random.choice(data_shoes)
                data_1 = f"{data1} {rare[4]}%"
                data2 = random.choice(data_shoes)
                data_2 = f"{data2} {random.choice(rare)}%"
                data3 = random.choice(data_shoes)
                data_3 = f"{data3} {random.choice(rare)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")        
            elif item_in == list_item[3] :
                data1 = random.choice(data_weapon)
                data_1 = f"{data1} {rare[4]}%"
                data2 = random.choice(data_weapon)
                data_2 = f"{data2} {random.choice(rare)}%"
                data3 = random.choice(data_weapon)
                data_3 = f"{data3} {random.choice(rare)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")   
        again = input(f"{item_in}의 잠재능력을 재설정하시겠습니까? (Y/N) : ")
    elif rank == list_rank[1] :
        if pres_1 <= 40 :
            rank = list_rank[2]
            pres_1 = random.randint(1,100)
            if item_in == list_item[0] :
                data1 = random.choice(data_glove[0:4])
                data_1 = f"{data1} {unique[4]}%"
                data2 = random.choice(data_glove[0:4])
                data_2 = f"{data2} {random.choice(unique)}%"
                data3 = random.choice(data_glove[0:4])
                data_3 = f"{data3} {random.choice(unique)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[1] :
                data1 = random.choice(data_hat[0:4])
                data_1 = f"{data1} {unique[4]}%"
                data2 = random.choice(data_hat[0:4])
                data_2 = f"{data2} {random.choice(unique)}%"
                data3 = random.choice(data_hat[0:4])
                data_3 = f"{data3} {random.choice(unique)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[2] :
                data1 = random.choice(data_shoes)
                data_1 = f"{data1} {unique[4]}%"
                data2 = random.choice(data_shoes)
                data_2 = f"{data2} {random.choice(unique)}%"
                data3 = random.choice(data_shoes)
                data_3 = f"{data3} {random.choice(unique)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")        
            elif item_in == list_item[3] :
                data1 = random.choice(data_weapon)
                data_1 = f"{data1} {unique[4]}%"
                data2 = random.choice(data_weapon)
                data_2 = f"{data2} {random.choice(unique)}%"
                data3 = random.choice(data_weapon)
                data_3 = f"{data3} {random.choice(unique)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")

        elif  pres_1 > 40 :
            if item_in == list_item[0] :
                data1 = random.choice(data_glove[0:4])
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_glove[0:4])
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_glove[0:4])
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[1] :
                data1 = random.choice(data_hat[0:4])
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_hat[0:4])
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_hat[0:4])
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
            elif item_in == list_item[2] :
                data1 = random.choice(data_shoes)
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_shoes)
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_shoes)
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")        
            elif item_in == list_item[3] :
                data1 = random.choice(data_weapon)
                data_1 = f"{data1} {epic[4]}%"
                data2 = random.choice(data_weapon)
                data_2 = f"{data2} {random.choice(epic)}%"
                data3 = random.choice(data_weapon)
                data_3 = f"{data3} {random.choice(epic)}%"
                print(f"{item_in}의 잠재능력입니다.\n{rank}등급\n{data_1}\n{data_2}\n{data_3}")
        again = input(f"{item_in}의 잠재능력을 재설정하시겠습니까? (Y/N) : ")  
        

print("잠재능력 설정을 종료합니다.")
sys.exit()
