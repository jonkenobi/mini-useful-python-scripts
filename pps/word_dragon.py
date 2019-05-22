''' word dragon game'''
import time

print("ようこそしりとりゲーム")
word = 'しりとり'
while True:
    entered_word = input("Enter a word that starts with the last letter of {}:".format(word)).lower()
    #exit 入力されたらexit
    if entered_word == 'exit':
        break
    if len(entered_word)<=2:
        print("3文字以上入力してください")
        pass
    if word[-1] == entered_word[0]:
        word = entered_word
        #最後の文字が「ー」だったら
         # if entered_word[-1] == '-':
    else:
        print("that doesn't start with {} !".format(word[-1]))
    
        
    #最後の文字が　ん　だったら
    if entered_word[-1] == 'ん':
        print("負け!!!")
        ans = input("もう一回やる?（y/n)").lower()
        
    #exit game 
        if ans in ['いいえ','n','ｎ','no'] :
            print('ゲームを終了します')
            time.sleep(1)
            break
        #new game
        else:
            word = 'しりとり'
            continue
        
