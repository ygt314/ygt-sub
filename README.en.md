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
└── terset.sh         # Plan your termux for subject
```

## Quick Start

1. Install the Termux app
2. Change the domestic mirror source:
   ```bash
   termux-change-repo
   ```
3. Download project：
### (1)[In Termux]subter\_1.1.5.zip
```
cd;curl https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.5.zip>sbt.zip
```
[Unzip and clean]
```bash
cd;unzip sbt.zip;rm sbt.zip
```
If you don't have 'unzip', you can use (2)
### (2)[In Termux]subter\_1.1.5.tar
```bash
cd;curl https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.5.tar>sbt.tar
```
[Unzip and clean]
```bash
cd;tar -xvf sbt.tar;rm sbt.tar
```
4. Run the initial script：
   ```bash
   cd
   bash terset.sh
   ```

## zhtmlf

It in ~/zhtmlf
1. Download and update
   You can use the automated script of this project **hhts.sh**
   ```bash
   bash hhts.sh
   ```
2. set up http server
   To access the subject webpage, you need to open the zhtmlf directory locally **http server**
   Two methods have been deployed in this project **(bash function)**:http.server(in python),and http-server(in nodejs)
   (1)python method function
   ```bash
   hhf
   ```
   (2)nodejs method function
   ```bash
   hhf_np
   ```
3. html to txt
   The 'cdh' function can be enabled
   ```bash
   cdh
   purl [URL]
   ```
   1.sh: catch local html
   ```bash
   bash 1.sh
   ```
   2.sh: you can put URL after '>>>'
   ```bash
   bash 2.sh
   ```
   hl\_new.sh realizes the extraction of Conan's update information
   ```bash
   bash hl_new.sh
   ```

## zbashfile

Use:
Long-press Termux app on the desktop to enable 'failsafe'，into 'failsafe' model
   ```bash
   source zbashfile/.bashrc
   ```
But you can only use your system commands

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