from mymath import *
import sys
from math_adapter import set_pypynum_output

sv, scale, name = sys.argv, 12, ""

def mpy(sss, cale=12):
    global ans
    ans = eval(sss)
    ans = cn_rn(ans, cale) if num(ans) else ans
    return ans

def get_help(s=''):
    import mymath as m
    dna = eval(s) if m.able_(s) else m
    help(m) if len(s) == 0 else help(dna)

def parse_args():
    """解析命令行参数，包括pypynum输出控制参数"""
    args = sys.argv[1:]
    expr = ""
    scale_val = 12
    suppress_pypynum = None  # 默认不改变当前设置
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ("-h", "--help"):
            # 处理帮助参数
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                name = args[i+1]
                get_help(name)
                exit()
            else:
                get_help()
                exit()
        elif arg == "--suppress-pypynum":
            suppress_pypynum = True
            i += 1
            continue
        elif arg == "--show-pypynum":
            suppress_pypynum = False
            i += 1
            continue
        elif arg.startswith('-'):
            # 其他参数处理
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                # 参数后跟值
                if arg in ["-s", "--scale"]:
                    try:
                        scale_val = int(args[i+1])
                    except ValueError:
                        print(f"错误: {args[i+1]} 不是有效的数值")
                        exit()
                i += 2
                continue
        else:
            # 表达式参数
            if not expr:
                expr = arg
            elif scale_val == 12:  # 只有在未通过-s或--scale设置时才用作scale
                try:
                    scale_val = int(arg)
                except ValueError:
                    print(f"[notice]: 参数 {arg} 无法识别")
            i += 1
            continue
        i += 1
    
    return expr, scale_val, suppress_pypynum

# 解析命令行参数
expr, scale, suppress_pypynum = parse_args()

# 根据参数设置pypynum输出
if suppress_pypynum is not None:
    set_pypynum_output(suppress=suppress_pypynum)

# 如果没有提供表达式，显示帮助并退出
if not expr:
    print('use: zm-sh.py "[expr]" [scale=12]')
    print('use: zm-sh.py --suppress-pypynum "[expr]" [scale=12]')
    print('use: zm-sh.py --show-pypynum "[expr]" [scale=12]')
    print("help: zm-sh.py -h|--help [name]")
    exit()

nbm = expr

if "it" in nbm:
    print('END'); exit() #quit or exit
elif nbm == "clear":
    print('clear'); exit()
if not able_(nbm):
    print("[notice]:can't exec"); exit()
elif "-h" in nbm:
    get_help(name); exit() # -h or --help

if nbm[:4] != "set ":
    _ = mpy(nbm, int(scale))
    print(_)
elif nbm[:4] == "set ":
    if len(nbm) < 7: 
        print("eg:set x=1"); exit()
    nbmm = [nbm[4], nbm[6:]]
    nbms = "=".join(nbmm)
    exec(nbms)
    print("赋值:", nbms)