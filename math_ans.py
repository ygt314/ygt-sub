import sys
sys.path.append('mapyrc/')
import math_txt as mat

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        mat.get_run(text)
    else:
        print("用法: python math_ans.py <文件名>")