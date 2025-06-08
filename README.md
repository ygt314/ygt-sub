# 学科ter - (zero)Termux学科资源集合

![Gitee Stars](https://gitee.com/ygt314159/subject-ter/badge/star.svg?theme=gray)
![Gitee Forks](https://gitee.com/ygt314159/subject-ter/badge/fork.svg?theme=gray)

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

下列方法仅适合国内用户
1. 安装Termux应用
**原生版下载**
-[1][当快源下载](https://azshareappdk.3322.cc/appfile/com.termux.apk?time=1749375009&key=ffb13415b8e26714891ccf5165273526)
[当快介绍页面](https://www.downkuai.com/android/140917.html)
-[2][2233源下载](https://azshareappr.3322.cc/appfile/com.termux.apk?time=1749375149&key=2a544bd7a618cb58395cd0ef7db8238e)
[2233介绍页面](https://www.32r.com/app/136073.html)
------
**汉化版下载**(ZeroTermux)
-[1][官网版下载](https://d.icdown.club/repository/main/ZeroTermux/ZeroTermux-0.118.1.43.apk)
[官网下载站](https://d.icdown.club/doc/)
-[2][脚本之家源下载](https://yddown4.jb51.net/202503/tools/zerotermux_979076.apk?auth_key=1749375866-e11f859287b98692f10c-0-dd3c542b4fd3dda8a875dd80b7d4e54c01e8da80d98a56a1b9e3964538f7e2ff)
[脚本之家介绍页面](https://www.jb51.net/softs/979076.html)
-[3][新绿源下载](http://x1.ydyspc.com/zerotermuxv0.118.38.1_xlhs.com.apk)
[新绿介绍页面](http://m.xlhs.com/app/2710.html)
2. 更换国内(清华)源
   如果你下载了汉化版:
   在软件里侧拉工具箱，点击[换源]并选择[清华源]即可
------
   如果你下载了原生版:
   ```bash
   termux-change-repo
   ```
   依次选择_Single mirror_>>_Mirror by Tsinghua University TUNA_即可更换国内清华源
   [清华大学镜像站帮助](https://mirrors.tuna.tsinghua.edu.cn/help/termux/)
3. 下载本项目(原生版和汉化版操作相同)：
-(1)[浏览器中下载]本项目[subter\_1.1.3.zip](https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.3.zip)文件，选择用termux打开并选择'Dir...'转到文件位置
**移动文件**后再解压
```bash
mv subter_1.1.3.zip ~/sbt.zip
```
[termux中下载]subter\_1.1.3.zip(汉化版操作相同)
```
cd;curl https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.3.zip>sbt.zip
```
[解压并清理]
```bash
cd;unzip sbt.zip;rm sbt.zip
```
如果你没有unzip可以采用方式(2)(原生版和汉化版操作相同)
------
-(2)[浏览器中下载]本项目[subter\_1.1.3.zip](https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.3.tar)文件，选择用termux打开并选择'Dir...'转到文件位置
**移动文件**后再解压
```bash
mv subter_1.1.3.tar ~/sbt.tar
```
[termux中下载]subter\_1.1.3.tar(汉化版操作相同)
```bash
cd;curl https://gitee.com/ygt314159/subject-ter/raw/master/subter_1.1.3.tar>sbt.tar
```
[解压并清理]
```bash
cd;tar -xvf sbt.tar;rm sbt.tar
```
4. 运行初始化脚本(原生版和汉化版操作相同)：
   ```bash
   cd
   bash terset.sh
   ```

## 学科网页目录

本项目已经确定其位置:~/zhtmlf(原生版和汉化版相同)
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
   hhf
   ```
   (2)nodejs方法函数
   ```bash
   hhf_np
   ```
3. html阅读功能
   cdh函数命令即可启用
   ```bash
   cdh
   purl [http链接]
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
- [Gitee帮助文档](https://gitee.com/help)
- [开源协议说明](https://www.eclipse.org/legal/epl-v10.html)
