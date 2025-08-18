import random

omikuji = ["大吉", "中吉", "小吉", "凶"]
result = random.choice(omikuji)

if result == "大吉":
    print("おめでとう！大吉です！")
elif result == "中吉":
    print("中吉です。まずまずですね。")
elif result == "小吉":
    print("小吉です。気を引き締めましょう。")
else:
    print("凶です。注意して過ごしましょう。")
