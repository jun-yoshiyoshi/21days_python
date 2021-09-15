import bmi
#体重と身長を代入
my_weight=55
my_height=1.7
#BMIモジュールを使って計算
my_bmi=bmi.calc(weight=my_weight,height=my_height)
print(my_bmi)
#BMIモジュールを使ってメッセージを選択
bmi_message=bmi.message(my_bmi)
print(bmi_message)