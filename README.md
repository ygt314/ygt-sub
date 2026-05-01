# 学科termux - (zero)Termux学科资源集合

![Gitee Stars](https://gitee.com/ygt314159/subject-termux/badge/star.svg?theme=gray)
![Gitee Forks](https://gitee.com/ygt314159/subject-termux/badge/fork.svg?theme=gray)

[中文] | [English](README.en.md)

## 📌 项目简介

学科ter是一个为(zero)Termux（Android端的Linux终端模拟器）提供的学科相关资源程序集合。(zero)Termux允许用户在Android设备上运行完整的Linux环境，本项目则在此基础上提供了多个学科的学习辅助工具和资源。
注意:本项目同时对原生版和zero汉化版有效

## 主要功能

- **多学科支持**：包含数学、英语、地理等多个学科的学习资源
- **Shell脚本工具**：提供便捷的学科相关命令行工具
- **配置文件管理**：各学科的个性化配置方案

## 目录结构

```
.
├── bcrc/            # bc数学
├── cmstrc/          # 化学配置
├── cnrc/            # 语文配置
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
└── terset.sh        # 计划环境脚本
```
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
[termux中下载]subter\_1.1.9.zip(汉化版操作相同)
```bash
cd;curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.1.9.zip>sbt.zip
```
[解压并清理]
```bash
cd;unzip sbt.zip;rm sbt.zip
```
如果你没有unzip可以采用方式(2)(原生版和汉化版操作相同)

[termux中下载]subter\_1.1.9.tar(汉化版操作相同)
```bash
cd;curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.1.9.tar>sbt.tar
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

## 学科网页目录

本项目已经确定其位置:~/zhtmlf(原生版和汉化版相同)
### 1. 下载更新
本项目已经部署自动化脚本**hhts.sh**
如果你刚刚执行了项目布署(install.sh)脚本，hhts.sh会被自动执行一次

需要定期执行hhts.sh来更新
```bash
bash hhts.sh
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

## zbashfile目录

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
