#!/usr/bin/env python
# mypy: ignore-errors

import os
import eel
from jinja2 import Environment, FileSystemLoader
from rviz_camera_manager.handlers.cam_actions import *  # noqa: F403
import rospkg

# Jinja2の設定
rospack = rospkg.RosPack()
package_path = rospack.get_path('rviz_camera_manager')
abs_path = os.path.join(package_path, 'src/rviz_camera_manager/templates')
os.makedirs(os.path.join(package_path, 'dist/web'), exist_ok=True)
env = Environment(loader=FileSystemLoader(abs_path))

# HTMLのレンダリング関数
def render_template(template_name, **context):
    template = env.get_template(template_name)
    rendered = template.render(**context)

    # 生成したHTMLをdist/web/フォルダに保存
    with open(os.path.join(package_path, f'dist/web/{template_name}'), 'w', encoding='utf-8') as f:
        f.write(rendered)

if __name__ == '__main__':
    render_template('index.html', title='視点管理ツール')

    options = {
        "host": "localhost",
        "port": 8000,
        'cmdline_args': ["--no-sandbox"],
        'size': (800, 600)
    }
    dist_path = os.path.join(package_path, 'dist/web')
    print("Starting Eel app...")
    print("  dist path: ", dist_path)
    print("  hosted at:", f"http://{options['host']}:{options['port']}")
    eel.init(dist_path)
    eel.start('index.html', **options) 