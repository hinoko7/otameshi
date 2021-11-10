me = 1
you = 1
count = 0

def attack():
    number = 1
    return number

def superattack():
    number = 1000
    return number

while me >= 1 and you >= 1:
    action = input("1:ため　2:攻撃　3:ため攻撃　4:バリア　")

    if action == "1":
        count += 1
    elif action == "2" and count >= 1:
        print("相手に攻撃!")
        count -= 1
        a = attack()
        you -= a
    elif action == "3" and count >= 3:
        print("スーパー攻撃だ!")
        count -= 3
        a = superattack()
        you -= a
    elif action == "4":
        pass
    
    print(f"me:{count}  you:count")

if you <= 0:
    print("you win!")
elif me <= 0:
    print("you lose")