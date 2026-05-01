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
- **AI智能支持**:版本1.1.8以上，自带模型的tgpt由本项目初始化脚本自动布署("本地智能"项)

## 目录结构

```
.
├── bcrc/           # bc数学
├── cmstrc/         # 化学配置
├── cnrc/           # 语文配置
├── en/             # 英语学习资源
├── enrc/           # 英语配置
├── mapyrc/         # py数学
├── mathrc/         # 数学配置
├── zbashfile/      # 示例shell环境(用于安全模式)
├── zchinese/       # 中文学习资源
├── .bashrc         # Termux环境配置
├── .gitignore      # Git忽略规则
├── LICENSE         # EPL-1.0开源协议
├── install.sh      # 项目布署脚本
├── README.md       # 项目说明(中文)
├── README.en.md    # 项目说明(英文)
└── terset.sh       # 计划环境脚本
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
[termux中下载]subter\_1.2.0.zip(汉化版操作相同)
```bash
cd;curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.2.0.zip>sbt.zip
```
[解压并清理]
```bash
cd;unzip sbt.zip;rm sbt.zip
```
如果你没有unzip可以采用方式(2)(原生版和汉化版操作相同)

[termux中下载]subter\_1.2.0.tar(汉化版操作相同)
```bash
cd;curl https://gitee.com/ygt314159/subject-termux/raw/master/subter_1.2.0.tar>sbt.tar
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

## 🚀 AI智能

本项目布署了两个本地AI工具(不联网也能用本地模型)——ollama和tgpt
### Ollama：一键搞定本地大模型部署
> Ollama是一款专注于本地部署、运行大语言模型（LLM） 的开源工具，目标是降低普通用户与开发者使用本地大模型的门槛，只需简单操作就能在个人设备上运行各类主流开源大模型。

Ollama（中文常音译为“奥拉马”）其实就是一款能让你在自己电脑本地跑开源大模型的工具，不用复杂配置，新手也能轻松上手，完全不用担心隐私泄露问题～💻✨
- 为什么它对新手这么友好？
   1. 安装超简单：支持Windows、macOS、Linux全平台，Linux更是一条命令就能搞定，Windows/macOS下载安装包点点下一步就行，全程不用折腾环境依赖。
   2. 用起来像点外卖：想玩哪个模型，只要打开命令行输入"ollama run 模型名"，它会自动帮你下载+启动，直接就能和模型聊天，比如"ollama run llama3"就能体验最新的Llama 3大模型。
   3. 不占太多资源：它本身只额外占100MB左右内存，哪怕你没有高端显卡，也能跑小参数模型（比如7B参数模型，8G内存就能跑），普通笔记本也能hold住。
- 核心好处就是两个：
    - 🔒 隐私安全拉满：所有对话、数据都存在你自己电脑里，不用上传到云端，敏感内容放心用。
    - 📶 离线也能玩：只要第一次下载好模型，断网也能正常使用，再也不用担心网络卡或者服务下线啦。
现在 GitHub 上已经有超过15万开发者给它点星，不管你是想玩本地AI助手，还是想试试不同开源大模型，Ollama都是新手入坑的不二之选～🚀
### 🤖 TGPT：你的终端原生AI小助手，新手也能轻松玩
>TGPT（Terminal GPT）是一款跨平台命令行工具，允许用户在终端中直接使用AI聊天机器人，无需API密钥。

TGPT是一款完全开源的AI工具，专门为命令行环境设计，哪怕你是刚接触终端的新手，也能快速上手用AI搞定各种问题。目前主要分为两个开发分支，满足不同使用需求：

1️⃣  Go版本TGPT（本项目默认采用）
- ✨ 核心亮点：模块化设计支持接入多家AI服务商，默认自带专为开发者优化的Phind模型，开箱即用(不用额外配置)；支持跨全平台运行，Linux/macOS/Windows都能装，一键脚本/包管理器两步就能装好，全程不用折腾复杂环境。
- 💡 新手友好特性：三种交互模式覆盖日常所有场景：普通问答直接输命令，写代码/长文用多行模式保持格式，连shell命令都能让AI生成并直接执行，简直是终端新手的作弊神器😉

2️⃣  python-tgpt版本
这是Python包形式的开源AI交互接口，最大惊喜是完全不需要API密钥就能免费使用🎉!支持45+种开源语言模型，不仅能帮你生成文本、写代码，还能直接根据文字生成图片，甚至把文本转成语音，一个工具搞定多种AI能力，本地就能跑起来，隐私又省心。

## 学科网页目录

本项目已经确定其位置:~/zhtmlf(原生版和汉化版相同)
### 1. 下载更新
本项目已经部署自动化脚本**hhts.sh**。
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
