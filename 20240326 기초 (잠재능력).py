import random
import sys

list_rank = ["레어","에픽"]
item = "신발"

data_shoes = ["str", "lck", "int", "dex"]

pres = random.randint(1,100)

rare = [1,1,1,1,3]
epic = [3,3,3,3,6]

a = input(f"{item}의 능력을 설정하시겠습니까?")

if a in ["Y", "y"] :
    rank = list_rank[0]
    data1 = random.choice(data_shoes)
    data_1 = f"{data1} {rare[4]}%"
    data2 = random.choice(data_shoes)
    data_2 = f"{data2} {random.choice(rare)}%"
    print(f"{rank}등급\n{data_1}\n{data_2}")
    b = input("잠재능력을 재설정할까요? ")

else : 
    print("잠재능력을 설정하지 않습니다.")    
    sys.exit()
    
    
while b in ["y", "Y"] :    
    if rank == list_rank[0]:
        if pres <= 50 :
            pres = random.randint(1,100)
            rank = list_rank[1]
            data1 = random.choice(data_shoes)
            data_1 = f"{data1} {epic[4]}%"
            data2 = random.choice(data_shoes)
            data_2 = f"{data2} {random.choice(epic)}%"
            print(f"{rank}등급\n{data_1}\n{data_2}")
        else :
            pres = random.randint(1,100)
            rank = list_rank[0]
            data1 = random.choice(data_shoes)
            data_1 = f"{data1} {rare[4]}%"
            data2 = random.choice(data_shoes)
            data_2 = f"{data2} {random.choice(rare)}%"
            print(f"{rank}등급\n{data_1}\n{data_2}")
    elif rank == list_rank[1] :
        data1 = random.choice(data_shoes)
        data_1 = f"{data1} {epic[4]}%"
        data2 = random.choice(data_shoes)
        data_2 = f"{data2} {random.choice(epic)}%"
        print(f"{rank}등급\n{data_1}\n{data_2}")    
    
    b = input("잠재능력을 재설정할까요? ")

    
print("잠재능력 설정을 종료합니다.")
sys.exit()