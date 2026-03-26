# openclaw-weex-api-skill

一个 [OpenClaw](https://openclaw.ai) Agent Skill，让 AI Agent 能够通过 WEEX 官方 REST API V3 与 [WEEX](https://www.weex.com) 加密货币交易所进行交互。

---

## 功能概述

该 Skill 教会 OpenClaw Agent 如何：

- 查询实时市场数据（价格、K 线、深度）
- 管理账户资产
- 下单、撤单
- 查询订单历史和成交明细

当用户说"查一下我的 WEEX 账户余额"或"在 WEEX 下一个 BTC 限价买单"时，Agent 会自动加载该 Skill 的上下文，生成正确的、带鉴权的 API 调用。

---

## 目录结构

```
openclaw-weex-api-skill/
├── SKILL.md                          # OpenClaw Skill 定义（frontmatter + 指引）
├── scripts/
│   └── weex_auth.py                  # 鉴权/请求工具
├── examples/
│   ├── get-balance.py                # 打印账户余额
│   └── get-server-time.py            # 获取服务器时间
└── references/
    └── error-codes.md                # 错误码参考
```

---

## 配置

在 `~/.openclaw/openclaw.json` 的顶级 `env` 字段中添加 WEEX API 凭证：

```json
{
  "env": {
    "WEEX_API_KEY": "your-api-key",
    "WEEX_SECRET_KEY": "your-secret-key",
    "WEEX_PASSPHRASE": "your-passphrase"
  }
}
```

---

## 依赖

```
requests
```

安装：

```bash
pip install requests
```

需要 Python 3.10+。
