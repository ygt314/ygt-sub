# Subject-termux: Termux Subject Resources

![Gitee Stars](https://gitee.com/ygt314159/subject-termux/badge/star.svg?theme=gray)
![Gitee Forks](https://gitee.com/ygt314159/subject-termux/badge/fork.svg?theme=gray)

[中文](README.md) | [English]

## 📌 Project Introduction

Subject-ter is a collection of subject-related resource programs for (zero)Termux, a Linux terminal emulator for Android devices. Termux allows users to run a complete Linux environment on Android devices, and this project provides learning assistance tools and resources for multiple subjects on this basis.
Note: This project works with both the original version and the ZeroTermux Chinese version.

## ✨ Feature Overview

| Category | Tool | Description |
|:---------|:-----|:------------|
| 🧮 **Math** | `pym` command | Python math calculator supporting trig, complex numbers, symbolic computation |
| | `bcm` / `bc -l math.bc` | GNU bc arbitrary precision math library (trig/log/factorial/summation) |
| | `math` / Shell tools | Shell calculator + `ran`/`deta`/`fx` functions |
| | `bash find_x.sh` / `cputest-pi.sh` | Root finding / CPU pi benchmark |
| | `python3 an_sn1.py` | Sequence summation formula derivation |
| | `python3 tri_abA.py` | Triangle (SSA) solver |
| | `python3 yfx.py` | Function value table generator |
| | `python3 con_fra.py` / `con_sqrt.py` | Continued fraction / continued radical computation |
| | Haskell scripts | Prime checking, permutations, statistics |
| 📐 **Plotting** | `python3 plot.py` | Terminal ASCII function plotting (supports f(x) and f(x,y)=0) |
| 🔬 **Chemistry** | Element lookup | Periodic table of 118 elements (Chinese & English names) |
| | `che_ba.py` | Chemical equation balancer |
| | `ph` / `dz` / `hxs` | pH calculation, elemental substance, chemical formula |
| 📖 **Chinese** | `mtxt` | Interactive poetry dictation (4-choice, accuracy tracking) |
| | `pf` | Poetry typewriter (character-by-character output) |
| | `page` / `pages` | Paged file reader with GBK support |
| 🔤 **English** | `r_w` | IPA pronunciation lookup with history |
| 🌎 **Astronomy** | `sun_len.py` | Solar elevation/azimuth/sunrise-sunset calculator |
| 🌐 **Web Pages** | `hhf` / `hhf_np` / `ppht.sh` | HTTP server + zhtmlf automated update script |
| 🤖 **AI Smart** | `ollama` + `tgpt` | Local LLM deployment + terminal AI assistant (offline-capable) |
| 🛠️ **Utilities** | `pff.sh` | Line-by-line file viewer (interactive) |
| | `con_txt.sh` | HTML text extraction, strip font markup |
| | `autoclearc` | One-click clean pip/npm/apt/go caches |
| | `startcmdrc` | Startup server + exam countdowns + pkg update |

## Directory Structure

```
.
├── bcrc/            # bc math library
├── cmstrc/          # chemistry config
├── cnrc/            # chinese config
├── en/              # English study resources
├── enrc/            # English config
├── mapyrc/          # python math (core pym backend)
├── mathrc/          # math config
├── zbashfile/       # safe-mode shell environment ([docs](zbashfile/README.md))
├── zchinese/        # Chinese study resources
├── zhtmlf/          # subject web resources ([docs](zhtmlf/README.md))
├── .bashrc          # Termux environment config
├── .gitignore       # Git-ignore rules
├── LICENSE          # EPL-1.0 open source license
├── README.md        # README (CN)
├── README.en.md     # README (EN)
└── terset.sh        # environment setup script
```

## 📄 Subdirectory Documentation

Each subdirectory may contain its own documentation with more detailed information:

| Directory | Document | Description |
|:----------|:---------|:------------|
| `mapyrc/` | [pymhelp.md](mapyrc/pymhelp.md) | pym calculator full command reference (CN/EN) |
| `mathrc/` | [README.md](mathrc/README.md) | Math config directory file index |
| `zbashfile/` | [README.md](zbashfile/README.md) | Bash toolkit detailed manual (684 lines) |
| `zhtmlf/` | [README.md](zhtmlf/README.md) | Subject web resources overview |
| `zhtmlf/gczcdjs/` | [README.md](zhtmlf/gczcdjs/README.md) | Gaokao/Zhongkao countdown tool |
| `zhtmlf/math/homo-master/` | [README.md](zhtmlf/math/homo-master/README.md) | "Homo Number" calculator |
| `zhtmlf/chemistry/ChemCalcu-master/` | [README.md](zhtmlf/chemistry/ChemCalcu-master/README.md) | ChemCalcu molecular weight calculator |

## 🚀 Quick Start

1. Install the Termux app
2. Change the domestic mirror source:
```bash
termux-change-repo
```
3. Deploy the project:
```bash
curl -fsSL https://gitee.com/ygt314159/subject-termux/raw/master/install.sh|bash
```

## 🧮 Math Tools

### pym — Interactive Math Calculator (Core Tool)

`pym` is the core math tool of this project, built on Python + sympy/symengine, supporting terminal-based mathematical computation.

```bash
pym "expression" [decimal places]

pym "sin(pi/3)"          # Trig → 0.866025403784439
pym "sqrt(2)" 5          # Sqrt with 5 decimals → 1.41421
pym "log(100,10)"        # Logarithm → 2
pym "1+2i"               # Complex number support → (1+2j)
pym "set x = 5"          # Variable assignment
pym "x**2 + 2*x + 1"     # Use variable → 36
```

**Supported**: sin/cos/tan/cot/sec/csc (radians & degrees), inverse trig, hyperbolic functions, exponentials & logarithms, rounding, complex numbers, constants (pi/e/phi/s2/gama), angle conversion (d_r/r_d).

### bcm — bc Arbitrary Precision Calculator

```bash
bc -l bcrc/math.bc       # Or use the bcm wrapper

sin(pi/4)                # Sine, auto angle handling
f(10)                    # 10! = 3628800
fbnc(20)                 # Fibonacci sequence 20th term
ln(100)                  # Natural log
```

### Shell Math Functions

```bash
math                    # Launch integer calculator
math_f                  # Launch decimal calculator
ran [n]                 # Generate random number 0~(n-1)
deta a b c              # Quadratic discriminant Δ=b^2-4ac
fx "x^2+1" 3            # Evaluate f(x) at x=3 → 10

bash find_x.sh          # Interactive root finder: scan [x1,x2] for f(x)=0
                        # Auto-detects roots and sign-change intervals (uses pym)
bash find_x_bc.sh       # Same but using bcm (high-precision bc)

bash cputest-pi.sh      # CPU pi benchmark: compute π via bc -l a(1)*4 with timing
```

### Python Math Scripts

| Command | Description |
|:--------|:------------|
| `python3 an_sn1.py [exp]` | Given a_n=n^k, derive S_n formula (e.g., `an_sn1.py 2` → S_n=n(n+1)(2n+1)/6) |
| `python3 sn_an.py "formula"` | Reverse derive a_n from S_n |
| `python3 tri_abA.py` | Interactive triangle solver (SSA case) |
| `python3 out_tri.py 0,0 3,0 0,4` | Circumcircle from 3 points |
| `python3 yfx.py` | Generate y=f(x) value table |
| `python3 con_fra.py 1,2,3` | Continued fraction 1+1/(2+1/3) |
| `python3 con_sqrt.py 1,2,3` | Continued radical √(1+√(2+√3)) |
| `python3 sun_len.py` | Solar elevation/azimuth/sunrise-sunset |
| `python3 math_ans.py filename` | Parse teaching doc, auto-compute & output steps |
| `python3 sym_init.py` | SymPy symbolic computation session |

### Haskell Examples

```bash
runhaskell pp.hs        # Fibonacci sequence
runhaskell prime.hs     # Prime checking
runhaskell evq.hs       # Random number mean & std deviation
```

## 🔬 Chemistry Tools

- **Periodic Table**: 118 elements with Chinese/English names and symbols
- **pH Calculation**: `ph` function
- **Elemental Substance** (单质): `dz` function
- **Chemical Formula**: `hxs` function (modifies variables only, no stdout output except errors)
- **Equation Balancing**: `che_ba.py`

```bash
python3 che_ba.py H2,O2 H2O
# Output: 2H2 + O2 → 2H2O
```

## 📖 Chinese Language Tools

### Poetry Dictation (mtxt)
```bash
mtxt "床前明月光"
# Character-by-character 4-choice quiz with accuracy tracking
```

### Poetry Typewriter (pf)
```bash
pf                  # Interactive mode: list poems, search by keyword, typewriter output
pf 静夜思           # Display a specific poem directly
# Press q anytime to quit; some poems support dictation mode (# title)
```

Powered by the `ptxt()` character-by-character print function with adjustable speed and punctuation pauses.

### Paged Reader (page)
```bash
page f filename          # Display file 15 lines per page
page f filename gbk      # GBK encoding support
pages f filename         # Interactive: +/- page, g/jump, q/quit
```

## 🔤 English Tools

### IPA Pronunciation Lookup (r_w)

```bash
r_w hello                # Lookup IPA pronunciation of "hello"
r_w hello 2              # Lookup phonetic spelling
r_w                      # Interactive mode, query one word at a time
```

History is automatically logged to `~/.listen_history`.

## 📐 Function Plotting

Terminal ASCII function plotting, no GUI required.

```bash
python3 plot.py
# Interactive: enter function, x-range, y-range

python3 plot2.py
# Enhanced auto-range version

python3 plot_sh.py "sin(x)" "-10:10" "-2:2"
python3 plot2_sh.py "x*x" "-5:5" "0:25"
# CLI parameter mode (function x_min:x_max y_min:y_max)
```

Supports `y=f(x)` and implicit functions `f(x,y)=0`.

## 🛠️ Utilities

### Line-by-Line File Viewer (pff)

```bash
bash pff.sh
# Interactive mode: type filename after >>>, press q to quit
# Supports ls for directory browsing

bash pff.sh filename
# Direct file view
```

### Terminal HTML Text Extraction (con_txt)

```bash
bash con_txt.sh
# Pick an html file interactively, extract text content
# Auto-handles <br> and unicode escape sequences

bash con_txt.sh file.html
# Direct file extraction
```

### System Management

```bash
bash autoclearc         # One-click clean pip/npm/apt/go caches
```

`startcmdrc` runs on startup and provides:
- **http-server** / **jupyter notebook** quick launch
- **Exam countdowns**: `zc` / `gc` / `cnmt` / `cngt`
- **Package manager updates**: `pkg upgrade`, `pipup`, `noup` (npm update)

## 🤖 AI Smart Tools

This project deploys two local AI tools — ollama and tgpt — both working offline.

### Ollama: Local LLM Runner

```bash
ollama run <model_name>
ollama run llama3        # Run Llama 3
ollama run qwen2:7b      # Run Qwen 2 7B
```

One command to download and run mainstream open-source LLMs. All data stays local, works without internet.

### TGPT: Terminal AI Assistant

Default Go version, no API key required. Three interaction modes:

```bash
tgpt "your question"        # Normal Q&A
tgpt -m "write some code"   # Multi-line mode (code/long text)
tgpt -s "install nginx"     # Shell command mode
```

Python-tgpt also available, supporting 45+ open-source language models plus text-to-image and text-to-speech.

## 🌐 Subject Web Pages

Location: ~/zhtmlf (same for both original and ZeroTermux versions)

### 1. Download & Update
The project provides the **ppht.sh** automated script (formerly hhts.sh), run automatically on first deployment.
Run periodically to update:
```bash
bash ppht.sh
```
### 2. Start HTTP Server
Access subject web pages via local HTTP server in the zhtmlf directory:
- Python method: `hhf`
- Node.js method: `hhf_np`
### 3. HTML Reading
```bash
cdh
purl [URL]               # Fetch and display web page
pht [FILE]               # Display local HTML file
```
```bash
bash 1.sh                # Display local HTML
bash 2.sh                # Interactive URL input
bash hl_new.sh           # Extract Conan update info
```

## 🛡️ zbashfile Directory

Long-press the Termux app icon on desktop → enable 'failsafe' mode, then:
```bash
source zbashfile/.bashrc
```
Limited to system commands only.

## License

This project is licensed under the **EPL-1.0** open source license.

## Contribution Guide

Welcome to contribute through Pull Requests or Issues:
1. Fork this repository
2. Create a new branch (Feat_xxx/Fix_xxx)
3. Submit code changes
4. Create a Pull Request

## Related Resources

- [Termux Official Website](https://termux.com/)
- [ZeroTermux Download](https://d.icdown.club/doc/)
- [Termux-X Official](https://termux-x.com/)
- [Gitee Help Documentation](https://gitee.com/help)
- [Open Source License Explanation](https://www.eclipse.org/legal/epl-v10.html)
