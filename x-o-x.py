import random

masa = ["_","_","_","_","_","_","_","_","_"]  
kazanan = None

current_player = "X"
gamerunning = True

def printmasa(masa):
    print(masa[0],"|",masa[1],"|",masa[2])
    print("---------")
    print(masa[3],"|",masa[4],"|",masa[5])
    print("---------")
    print(masa[6],"|",masa[7],"|",masa[8])
    

def oyuncu_girdi(masa):
    inp = int(input("1-9 arasi bir sayi giriniz"))
    if inp >=1 and inp <=9 and masa[inp-1]=="_":
        masa[inp-1] = current_player
    else:
        print("Bos bir yer seciniz")

def dikey_kontrol(masa):
    if masa[0] ==masa[3]==masa[6] and masa[0]!= "_":
        kazanan=masa[0]
        return True
    elif masa[1]==masa[4]==masa[7] and  masa[1]!="_":
        kazanan=masa[1]
        return True
    elif masa[2]==masa[5]==masa[8] and masa[2]!="_":
        kazanan=masa[2]
        return True

def yatay_kontrol(masa):
    if masa[0]==masa[1]==masa[2] and masa[0] !="_":
        kazanan=masa[0]
        return True
    elif masa[3]==masa[4]==masa[5] and masa[3] !="_":
        kazanan=masa[3]
        return True
    elif masa[6]==masa[7]==masa[8] and masa[6]!="_":
        kazanan=masa[6]
        return True

def capraz_kontrol(masa):
    if masa[0]==masa[4]==masa[8] and masa[0] !="_":
        kazanan=masa[0]
        return True
    elif masa[2]==masa[4]==masa[6] and masa[2]!="_":
        kazanan=masa[2]
        return True

def berabere_mi(masa):
    global gamerunning
    if "_" not in masa:
        printmasa(masa)
        print("Berabere")
        gamerunning = False

def oyuncu_degis():
    global current_player
    if(current_player=="X"):
        current_player="O"
    else:
        current_player="X" 

def checkwin():
    global gamerunning
    if dikey_kontrol(masa) or yatay_kontrol(masa) or capraz_kontrol(masa):
        print(f"Kazanan oyuncu {current_player} Tebrikler")
        gamerunning = False
    
def bilgisayar(masa):
    while current_player == "O":
        position = random.randint(0,8)
        if masa[position] == "_":
            masa[position] = "O"
            oyuncu_degis()


while gamerunning:
    printmasa(masa)
    oyuncu_girdi(masa)
    printmasa(masa)
    checkwin()
    berabere_mi(masa)
    oyuncu_degis()
    bilgisayar(masa)
    printmasa(masa)
    checkwin()
    berabere_mi(masa)
    
