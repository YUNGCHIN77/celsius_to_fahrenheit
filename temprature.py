#攝氏('C)轉換成華氏('F)程式
#讓使用者輸入 攝氏溫度
#然後印出華氏溫度

celsius = float(input("請輸入攝氏溫度："))
fahrenheit = round(celsius * 9 / 5 + 32, 2)
print("華氏溫度為：", fahrenheit)