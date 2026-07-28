"""资源路径兼容工具。

兼容开发目录与 PyInstaller 打包后的路径 (__MEIPASS)。
"""
import os
import sys


def get_app_root() -> str:
    """返回项目根目录。

    开发时基于本文件所在目录向上回退两级：
      project/utils/resources.py -> project/
    打包后使用 PyInstaller 解包根目录 sys._MEIPASS。
    """
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    # 本文件位于 project/utils/resources.py，向上回退两级到项目根目录
    # 但当 __file__ 是点 pyc/.pyo 或被冻结时，回退路径不可靠；
    # 这里采用从当前路径往父级查找 templates 的方式确定项目根。
    current = os.path.dirname(os.path.abspath(__file__))
    candidate = current
    for _ in range(3):
        if os.path.isdir(os.path.join(candidate, 'templates')):
            return candidate
        parent = os.path.dirname(candidate)
        if parent == candidate:
            break
        candidate = parent
    # 兜底：默认回退两级
    return os.path.dirname(os.path.dirname(current))


APP_ROOT = get_app_root()


def resource_path(rel: str) -> str:
    """返回相对项目根目录的绝对路径。"""
    return os.path.join(APP_ROOT, rel)


def get_template_folder() -> str:
    return resource_path('templates')


def get_static_folder() -> str:
    return resource_path('static')


def get_res_folder() -> str:
    return resource_path('res')
