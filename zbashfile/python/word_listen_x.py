import androidhelper as an
import sys,os
d=an.Android()
myname=sys.argv[0]
# word_str=sys.argv[1]
# words_len=len(sys.argv)
num=0
for word in sys.argv:
    if word==myname:
        continue
    num+=1
    d.ttsSpeak(word)
    os.system("sleep 0.5")
    print(myname+":"+word)