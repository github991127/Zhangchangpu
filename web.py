"""Web 入口：启动 Flask 服务并自动打开系统默认浏览器。

本文件是网页版入口。它会自动寻找一个空闲端口，启动 Flask 服务，
并用系统默认浏览器打开首页。服务会在前台持续运行，直到按 Ctrl+C 停止。

运行方式：
    python web.py
"""
import webbrowser

from routes import create_app
from utils.port import find_free_port


def main():
    """网页版启动入口。"""
    # 1. 寻找空闲端口，避免与现有端口冲突
    port = find_free_port()
    host = '127.0.0.1'
    url = f'http://{host}:{port}/'

    # 2. 在后台打开浏览器，使用 new=2 在新标签页打开
    #    此调用不会阻塞服务启动
    webbrowser.open(url, new=2)

    # 3. 启动 Flask 服务（前台阻塞运行）
    app = create_app()
    print(f'服务已启动：{url}')
    app.run(host=host, port=port, threaded=True)


if __name__ == '__main__':
    main()
