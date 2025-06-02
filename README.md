# 学科ter - Termux学科资源集合

![Gitee Stars](https://gitee.com/ygt314159/subject-ter/badge/star.svg?theme=gray)
![Gitee Forks](https://gitee.com/ygt314159/subject-ter/badge/fork.svg?theme=gray)

## 📌 项目简介

学科ter是一个为Termux（Android端的Linux终端模拟器）提供的学科相关资源程序集合。Termux允许用户在Android设备上运行完整的Linux环境，本项目则在此基础上提供了多个学科的学习辅助工具和资源。

## 主要功能

- **多学科支持**：包含数学、英语、地理等多个学科的学习资源
- **Shell脚本工具**：提供便捷的学科相关命令行工具
- **配置文件管理**：各学科的个性化配置方案

## 目录结构

```
.
├── bcrc/            # bc数学
├── cmstrc/          # 化学配置
├── en/              # 英语学习资源
├── enrc/            # 英语配置
├── mapyrc/          # py数学
├── mathrc/          # 数学配置
├── zbashfile/       # 示例shell环境(用于安全模式)
├── zchinese/        # 中文学习资源
├── .bashrc          # Termux环境配置
├── .gitignore       # Git忽略规则
├── LICENSE          # EPL-1.0开源协议
├── README.md        # 项目说明(中文)
├── README.en.md     # 项目说明(英文)
├── subter_1.1.3.zip      # 本项目zip压缩打包
└── terset.sh         # 计划环境脚本
```
## 🚀 快速开始

1. 安装Termux应用
2. 更换国内(清华)源
   ```bash
   termux-change-repo
   ```
   依次选择_Single mirror_>>_Mirror by Tsinghua University TUNA_即可更换国内清华源
   [清华大学镜像站帮助](https://mirrors.tuna.tsinghua.edu.cn/help/termux/)
3. 克隆本项目：
   ```bash
   git clone https://gitee.com/ygt314159/subject-ter.git      
   ```
如果你没有git帐号，在浏览器中下载本项目subter\_1.1.3.zip文件
选择用termux打开并选择'Dir...'转到文件位置
   ```bash
   unzip subter-1.1.1.zip -d ~
   ```
4. 运行初始化脚本：
   ```bash
   cd
   bash terset.sh
   ```
## 学科网页目录
本项目已经确定其位置:~/zhtmlf
1. 下载更新
   本项目已经部署自动化脚本**hhts.sh**
   ```bash
   bash hhts.sh
   ```
2. 建立http服务
   访问学科网页需要你在本地开启zhtmlf目录的**http服务**
   本项目已经部署两种方法的**bash函数**:python的server标准库和http-server(nodejs工具)
   (1)python方法函数
   ```bash
   hht
   ```
   (2)nodejs方法函数
   ```bash
   hht_np
   ```
## zbashfile目录
使用方法:
在桌面长按termux启用'failsafe'，进入安全模式
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
- [Gitee帮助文档](https://gitee.com/help)
- [开源协议说明](https://www.eclipse.org/legal/epl-v10.html)
