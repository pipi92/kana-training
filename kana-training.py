import os, time, random
 
hiraganas={
'あ':'A', 'い':'I', 'う':'U', 'え':'E', 'お':'O',
'か':'KA', 'き':'KI', 'く':'KU', 'け':'KE', 'こ':'KO',
'さ':'SA', 'し':'SHI', 'す':'SU', 'せ':'TE', 'そ':'TO',
'た':'TA','ち':'CHI', 'つ':'TSU', 'て':'TE', 'と':'TO',
'な':'NA', 'に':'NI', 'ぬ':'NU', 'ね':'NE', 'の':'NO',
'は':'HA', 'ひ':'HI', 'ふ':'FU', 'へ':'HE', 'ほ':'HO',
'ま':'MA', 'み':'MI', 'む':'MU', 'め':'ME', 'も':'MO',
'や':'YA', 'ゆ':'YU', 'よ':'YO',
'ら':'RA', 'り':'RI', 'る':'RU', 'れ':'RE', 'ろ':'RO',
'わ':'WA', 'を':'WO', 'ん':'N',  
'が':'GA', 'ぎ':'GI', 'ぐ':'GU', 'げ':'GE', 'ご':'GO',
'ざ':'ZA', 'じ':'JI', 'ず':'ZU', 'ぜ':'ZE', 'ぞ':'ZO',
'だ':'DA', 'ぢ':'DJI', 'づ':'DZU', 'で':'DE', 'ど':'DO',
'ば':'BA', 'び':'BI', 'ぶ':'BU', 'べ':'BE', 'ぼ':'BO',
'ぱ':'PA', 'ぴ':'PI', 'ぷ':'PU', 'ぺ':'PE', 'ぽ':'PO',
'きゃ':'KYA', 'きゅ':'KYU', 'きょ':'KYO',
'しゃ':'SHA', 'しゅ':'SHU', 'しょ':'SHO',
'ちゃ':'CHA', 'ちゅ':'CHU', 'ちょ':'CHO',
'にゃ':'NYA', 'にゅ':'NYU', 'にょ':'NYO',
'ひゃ':'HYA', 'ひゅ':'HYU', 'ひょ':'HYO',
'みゃ':'MYA', 'みゅ':'MYU', 'みょ':'MYO',
'りゃ':'RYA', 'りゅ':"RYU", 'りょ':'RYO',
'ぎゃ':'GYA', 'ぎゅ':'GYU', 'ぎょ':'GYO',
'じゃ':'JA', 'じゅ':'JU', 'じょ':'JO',
'ぢゃ':'JA', 'ぢゅ':'JU', 'ぢょ':'JO',
'びゃ':'BYA', 'びゅ':'BYU', 'びょ':'BYO',
'ぴゃ':'PYA', 'ぴゅ':'PYU', 'ぴょ':'PYO'
}
 
katakanas={
'ア': 'A', 'イ': 'I', 'ウ': 'U', 'エ': 'E', 'オ': 'O',
'カ': 'KA', 'キ': 'KI', 'ク': 'KU', 'ケ': 'KE', 'コ': 'KO',
'サ': 'SA', 'シ': 'SHI', 'ス': 'SU', 'セ': 'SE', 'ソ': 'SO',
'タ': 'TA', 'チ': 'CHI', 'ツ': 'TSU', 'テ': 'TE', 'ト': 'TO',
'ナ': 'NA', 'ニ': 'NI', 'ヌ': 'NU', 'ネ': 'NE', 'ノ': 'NO',
'ハ': 'HA', 'ヒ': 'HI', 'フ': 'FU', 'ヘ': 'HE', 'ホ': 'HO',
'マ': 'MA', 'ミ': 'MI', 'ム': 'MU', 'メ': 'ME', 'モ': 'MO',
'ヤ': 'YA', 'ユ': 'YU', 'ヨ': 'YO',
'ラ': 'RA', 'リ': 'RI', 'ル': 'RU', 'レ': 'RE', 'ロ': 'RO',
'ワ': 'WA', 'ヲ': 'WO', 'ン': 'N',
'ガ': 'GA', 'ギ': 'GI', 'グ': 'GU', 'ゲ': 'GE', 'ゴ': 'GO',
'ザ': 'ZA', 'ジ': 'JI', 'ズ': 'ZU', 'ゼ': 'ZE', 'ゾ': 'ZO',
'ダ': 'DA', 'ヂ': 'DJI', 'ヅ': 'DZU', 'デ': 'DE', 'ド': 'DO',
'バ': 'BA', 'ビ': 'BI', 'ブ': 'BU', 'ベ': 'BE', 'ボ': 'BO',
'パ': 'PA', 'ピ': 'PI', 'プ': 'PU', 'ペ': 'PE', 'ポ': 'PO',
'キャ': 'KYA', 'キュ': 'KYU', 'キョ': 'KYO',
'シャ': 'SHA', 'シュ': 'SHU', 'ショ': 'SHO',
'チャ': 'CHA', 'チュ': 'CHU', 'チョ': 'CHO',
'ニャ': 'NYA', 'ニュ': 'NYU', 'ニョ': 'NYO',
'ヒャ': 'HYA', 'ヒュ': 'HYU', 'ヒョ': 'HYO',
'ミャ': 'MYA', 'ミュ': 'MYU', 'ミョ': 'MYO',
'リャ': 'RYA', 'リュ': 'RYU', 'リョ': 'RYO',
'ギャ': 'GYA', 'ギュ': 'GYU', 'ギョ': 'GYO',
'ジャ': 'JA', 'ジュ': 'JU', 'ジョ': 'JO',
'ヂャ': 'JA', 'ヂュ': 'JU', 'ヂョ': 'JO',
'ビャ': 'BYA', 'ビュ': 'BYU', 'ビョ': 'BYO',
'ピャ': 'PYA', 'ピュ': 'PYU', 'ピョ': 'PYO'
}
 
def practice(kana):
    
    corrects=0
    mistakes=0
    
    l=list(kana.items())
    random.shuffle(l)
    mixed_kanas=dict(l)
    
    for k,v in mixed_kanas.items():
        os.system('clear')
        print("Practice Room - type 'x' to exit")
        print(f"Corrects: {corrects}")
        print(f"Mistakes: {mistakes}")
        answer=input(f"{k}: ")
        if answer.upper()==v:
            corrects+=1
            print("Correct!")
            time.sleep(1)
        elif answer.upper()=='X':
            break
        else:
            mistakes+=1
            print(f"Oops! It's {v}")
            time.sleep(1)
    
    
option = "x"    
while option != "0":
    os.system('clear')
    print("Kana Learning Tool\n")
    print("1 - Show Hiragana\n")
    print("2 - Show Katakana\n")
    print("3 - Practice Hiragana\n")
    print("4 - Practice Katakana\n")
    print("0 - Quit\n")
    option=input("Choose an option: ")
    if option=="1":
        input(hiraganas)
    elif option=="2":
        input(katakanas)
    elif option=="3":
        practice(hiraganas)
    elif option=="4":
        practice(katakanas)
