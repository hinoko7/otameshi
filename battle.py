import random

print("今日はボスを倒してみよう！")

print("--------------")

i_life = 100
boss_life = random.randrange(100, 1000)

print(f"君：{i_life}　　ボス：{boss_life}")

while i_life > 0 or boss_life > 0:
    print("--------------")
    print("攻撃だ！")
    i_attack = random.randrange(10, 100)
    print(f"敵に{i_attack}ダメージ与えた。")
    boss_life -= i_attack
    if boss_life <= 0:
        break
    print("--------------")
    print("反撃だ！")
    boss_attack = random.randrange(1, 100)
    print(f"{boss_attack}ダメージくらった")
    i_life -= boss_attack
    print("--------------")
    if i_life <= 0:
        break
    print(f"君：{i_life}　　ボス：{boss_life}")
    if input("逃げる？　y　n：") == "y":
        break

if i_life <= 0 and boss_life <= 0:
    print("相打ちだ！")
elif boss_life <= 0:
    print("君の勝利だ！！")
elif i_life <= 0:
    print("君の負けだ")
else:
    print("君は逃げ出した！")