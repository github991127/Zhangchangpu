# -*- mode: python ; coding: utf-8 -*-
import os

from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

block_cipher = None

# spec 文件位于项目根目录
ROOT = os.path.dirname(os.path.abspath(SPECPATH))

a = Analysis(
    ['app.py'],
    pathex=[ROOT],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('static', 'static'),
        ('res', 'res'),
        ('source', 'source'),
        ('routes', 'routes'),
        ('utils', 'utils'),
    ],
    hiddenimports=['source.zhangchangpu', 'source.mizhu', 'source.dialogue'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide2', 'qt_material', 'PyQt5', 'PyQt6'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='zhangchangpu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='res/image.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='zhangchangpu',
)
