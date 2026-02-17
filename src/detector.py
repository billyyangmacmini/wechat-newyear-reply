#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信拜年自动回复 - 消息检测模块
跨平台支持: Windows + macOS
"""

import os
import sys
import time
import platform

class MessageDetector:
    """消息检测器"""
    
    def __init__(self):
        self.system = platform.system()
        print(f"🖥️ 检测到系统: {self.system}")
        
        if self.system == "Darwin":  # macOS
            self._init_macos()
        else:  # Windows
            self._init_windows()
    
    def _init_macos(self):
        """macOS 初始化"""
        try:
            # macOS 使用 AppleScript
            print("✅ macOS: 使用 AppleScript")
        except Exception as e:
            print(f"⚠️ macOS 初始化警告: {e}")
    
    def _init_windows(self):
        """Windows 初始化"""
        try:
            # Windows 使用 pyautogui
            import pyautogui
            print("✅ Windows: 使用 pyautogui")
        except ImportError:
            print("⚠️ 请安装 pyautogui: pip install pyautogui")
    
    def get_wechat_messages(self):
        """
        获取微信最新消息
        返回: 消息列表 [{'sender': str, 'content': str}]
        """
        if self.system == "Darwin":
            return self._get_messages_macos()
        else:
            return self._get_messages_windows()
    
    def _get_messages_macos(self):
        """macOS: 使用 AppleScript 获取微信消息"""
        script = '''
        tell application "WeChat"
            if exists window 1 then
                set msgList to {}
                tell window 1
                    try
                        set chatContent to ""
                        -- 注意: AppleScript 访问微信内容有限制
                        -- 实际使用可能需要辅助功能权限
                    end try
                end tell
            end if
        end tell
        '''
        
        # macOS 微信自动化需要用户授权辅助功能
        # 首次使用需要在 系统设置 > 隐私与安全性 > 辅助功能 中授权
        print("ℹ️ macOS 提示:")
        print("   首次使用需要在【系统设置 > 隐私与安全性 > 辅助功能】")
        print("   中授权 Python/你的编辑器 访问微信")
        
        # 返回模拟数据（实际需要用户授权后才能读取）
        return []
    
    def _get_messages_windows(self):
        """Windows: 获取微信消息"""
        try:
            import pyautogui
            # Windows 方案: 截图 + OCR 识别消息
            # 这里需要配合 OCR 库使用
            return []
        except ImportError:
            print("❌ 请安装 pyautogui: pip install pyautogui")
            return []
    
    def is_wechat_open(self):
        """检查微信是否运行"""
        if self.system == "Darwin":
            script = '''
            tell application "System Events"
                set wechatRunning to exists process "WeChat"
            end tell
            '''
            # 检查微信进程
            import subprocess
            result = subprocess.run(
                ["pgrep", "-x", "WeChat"],
                capture_output=True
            )
            return result.returncode == 0
        else:
            import pyautogui
            try:
                # 尝试查找微信窗口
                return pyautogui.getWindowsWithTitle("微信") != []
            except:
                return False


if __name__ == "__main__":
    detector = MessageDetector()
    print(f"\n微信运行中: {detector.is_wechat_open()}")
