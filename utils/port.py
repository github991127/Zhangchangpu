"""空闲端口检测工具。"""
import socket


def find_free_port(host: str = '127.0.0.1') -> int:
    """让操作系统分配一个可用端口并立即释放。

    Args:
        host: 监听地址，默认 127.0.0.1。

    Returns:
        可用的端口号。
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, 0))
        return sock.getsockname()[1]
