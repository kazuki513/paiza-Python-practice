import random

damage = random.randint(10, 100)  # ランダムダメージ
print(f"攻撃力: {damage}")

if damage >= 80:
    print("クリティカルヒット！")
elif damage >= 50:
    print("良いダメージ！")
else:
    print("通常ダメージです")
