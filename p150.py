import sys
if len(sys.argv)<2:
    print('表示したい名前を指定してください。')
    sys.exit()
my_name=sysargv[1]
#計算結果の表示メッセージ
kitchen_message=my_name+'さんの最適なキッチンの高さ(そのn)は'
try:
    except ValueError as e:
        print('身長または今のキッチンの高さを見直してください。')
        print(e)
    except:
        import traceback
        traceback.print_exc()