import androidhelper as an
import sys
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
    w_txt=d.dialogGetInput('听写单词('+str(num)+')','What would you like to write?').result
    print("word_write:"+word)
    if word==w_txt:
        result_w="Answer Right:\nThe word '"+w_txt+"' is "+str(word==w_txt)+"."
    else:
        result_w="Answer Error:\nThe word '"+w_txt+"' is "+str(word==w_txt)+"."
    print("result:"+result_w)