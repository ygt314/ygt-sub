'''
文章数学:个性化解答展示
结构:信息头_方案_答案
注释:万能(::#),信息头和答案中(:#)
信息头:已知(i:)_问题(q:),均+python字符串
加载第三方py库(p:),使用py库加载写法
mymath为常驻库无需声明
定义(dn:)+python表达式,d_s为定义个数
方案:(py脚本语言)方法+::+(py字符串)回应
答案:(reply:)+py字符串
格式化公式(print:)+py表达式
例:(证明:1+1<3)(test.txt)
#head
q:1+1<3;sin(30°)
p:import math
d_s:1
d1:pi=math.pi
#way
c=1+1::1+1={c}
ans1=(c<3)::2<3 is {ans1}
ans2=math.sin(pi/6)::sin(30°)=1/2
#answer
reply:{ans1},{ans2}
(控制台输出)求:1+1<3;sin(30°)?
step1:1+1=2
step2:2<3 is True
step3:sin(30°)=1/2
答:True,0.5.
'''
#常驻库
from mymath import *
# 按行解析数学文本内容
def parse_math_text(text):
    lines = text.strip().split('\n')
    head_info = {'i':'','q':'','d_s':'0','p':'0'}
    way_info = {}
    answer_info = {}
    current_section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#head'):
            current_section = 'head'
        elif line.startswith('#way'):
            current_section = 'way'
        elif line.startswith('#answer'):
            current_section = 'answer'
        else:
            if current_section == 'head':
                key, value = line.split(':', 1)
                head_info[key] = value
            elif current_section == 'way':
                key, value = line.split(':', 1)
                way_info[key] = value[1:]
            elif current_section == 'answer':
                key, value = line.split(':', 1)
                answer_info[key] = value
    return head_info, way_info, answer_info

# 解题
def exec_way(answer_info,way_info,hd_i=[]):
    local_ns = locals()
    global_ns = globals()
    for port in ["0",hd_i[0],"p"]:
        if port=="p":
            print("解:"+' '*5)
        elif port=="0":
            print("[Ready]",end="\r")
        else:
            exec(port, global_ns, global_ns)
    for d_d in hd_i[1:]:
        exec(d_d, global_ns, global_ns)
    stepn=1
    for key, value in way_info.items():
        exec(key, global_ns, local_ns);print(f"step{stepn}",end=":")
        exec(f"print(f'{value}')", global_ns, local_ns)
        stepn+=1
    return eval(f"f'{answer_info}'", global_ns, local_ns), local_ns

# 生成问题与回答
def ques_txt(quet,hhh=""):
    q_s=f"已知{hhh}，" if len(hhh)>1 else ""
    return f"{q_s}求{quet}？"
def answer_txt(result):
    return f"答:{result}."

# 一触即发
def get_run(text):
    # 解析文本
    head, way, answer = parse_math_text(text)
    # 问题
    print(ques_txt(head['q'],head['i']))
    # 导入头信息，执行方法
    d_s=[head[f'd{i+1}'] for i in range(0,int(head['d_s']))]
    hd_if=[head['p']]+d_s #库信息前置
    result=exec_way(answer['reply'],way,hd_if)
    # 回答
    print(answer_txt(result[0]))
    # 格式化公式
    if 'print' in answer:
        import sympy as sm
        sm.pprint(eval(answer["print"],result[1]))

# 示例文本
demo_txt='''
#head
q:1+1<3;sin(30°)
p:import math
d_s:1
d1:pi=math.pi
#way
c=1+1::1+1={c}
ans1=(c<3)::2<3 is {ans1}
ans2=math.sin(pi/6)::sin(30°)=1/2=0.5
#answer
reply:{ans1},{ans2}
'''
if __name__=="__main__":
    head, way, answer = parse_math_text(demo_txt)
    print("head信息:", head)
    print("way信息:", way)
    print("answer信息:", answer)
    d_s=[head[f'd{i+1}'] for i in range(0,int(head['d_s']))]
    hd_if=[head['p']]+d_s
    result = exec_way(answer['reply'],way,hd_if)
    print("way中变量计算结果:", result)