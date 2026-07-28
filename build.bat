@echo off
chcp 65001 >nul
echo 开始构建 张菖蒲/糜竺 桌面版...

REM 1. 清理旧构建
if exist "dist" (
    echo 清理 dist/ ...
    rmdir /s /q "dist"
)
if exist "build" (
    echo 清理 build/ ...
    rmdir /s /q "build"
)
if exist "__pycache__" (
    echo 清理 __pycache__/ ...
    rmdir /s /q "__pycache__"
)

REM 2. 安装/校验依赖
python -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo 依赖安装失败。
    exit /b 1
)

REM 3. 运行 PyInstaller
pyinstaller zhangchangpu.spec --clean --noconfirm
if errorlevel 1 (
    echo PyInstaller 构建失败。
    exit /b 1
)

REM 4. 确认输出
if exist "dist\zhangchangpu\zhangchangpu.exe" (
    echo 构建完成：dist\zhangchangpu\
) else (
    echo 构建失败，未找到 dist\zhangchangpu\zhangchangpu.exe。
    exit /b 1
)
