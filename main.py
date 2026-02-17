#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信拜年自动回复脚本
检测微信拜年消息，自动发送祝福回复
"""

import os
import sys
import time
import yaml
import signal

# 添加 src 目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.style import StyleManager

class WechatNewyearReply:
    """微信拜年自动回复"""
    
    def __init__(self, config_file="config.yaml"):
        self.config = self._load_config(config_file)
        self.style_manager = StyleManager(self.config.get("style", "formal"))
        self.running = True
        
        # 设置信号处理
        signal.signal(signal.SIGINT, self._handle_exit)
        signal.signal(signal.SIGTERM, self._handle_exit)
    
    def _load_config(self, config_file):
        """加载配置文件"""
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, config_file)
        
        if not os.path.exists(config_path):
            print(f"❌ 配置文件不存在: {config_path}")
            sys.exit(1)
        
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def _handle_exit(self, signum, frame):
        """处理退出信号"""
        print("\n👋 收到退出信号，正在停止...")
        self.running = False
    
    def set_style(self, style):
        """设置回复风格"""
        self.style_manager.set_style(style)
        print(f"✅ 已切换为: {style} 风格")
    
    def is_in_do_not_disturb(self):
        """检查是否在免打扰时段"""
        if not self.config.get("do_not_disturb", {}).get("enabled", False):
            return False
        
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        
        start = self.config["do_not_disturb"]["start"]
        end = self.config["do_not_disturb"]["end"]
        
        return start <= now <= end
    
    def check_for_newyear_messages(self):
        """
        检测拜年消息
        TODO: 实现微信消息检测逻辑
        """
        # 这里需要实现微信消息检测
        # 暂时返回模拟结果
        return False
    
    def send_reply(self, message):
        """
        发送回复
        TODO: 实现微信消息发送逻辑
        """
        # 这里需要实现微信消息发送
        print(f"📤 发送回复: {message}")
        return True
    
    def run(self):
        """主循环"""
        print("🎊 微信拜年自动回复已启动！")
        print(f"📝 当前风格: {self.style_manager.get_style()}")
        print(f"⏰ 检测间隔: {self.config.get('check_interval', 2)} 秒")
        print("-" * 40)
        
        while self.running:
            try:
                # 检查免打扰
                if self.is_in_do_not_disturb():
                    time.sleep(60)
                    continue
                
                # 检测消息
                if self.check_for_newyear_messages():
                    reply = self.style_manager.get_random_reply()
                    self.send_reply(reply)
                
                # 等待
                interval = self.config.get("check_interval", 2)
                time.sleep(interval)
                
            except Exception as e:
                print(f"❌ 错误: {e}")
                time.sleep(5)
        
        print("👋 已停止")


def select_style():
    """运行时选择风格"""
    print("\n" + "=" * 50)
    print("🎊 微信拜年自动回复 - 风格选择")
    print("=" * 50)
    print()
    print("请选择回复风格：")
    print()
    print("  1. 🌟 温馨正式")
    print("     适用：同事、客户、长辈")
    print("     示例：感谢您的祝福，祝您新春快乐，马年大吉！🐎✨")
    print()
    print("  2. 😄 轻松幽默")
    print("     适用：朋友、同学")
    print("     示例：新年好呀！祝你马年666，事事顺心！🎉😄")
    print()
    
    while True:
        choice = input("请输入 (1/2): ").strip()
        
        if choice == "1":
            print("\n✅ 已选择：温馨正式")
            return "formal"
        elif choice == "2":
            print("\n✅ 已选择：轻松幽默")
            return "humor"
        else:
            print("❌ 无效选择，请输入 1 或 2")


def main():
    """主入口"""
    config_file = "config.yaml"
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("🎊 微信拜年自动回复")
            print("\n用法: python main.py [配置文件]")
            print("\n示例:")
            print("  python main.py              # 使用默认 config.yaml")
            print("  python main.py myconfig.yaml  # 使用自定义配置")
            sys.exit(0)
        else:
            config_file = sys.argv[1]
    
    # 运行时选择风格
    style = select_style()
    
    # 加载配置
    app = WechatNewyearReply(config_file)
    app.set_style(style)
    
    app.run()


if __name__ == "__main__":
    main()
