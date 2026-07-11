"""
测试基线：tri_solve.py（已知自引用 bug）
标记为 xfail，记录问题待后续修复
"""
import pytest


@pytest.mark.xfail(strict=True, reason="自引用bug: 第11行 from tri_solve import ... 导入自身")
def test_tri_solve_import():
    """验证 tri_solve.py 的导入因自引用 bug 而失败"""
    import tri_solve
    # 如果导入成功（bug 修复后），至少应有基本函数
    assert hasattr(tri_solve, 'tgt')
