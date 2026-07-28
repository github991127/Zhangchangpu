"""Flask 应用工厂与路由注册。

本模块负责创建 Flask 应用实例、注册业务蓝图、配置模板/静态目录，
并提供统一的全局错误处理。

使用方式：
    from routes import create_app
    app = create_app()
"""
import logging
import os
import traceback

from flask import Flask, jsonify, render_template, request, send_from_directory

from utils.resources import get_template_folder, get_static_folder, get_res_folder

# 限制请求体大小为 2KB，足够容纳 30 张牌及少量 JSON 包装
MAX_CONTENT_LENGTH = 2 * 1024


def create_app() -> Flask:
    """创建并配置 Flask 应用。

    该工厂函数完成以下工作：
    1. 使用 utils.resources 提供的路径配置 template_folder 与 static_folder，
       以同时兼容开发目录与 PyInstaller 打包后的运行环境。
    2. 注册张菖蒲与糜竺业务蓝图。
    3. 配置首页、图标与全局错误处理器。

    Returns:
        配置好的 Flask 应用实例。
    """
    # 1. 创建 Flask 实例，使用可跨环境解析的模板与静态目录
    app = Flask(
        __name__,
        template_folder=get_template_folder(),
        static_folder=get_static_folder(),
    )
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

    # 2. 注册业务蓝图
    #    所有 API 路由统一以 /api 为前缀
    from routes.zhangchangpu import bp as zhangchangpu_bp
    from routes.mizhu import bp as mizhu_bp

    app.register_blueprint(zhangchangpu_bp, url_prefix='/api')
    app.register_blueprint(mizhu_bp, url_prefix='/api')

    # 3. 首页路由：渲染 templates/index.html
    @app.route('/')
    def index():
        return render_template('index.html')

    # 4. 图标路由：浏览器标签页 / 窗口图标
    #    直接使用 res/image.ico，避免重复复制图标到 static
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            get_res_folder(), 'image.ico', mimetype='image/vnd.microsoft.icon'
        )

    # 5. 全局请求日志（仅记录 API 路径与方法，不记录敏感 payload）
    @app.before_request
    def log_request():
        if request.path.startswith('/api/'):
            logging.getLogger(__name__).info('%s %s', request.method, request.path)

    # 6. 全局错误处理：统一返回中文 JSON 提示
    @app.errorhandler(404)
    def not_found(_):
        return jsonify({'success': False, 'error': '请求的接口不存在'}), 404

    @app.errorhandler(500)
    def internal_error(exc):
        logging.getLogger(__name__).error('服务器内部错误：%s\n%s', exc, traceback.format_exc())
        return jsonify({'success': False, 'error': '服务器内部错误，请稍后重试'}), 500

    return app
