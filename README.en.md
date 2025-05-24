# Subject-ter: Termux Subject Resources

![Gitee Stars](https://gitee.com/ygt314159/subject-ter/badge/star.svg?theme=gray) ![Gitee Forks](https://gitee.com/ygt314159/subject-ter/badge/fork.svg?theme=gray)

## Project Introduction

Subject-ter is a collection of subject-related resource programs for Termux, a Linux terminal emulator for Android devices. Termux allows users to run a complete Linux environment on Android devices, and this project provides learning assistance tools and resources for multiple subjects on this basis.

## Main Features

- **Multi-subject Support**: Includes learning resources for mathematics, English, geography and other subjects
- **Shell Script Tools**: Provides convenient command-line tools for various subjects
- **Configuration Management**: Personalized configuration solutions for different subjects

## Directory Structure

```
.
├── bcrc/            # BC math sources
├── cmstrc/          # Chemistry sources
├── en/              # English learning resources
├── enrc/            # English sources
├── mapyrc/          # Python math sources
├── mathrc/          # Math sources
├── zbashfile/       # Bash shell e.g.-env
├── zchinese/        # Chinese learning resources
├── .bashrc          # Termux environment configuration
├── .gitignore       # Git ignore rules
├── LICENSE          # EPL-1.0 open source license
├── README.md        # Project description (Chinese)
├── README.en.md     # Project description (English)
├── subter-1.1.1.zip      # Zip package
└── terset.sh         # Plan your termux for subject
```

## Quick Start

1. Install the Termux app
2. Clone this project:
   ```bash
   git clone https://gitee.com/ygt314159/subject-ter.git
   ```
   If you have not 'git',download the zip file in the browser.Then,open it in termux.(choose 'Dir...')
   通过百度网盘分享的文件：
   [subject-…](https://pan.baidu.com/s/12n1xJgMGeiO_p_k7fVQHnA?pwd=b68v )
   ```
   unzip subter-1.1.1.zip
   mv subter-1.1.1/* -r ~
   ```
   
3. Run the initialization script:
   ```bash
   cd
   bash terset.sh
   ```
    Befor,you need not run terset.sh
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
- [Gitee Help Documentation](https://gitee.com/help)
- [Open Source License Explanation](https://www.eclipse.org/legal/epl-v10.html)