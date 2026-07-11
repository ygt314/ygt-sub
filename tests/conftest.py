import sys
import os

# 目录顺序：先插入 mapyrc，再插入项目根目录，
# 使项目根目录在 sys.path 中优先，确保 mymath/ 包覆盖 mapyrc/mymath.py
MAPYRC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'mapyrc')
sys.path.insert(0, MAPYRC_DIR)

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)
