# 学科termux - (zero)Termux学科资源集合

![Gitee Stars](https://gitee.com/ygt314159/subject-termux/badge/star.svg?theme=gray)
![Gitee Forks](https://gitee.com/ygt314159/subject-termux/badge/fork.svg?theme=gray)

[中文] | [English](README.en.md)

## 📌 项目简介

学科ter是一个为(zero)Termux（Android端的Linux终端模拟器）提供的学科相关资源程序集合。(zero)Termux允许用户在Android设备上运行完整的Linux环境，本项目则在此基础上提供了多个学科的学习辅助工具和资源。
注意:本项目同时对原生版和zero汉化版有效

## ✨ 功能概览

| 类别 | 工具 | 说明 |
|:----|:----|:-----|
| 🧮 **数学** | `pym` 命令 | Python 数学计算器，支持三角函数、复数、符号运算 |
| | `bcm` / `bc -l math.bc` | GNU bc 任意精度数学库（三角函数/对数/阶乘/求和）|
| | `math` 命令 / Shell 工具 | Shell 整数/小数计算器 + `ran`/`deta`/`fx` 函数 |
| | `bash find_x.sh` / `cputest-pi.sh` | 函数寻根 / CPU 圆周率性能测试 |
| | `python3 an_sn1.py` | 数列求和公式推导 |
| | `python3 tri_abA.py` | 三角形（边边角）求解 |
| | `python3 yfx.py` | 函数值表生成 |
| | `python3 con_fra.py` / `con_sqrt.py` | 连分数 / 连根式计算 |
| | Haskell 示例 | 素数判定、排列组合、统计分析 |
| 📐 **函数绘图** | `python3 plot.py` | 终端字符画函数图像（支持 f(x) 和 f(x,y)=0）|
| 🔬 **化学** | 元素查询 | 118 个元素中英文名周期表查询 |
| | `che_ba.py` | 化学方程式自动配平 |
| | `ph` / `dz` / `hxs` | pH 计算 / 单质 / 化学式 |
| 📖 **语文** | `mtxt` | 古诗词交互式逐字默写练习（4选1，统计正确率）|
| | `pf` | 古诗打字机逐字输出 |
| | `page` / `pages` | 文件分页阅读器（支持翻页/跳转、GBK编码）|
| 🔤 **英语** | `r_w` | 单词 IPA 音标查询 + 自然拼读，自动记录历史 |
| 🌎 **地理天文** | `sun_len.py` | 太阳高度角 / 方位角 / 日出日落计算 |
| 🌐 **学科网页** | `hhf` / `hhf_np` / `ppht.sh` | HTTP 服务 + zhtmlf 自动化更新脚本 |
| 🤖 **AI 智能** | `ollama` + `tgpt` | 本地大模型部署 + 终端 AI 助手（无需联网）|
| 🛠️ **常用工具** | `pff.sh` | 逐行文件阅读器（交互式翻页）|
| | `con_txt.sh` | HTML 文本提取，去除字体标记 |
| | `autoclearc` | 一键清理 pip/npm/apt/go 缓存 |
| | `startcmdrc` | 启动服务 + 考试倒计时 + 包更新 |

## 目录结构

```
.
├── bcrc/           # bc数学
├── cmstrc/         # 化学配置
├── cnrc/           # 语文配置
├── en/             # 英语学习资源
├── enrc/           # 英语配置
├── mapyrc/         # py数学（核心：pym 计算器后端）
├── mathrc/         # 数学配置
├── zbashfile/      # 示例shell环境(用于安全模式) ([文档](zbashfile/README.md))
├── zchinese/       # 中文学习资源
├── zhtmlf/         # 学科网页资源 ([文档](zhtmlf/README.md))
├── .bashrc         # Termux环境配置
├── .gitignore      # Git忽略规则
├── LICENSE         # EPL-1.0开源协议
├── install.sh      # 项目布署脚本
├── README.md       # 项目说明(中文)
├── README.en.md    # 项目说明(英文)
└── terset.sh       # 计划环境脚本
```

## 📄 子目录文档

各子目录包含独立的说明文档，提供更详尽的功能介绍和使用参考：

| 目录 | 文档 | 说明 |
|:----|:-----|:-----|
| `mapyrc/` | [pymhelp.md](mapyrc/pymhelp.md) | pym 数学计算器完整命令参考（中英双语） |
| `mathrc/` | [README.md](mathrc/README.md) | 数学配置目录文件索引 |
| `zbashfile/` | [README.md](zbashfile/README.md) | Bash 工具集详细使用手册（684 行） |
| `zhtmlf/` | [README.md](zhtmlf/README.md) | 学科网页资源目录概览 |
| `zhtmlf/gczcdjs/` | [README.md](zhtmlf/gczcdjs/README.md) | 中高考倒计时工具 |
| `zhtmlf/math/homo-master/` | [README.md](zhtmlf/math/homo-master/README.md) | 恶臭数字论证器 |
| `zhtmlf/chemistry/ChemCalcu-master/` | [README.md](zhtmlf/chemistry/ChemCalcu-master/README.md) | 化学分子量计算器 ChemCalcu |

## 🚀 快速开始

下列方法适合国内用户
### 1. 安装Termux应用
**原生版下载**

- [1] [当快源下载](https://azshareappdk.3322.cc/appfile/com.termux.apk?time=1749375009&key=ffb13415b8e26714891ccf5165273526)
[当快介绍页面](https://www.downkuai.com/android/140917.html)
- [2] [2233源下载](https://azshareappr.3322.cc/appfile/com.termux.apk?time=1749375149&key=2a544bd7a618cb58395cd0ef7db8238e)
[2233介绍页面](https://www.32r.com/app/136073.html)
------
**汉化版下载**(ZeroTermux)

- [zerotermux官网](https://zerotermux.dev/)
- [1] [直接下载](https://d.icdown.club/repository/main/ZeroTermux/ZeroTermux-0.118.54.apk)
[官网下载站](https://d.icdown.club/doc/)
------
**高级汉化版**(Termux-X)

基于zero-termux项目
- [termux-x官网](https://termux-x.com)
- [Termux-X手册](https://termux-x.com/guide/introduction-overview)
- [1] [直接下载](https://xheishou.com/update/apk/nethunter/Termux-X-0.118.3.60.1.apk)
### 2. 更换国内(清华)源
- 如果你下载了汉化版:
在软件里侧拉工具箱，点击[切换源]并选择[清华源]即可临时换源。但关闭APP会失效，需要重新操作
如果你要获得永久支持，请按原生版操作
- 如果你下载了原生版(汉化版同样可以):
```bash
termux-change-repo
```
依次点击(或空格)选择 _Single mirror_(单镜像，位于第二项) >> _Mirror by Tsinghua University TUNA_ (若没有看到，请按↑或↓翻页)即可更换国内清华源
- Termux[清华大学镜像站帮助](https://mirrors.tuna.tsinghua.edu.cn/help/termux/)
### 3. 布署本项目(原生版和汉化版操作相同)
[安装curl]本项目依赖curl，先在Termux中执行
```bash
apt install -y curl
```
如果没有执行，下面脚本部分功能会失效

[自动化脚本布署]请在Termux中执行
```bash
curl -fsSL https://gitee.com/ygt314159/subject-termux/raw/master/install.sh|bash
```
#### 备用布署方案
[termux中下载]subter\_1.2.2.zip(汉化版操作相同)
```bash
cd;curl -L https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.2.2.zip>sbt.zip
```
[解压并清理]
```bash
cd;unzip sbt.zip;rm sbt.zip
```
如果你没有unzip可以采用方式(2)(原生版和汉化版操作相同)

[termux中下载]subter\_1.2.2.tar(汉化版操作相同)
```bash
cd;curl -L https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.2.2.tar>sbt.tar
```
[解压并清理]
```bash
cd;tar -xvf sbt.tar;rm sbt.tar
```
### 4.初始化脚本(原生版和汉化版操作相同)
项目布署脚本会自动进行初始化
如果你误用了apt remove命令或网络问题而终止，可以重新执行
```bash
cd
bash terset.sh
```

## 🧮 数学工具

### pym — 交互式数学计算器（核心工具）

`pym` 是本项目的核心数学工具，基于 Python + sympy/symengine 实现，支持在终端中直接进行数学计算。

```bash
pym "表达式" [小数位数]

pym "sin(pi/3)"          # 三角函数  → 0.866025403784439
pym "sqrt(2)" 5          # 根号保留5位小数 → 1.41421
pym "log(100,10)"        # 对数      → 2
pym "1+2i"               # 复数支持   → (1+2j)
pym "set x = 5"          # 变量赋值
pym "x**2 + 2*x + 1"     # 使用变量   → 36
```

**支持的功能**：三角函数（sin/cos/tan/cot/sec/csc, 支持弧度/角度）、反三角函数、双曲函数、指数对数、取整、复数运算、常数（pi/e/phi/s2/gama）、角度转换（d_r/r_d）。

### bcm — bc 任意精度计算器

基于 GNU bc 的数学库，支持高精度计算。

```bash
bc -l bcrc/math.bc
# 或使用封装的 bcm 命令

sin(pi/4)        # 正弦，自动角度处理
cos(0.5)         # 余弦
f(10)            # 10! = 3628800
fbnc(20)         # 斐波那契数列第20项
ln(100)          # 自然对数
```

### Shell 数学

```bash
math                 # 启动整数计算器 (math_s.sh)
math_f              # 启动小数计算器 (math_f.sh，基于 bc -l)
ran [n]             # 生成 0~(n-1) 随机数
deta a b c          # 一元二次方程判别式 Δ=b^2-4ac
fx "x^2+1" 3        # 将函数 f(x) 中的 x 替换为 3

bash find_x.sh      # 交互式函数寻根：在 [x1,x2] 区间扫描 f(x)=0 的解
                    # 支持自动检测根和变号区间（基于 pym）
bash find_x_bc.sh   # 同上，但基于 bcm（高精度 bc 计算）

bash cputest-pi.sh  # CPU 圆周率性能测试
                    # 用 bc -l 计算 π（a(1)*4），可指定位数并计时
```

### Python 数学脚本

| 命令 | 功能 |
|:-----|:-----|
| `python3 an_sn1.py [指数]` | 已知 a_n=n^k，求 S_n 公式（如 `an_sn1.py 2` 得 S_n=n(n+1)(2n+1)/6）|
| `python3 sn_an.py "n*(n+1)/2"` | 由 S_n 反推 a_n |
| `python3 tri_abA.py` | 交互式三角形求解（已知两边及对角，自动判断解的情况）|
| `python3 out_tri.py 0,0 3,0 0,4` | 三点确定外接圆，输出圆方程 |
| `python3 yfx.py` | 交互式生成 y=f(x) 的函数值表 |
| `python3 con_fra.py 1,2,3` | 连分数计算 1+1/(2+1/3) |
| `python3 con_sqrt.py 1,2,3` | 连根式计算 √(1+√(2+√3)) |
| `python3 sun_len.py` | 交互式计算太阳高度角/方位角/日出日落 |
| `python3 math_ans.py 文件名` | 解析教学文档，自动计算并输出解答步骤 |
| `python3 sym_init.py` | 启动 SymPy 符号计算交互会话 |

### Haskell 示例

```bash
runhaskell pp.hs      # 斐波那契数列
runhaskell prime.hs   # 素数判定
runhaskell evq.hs     # 随机数均值与标准差
```

## 🔬 化学工具

在 Termux 中可直接使用以下化学相关功能：

- **元素周期表查询**：118 个元素的中英文名、符号
- **pH 计算**：`ph` 函数
- **单质**：`dz` 函数
- **化学式**: `hxs` 函数（只修改变量，不输出结果，仅显示错误信息）
- **方程式配平**：`che_ba.py`

```bash
python3 che_ba.py H2,O2 H2O
# 输出: 2H2 + O2 → 2H2O
```

## 📖 语文工具

### 古诗打字机（pf）

```bash
pf                  # 交互模式：列出古诗，输入关键词搜索，逐字打字机输出
pf 静夜思           # 直接显示指定古诗
# 按 q 随时退出，部分古诗支持默写模式（带 # 标题）
```

基于 `ptxt()` 逐字打印函数，支持调节速度、标点停顿。

### 古诗词默写（mtxt）

```bash
mtxt "床前明月光"
# 逐个字符给出 4 个选项，选择正确字，统计正确率
```

### 分页阅读（page）

```bash
page f 文件名        # 每页 15 行显示文件
page f 文件名 gbk   # 支持 GBK 编码文件
pages f 文件名      # 交互式分页：+/翻页、-/回翻、g/跳转、q/退出
```

~~远古mp4式~~小说阅读，快来找回你的年少追文的快乐时光:)

## 🔤 英语工具

### 单词音标查询（r_w）

```bash
r_w hello          # 查询 hello 的 IPA 音标
r_w hello 2        # 查询自然拼读（speak -x）
r_w                # 交互模式，逐词查询
```

自动记录查询历史到 `~/.listen_history`。

## 📐 函数绘图

终端字符画函数图像，无需图形界面。

```bash
python3 plot.py
# 交互输入：函数、x范围、y范围

python3 plot2.py
# 自动探索范围的增强版

python3 plot_sh.py "sin(x)" "-10:10" "-2:2"
python3 plot2_sh.py "x*x" "-5:5" "0:25"
# 命令行参数版，格式：函数 x_min:x_max y_min:y_max
```

支持 `y=f(x)` 和隐函数 `f(x,y)=0`。

## 🛠️ 常用工具

### 逐行文件阅读器（pff）

```bash
bash pff.sh
# 交互模式：在 >>> 后输入文件名，逐行显示，按 q 退出
# 支持 ls 浏览目录

bash pff.sh 文件名
# 直接查看文件
```

### 终端 HTML 文本提取（con_txt）

```bash
bash con_txt.sh
# 交互选择 html 文件，提取文字内容，去除字体标记
# 自动处理 <br> 换行和 unicode 转义序列

bash con_txt.sh 文件.html
# 直接指定文件
```

### 系统管理

```bash
bash autoclearc         # 一键清理 pip/npm/apt/go 缓存
```

`startcmdrc` 在启动时自动运行，提供：
- **http-server** / **jupyter notebook** 快速启动
- **中考/高考倒计时**：`zc` / `gc` / `cnmt` / `cngt`
- **包管理器更新**：`pkg upgrade`、`pipup`、`noup`（npm update）

## 🤖 AI 智能

本项目布署了两个本地AI工具(不联网也能用本地模型)——ollama和tgpt

### Ollama：本地大模型部署

```bash
ollama run <模型名>
ollama run llama3        # 运行 Llama 3
ollama run qwen2:7b      # 运行通义千问 7B
```

安装简单，一行命令即可下载并运行主流开源大模型，所有数据在本地处理，断网也可使用。

### TGPT：终端 AI 助手

本项目默认采用 Go 版本 TGPT，开箱即用，无需 API 密钥。支持三种交互模式：

```bash
tgpt "你的问题"               # 普通问答
tgpt -m "写一段Python代码"    # 多行模式（代码/长文）
tgpt -s "安装nginx"          # Shell 命令模式（自动生成并执行）
```

另有 python-tgpt 版本，支持 45+ 种开源语言模型，还能根据文字生成图片和语音。

## 🌐 学科网页目录

本项目已经确定其位置:~/zhtmlf(原生版和汉化版相同)
### 1. 下载更新
本项目已经部署自动化脚本**ppht.sh**（原名 hhts.sh）。
如果你刚刚执行了项目布署(install.sh)脚本，ppht.sh会被自动执行一次

需要定期执行ppht.sh来更新
```bash
bash ppht.sh
```
### 2. 建立http服务
访问学科网页需要你在本地开启zhtmlf目录的**http服务**
本项目已经部署两种方法的**bash函数**:python的server标准库和http-server(nodejs工具)
- (1)python方法函数
```bash
hhf
```
- (2)nodejs方法函数
```bash
hhf_np
```
### 3. html阅读功能
cdh函数命令即可启用
```bash
cdh
purl [http链接]
pht [html文件]
```
1.sh:本地html
```bash
bash 1.sh
```
2.sh:purl的交互模式
```bash
bash 2.sh
```
hl\_new.sh实现提取柯南更新信息
```bash
bash hl_new.sh
```

## 🛡️ zbashfile目录

使用方法:
在桌面长按termux启用'failsafe'(汉化版为'故障安全')，进入安全模式
```bash
source zbashfile/.bashrc
```
但只能使用系统命令

## 许可证

本项目采用 **EPL-1.0** 开源许可证。

## 贡献指南
这个项目还处于初期阶段
欢迎通过Pull Request或Issue参与项目贡献：
1. Fork本仓库
2. 创建新分支（Feat_xxx/Fix_xxx）
3. 提交代码变更
4. 发起Pull Request

## 相关资源

- [Termux官网](https://termux.com/)
- [ZeroTermux官网下载站](https://d.icdown.club/doc/)
- [Termux-X官网](https://termux-x.com/)
- [Gitee帮助文档](https://gitee.com/help)
- [开源协议说明](https://www.eclipse.org/legal/epl-v10.html)