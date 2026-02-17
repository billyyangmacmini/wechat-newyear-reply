#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信拜年自动回复 - 风格管理模块
"""

import random
import os

class StyleManager:
    """管理回复风格"""
    
    def __init__(self, style="formal"):
        self.style = style
        self.replies = self._load_replies()
    
    def _load_replies(self):
        """加载回复模板"""
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        if self.style == "formal":
            file_path = os.path.join(base_path, "data", "formal_replies.txt")
        else:
            file_path = os.path.join(base_path, "data", "humor_replies.txt")
        
        replies = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    replies.append(line)
        
        return replies
    
    def get_random_reply(self):
        """获取随机回复"""
        return random.choice(self.replies)
    
    def get_reply(self, index=None):
        """获取指定或随机回复"""
        if index is not None and 0 <= index < len(self.replies):
            return self.replies[index]
        return self.get_random_reply()
    
    def set_style(self, style):
        """设置风格"""
        if style in ["formal", "humor"]:
            self.style = style
            self.replies = self._load_replies()
            return True
        return False
    
    def get_style(self):
        """获取当前风格"""
        return self.style


if __name__ == "__main__":
    # 测试
    sm = StyleManager("formal")
    print("正式风格:", sm.get_random_reply())
    
    sm.set_style("humor")
    print("幽默风格:", sm.get_random_reply())
