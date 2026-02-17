#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信拜年自动回复 - 消息发送模块
跨平台支持: Windows + macOS
"""

import os
import sys
import time
import platform
import subprocess

class MessageSender:
    """消息发送器"""
    
    def __init__(self):
        self.system = platform.system()
        print(f"🖥️ 消息发送器 - 系统: {self.system}")
    
    def send_message(self, message):
        """
        发送消息到当前微信聊天窗口
        """
        if self.system == "Darwin":  # macOS
            return self._send_macos(message)
        else:  # Windows
            return self._send_windows(message)
    
    def _send_macos(self, message):
        """macOS: 使用 AppleScript 发送消息"""
        
        # 将消息中的引号转义
        escaped_message = message.replace('"', '\\"')
        
        apple_script = f'''
        tell application "System Events"
            tell process "WeChat"
                -- 点击微信输入框
                keystroke "v" using {command down}  -- 粘贴
                delay 0.5
                
                -- 发送消息
                keystroke return
            end tell
        end tell
        '''
        
        # macOS 发送流程:
        # 1. 将消息复制到剪贴板
        # 2. 切换到微信窗口
        # 3. Cmd+V 粘贴
        # 4. Return 发送
        
        try:
            import pyperclip
            pyperclip.copy(message)
            
            # 使用 osascript 执行 AppleScript
            script = f'''
            tell application "System Events"
                keystroke "v" using command down
                delay 0.3
                keystroke return
            end tell
            '''
            
            subprocess.run(["osascript", "-e", script], check=True)
            print(f"✅ 消息已发送: {message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ AppleScript 执行失败: {e}")
            return False
        except ImportError:
            print("⚠️ 请安装 pyperclip: pip install pyperclip")
            return False
        except Exception as e:
            print(f"❌ 发送失败: {e}")
            return False
    
    def _send_windows(self, message):
        """Windows: 使用 pyautogui 发送消息"""
        try:
            import pyautogui
            import pyperclip
            
            # 复制消息
            pyperclip.copy(message)
            
            # 粘贴并发送
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.3)
            pyautogui.press('enter')
            
            print(f"✅ 消息已发送: {message}")
            return True
            
        except ImportError as e:
            print(f"❌ 请安装依赖: pip install pyautogui pyperclip")
            return False
        except Exception as e:
            print(f"❌ 发送失败: {e}")
            return False
    
    def activate_wechat(self):
        """激活微信窗口"""
        if self.system == "Darwin":
            subprocess.run(["osascript", "-e", 'tell application "WeChat" to activate'])
        else:
            import pyautogui
            wechat = pyautogui.getWindowsWithTitle("微信")
            if wechat:
                wechat[0].activate()


if __name__ == "__main__":
    sender = MessageSender()
    
    # 测试发送
    test_message = "🎊 测试消息：新春快乐！"
    print(f"\n🧪 测试发送: {test_message}")
    sender.send_message(test_message)
