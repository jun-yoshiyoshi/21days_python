my_weight=70 #体重70㎏
my_height=0  #身長0ｍ
try:
    #身長が0以下の場合、割り算できない
    if my_height<=0:
        raise ValueError('身長が正しくありません。')
    #BMI=体重[kg]÷(身長[m]×身長[m])
    my_bmi=my_weight/(my_height*my_height)
    print('あなたのBMI値は{my_bmi}です。')
except ValueError as e:
    print('体重を見直してください。')
    print(e)
except:
    import traceback
    traceback.print_exc() 