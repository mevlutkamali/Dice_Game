
import random
import os

menu = """
       # MENÜ #
    1 ) 6'lı zar at .
    2 ) 20'li zar at .  
    Q ) Çıkış .
"""

def dice_random() :
    dice = random.randint(1, 6)

    number = int(input(" 1 ile 6  arası rastgele sayı tut : "))
    print(" Gelen zar : ", dice)

    if dice == number:
        print(" Tebrikler sayılarınız aynı :)... ")
        quit()

    else:
        print(" Ne yazıkki sayılarınız eşit değil :(... ")
        input(" Oyuna devam etmek için enter'a tıklayınız . ")

def dice_2_random() :
    dice = random.randint(1, 20)

    number = int(input(" 1 ile 20  arası rastgele sayı tut : "))
    print(" Gelen zar : ", dice)

    if dice == number:
        print(" Tebrikler sayılarınız aynı :)... ")
        quit()

    else:
        print(" Ne yazıkki sayılarınız eşit değil :(... ")
        input(" Oyuna devam etmek için enter'a tıklayınız . ")

def exitt() :
    print(" Bizi terçih ettiğiniz için teşekkürler . ")
    quit()

def warning() :
    print(" Hatalı giriş yaptınız ! \n Uygulamayı yeniden başlatınız . ")
    quit()

print(menu)
vote = input(" Lütfen seçim yapınız : ")

while True :

    os.system("cls")

    if vote == "1" :
        dice_random()

    elif vote == "2" :
        dice_2_random()

    elif vote == "Q" or vote == "q" :
        exitt()

    else :
        warning()

