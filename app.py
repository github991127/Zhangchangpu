"""桌面入口：启动 Flask 服务并在 PyWebView 窗口中打开。

本文件是桌面版入口。它会先启动一个后台线程运行 Flask 服务，
然后使用 PyWebView 创建一个本地窗口加载前端页面。关闭窗口后进程结束。

运行方式：
    python app.py
"""
import socket
import threading
import time
import webview

from routes import create_app
from utils.port import find_free_port


def _wait_for_server(host: str, port: int, timeout: float = 5.0) -> bool:
    """轮询等待 Flask 服务开始监听指定端口。

    Args:
        host: 服务监听地址。
        port: 服务监听端口。
        timeout: 最长等待秒数。

    Returns:
        在超时前成功连接返回 True，否则返回 False。
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.1):
                return True
        except OSError:
            # 服务尚未就绪，短暂等待后重试
            time.sleep(0.1)
    return False


def main():
    """桌面版启动入口。"""
    # 1. 寻找空闲端口，避免与其他本地服务冲突
    port = find_free_port()
    host = '127.0.0.1'
    app = create_app()

    # 2. 在后台线程启动 Flask 服务
    #    daemon=True 保证主窗口关闭时服务线程自动结束
    server = threading.Thread(
        target=lambda: app.run(host=host, port=port, threaded=True),
        daemon=True,
    )
    server.start()

    # 3. 等待 Flask 就绪，避免窗口打开后页面不可访问
    if not _wait_for_server(host, port):
        print('错误：Flask 服务未能启动')
        return

    # 4. 创建 PyWebView 桌面窗口
    url = f'http://{host}:{port}/'
    window = webview.create_window(
        title='张菖蒲 / 糜竺 点数辅助工具',
        url=url,
        width=1200,
        height=900,
        min_size=(800, 600),
        text_select=True,
    )
    webview.start()


if __name__ == '__main__':
    main()
