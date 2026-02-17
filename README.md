# 🎊 微信拜年自动回复脚本

自动检测微信拜年消息并发送祝福回复。

## 📋 功能

- ✅ 自动识别拜年消息（关键词检测）
- ✅ 自动发送祝福回复
- ✅ 支持文字 + emoji
- ✅ 两种风格切换（温馨正式 / 轻松幽默）
- ✅ **跨平台支持**: Windows + macOS 🍎

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置

编辑 `config.yaml`：

```yaml
# 回复风格: "formal" (温馨正式) 或 "humor" (轻松幽默)
style: "formal"

# 免打扰时段 (24小时制)
do_not_disturb:
  enabled: true
  start: "23:00"
  end: "08:00"
```

### 3. 运行

```bash
python main.py
```

## 🍎 macOS 使用说明

macOS 需要额外的辅助功能权限：

1. **首次运行前**，请打开 **系统设置 > 隐私与安全性 > 辅助功能**
2. **授权** 你的终端应用或 Python
3. 勾选 **"辅助功能"** 和 **"完全磁盘访问权限"**（如果需要）

如果运行时提示权限问题，请重启终端后重试。

## 📁 项目结构

```
wechat-newyear-reply/
├── README.md
├── config.yaml           # 配置文件
├── requirements.txt      # 依赖
├── main.py              # 主程序
├── src/
│   ├── detector.py     # 消息检测器
│   ├── sender.py       # 消息发送器
│   └── style.py        # 风格管理
├── data/
│   ├── formal_replies.txt   # 正式风格回复
│   └── humor_replies.txt    # 幽默风格回复
└── assets/
    └── emojis/         # 表情包资源
```

## 🎯 回复示例

### 温馨正式风格
- "感谢您的祝福，祝您新春快乐，龙年大吉！🐉✨"
- "谢谢！祝您和家人春节愉快，万事如意！🎊"

### 轻松幽默风格
- "新年好呀！祝你龙年666，事事顺心！🎉😄"
- "哈喽！新的一年也要元气满满哦！龙年冲鸭！🐉💪"

## ⚠️ 注意事项

### macOS
- 需要在 **系统设置 > 隐私与安全性 > 辅助功能** 中授权
- 微信需要保持登录状态
- 建议使用英文系统语言以获得最佳兼容性

### Windows
- 需要保持电脑开机
- 微信 PC 版需要保持登录

## 📝 License

MIT

---

Made with ❤️ for Chinese New Year!
