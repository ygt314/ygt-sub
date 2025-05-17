![Gitee Stars](https://gitee.com/ygt314159/subject-ter/badge/star.svg?theme=gray) ![Gitee Forks](https://gitee.com/ygt314159/subject-ter/badge/fork.svg?theme=gray)

## 项目简介

学科ter是一个为Termux（Android端的Linux终端模拟器）提供的学科相关资源程序集合。Termux允许用户在Android设备上运行完整的Linux环境，本项目则在此基础上提供了多个学科的学习辅助工具和资源。

## 主要功能

- **多学科支持**：包含数学、英语、地理等多个学科的学习资源
- **Shell脚本工具**：提供便捷的学科相关命令行工具
- **配置文件管理**：各学科的个性化配置方案

## 目录结构

```
.
├── bcrc/            # 学科相关配置
├── cmstrc/          # 学科相关配置
├── en/              # 英语学习资源
├── enrc/            # 英语配置
├── mapyrc/          # 地理相关配置
├── mathrc/          # 数学相关配置
├── zbashfile/       # Bash脚本文件
├── zchinese/        # 中文学习资源
├── .bashrc          # Termux环境配置
├── .gitignore       # Git忽略规则
├── LICENSE          # EPL-1.0开源协议
├── README.md        # 项目说明(中文)
├── README.en.md     # 项目说明(英文)
└── nbter.sh         # 主程序脚本
```

## 快速开始

1. 安装Termux应用
2. 克隆本项目：
   ```bash
   git clone https://gitee.com/ygt314159/subject-ter.git
   ```
3. 运行初始化脚本：
   ```bash
   cd subject-ter
   bash nbter.sh
   ```

## 许可证

本项目采用 **EPL-1.0** 开源许可证。

## 贡献指南

欢迎通过Pull Request或Issue参与项目贡献：
1. Fork本仓库
2. 创建新分支（Feat_xxx/Fix_xxx）
3. 提交代码变更
4. 发起Pull Request

## 相关资源

- [Termux官网](https://termux.com/)
- [Gitee帮助文档](https://gitee.com/help)
- [开源协议说明](https://www.eclipse.org/legal/epl-v10.html)