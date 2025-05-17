import androidhelper as an
import sys,os
d=an.Android()
myname=sys.argv[0]
# word_str=sys.argv[1]
# words_len=len(sys.argv)
sentence="";num=0
for word in sys.argv:
    if word==myname:
        continue
    sentence=sentence+" "+str(word);num+=1
d.ttsSpeak(sentence)
d.dialogCreateAlert('读句子',sentence)
d.dialogSetPositiveButtonText("Yes")
#d.dialogSetNegativeButtonText("No")
d.dialogShow()
os.system("sleep 1")
print("read_txt.py:"+sentence)
print("total:"+str(num))