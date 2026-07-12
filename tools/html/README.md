# 学科HTML 命令行工具 (Termux)

本目录的 bash 工具已迁移至 [zhtmlf/html/bash/](../zhtmlf/html/bash/)。

## 快速使用

```bash
# 直接引用 submodule 中的工具
source ./zhtmlf/html/bash/html_txtrc

# 交互式 HTML 查看器
bash ./zhtmlf/html/bash/1.sh

# URL 下载 + HTML 查看
bash ./zhtmlf/html/bash/2.sh
```

## 安装到用户目录

```bash
# 将 bash 工具软链到 ~/.local/bin/
mkdir -p ~/.local/bin
ln -sf "$PWD/zhtmlf/html/bash/html_txtrc" ~/.local/bin/
ln -sf "$PWD/zhtmlf/html/bash/1.sh" ~/.local/bin/htview
ln -sf "$PWD/zhtmlf/html/bash/2.sh" ~/.local/bin/urlview

# 将以下内容加入 ~/.bashrc
# source ~/.local/bin/html_txtrc
```
