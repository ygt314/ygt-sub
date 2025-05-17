from translate import Translator
import androidhelper as an
import sys,os
d=an.Android()
myname=sys.argv[0]
#word_str=sys.argv[1]
#words_len=len(sys.argv)
num=0
for word in sys.argv:
    if word==myname:
        continue
    num+=1
#input("from_text:")
    print("trans.py:",word)
    lang1="English" #input("from_lang:")
    lang2="Chinese" #input("to_lang:")
    trans_all=Translator(from_lang = lang1.capitalize(), to_lang=lang2.capitalize())
    text_to=trans_all.translate(word)
    d.dialogCreateAlert('翻译('+str(num)+')',word+":"+text_to)
    d.dialogSetPositiveButtonText("Yes")
    #d.dialogSetNegativeButtonText("No")
    d.dialogShow()
    print("mean:",text_to)