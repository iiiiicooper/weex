---
name: weex-api
description: 该技能允许 AI Agent 通过 WEEX API V3 进行现货和合约交易、查询账户余额、获取行情数据等。当用户提到“查询 WEEX 余额”、“在 WEEX 下单”或“获取 WEEX 行情”时调用。
version: 1.0.0
---

# WEEX API V3 Skill

## 概览

WEEX API V3 提供 REST 接口，用于现货（Spot）和合约（Contract）交易、行情获取及账户管理。

- **现货域名**: `https://api-spot.weex.com`
- **合约域名**: `https://api-contract.weex.com`
- **鉴权方式**: HMAC SHA256 签名（私有接口需要）
- **频率限制**: 公共接口 20次/2s (每 IP)；私有接口根据 API Key 限制

## 配置设置

在 `~/.openclaw/openclaw.json` 的 `env` 字段中添加凭证：

```json
{
  "env": {
    "WEEX_API_KEY": "your-api-key",
    "WEEX_SECRET_KEY": "your-secret-key",
    "WEEX_PASSPHRASE": "your-passphrase"
  }
}
```

## 鉴权头 (Authentication Headers)

私有接口需在 Header 中包含以下字段：

| Header | 说明 |
|--------|------|
| `ACCESS-KEY` | API Key |
| `ACCESS-SIGN` | Base64(HmacSHA256(timestamp + METHOD + path_with_query + body, secret)) |
| `ACCESS-TIMESTAMP` | 毫秒时间戳 |
| `ACCESS-PASSPHRASE` | API 口令 |
| `Content-Type` | `application/json` (仅 POST) |

## 常用操作速查

| 意图 | 方法 | 端点 |
|------|------|------|
| 获取服务器时间 | GET | `/api/v3/spot/public/time` |
| 查询账户信息 | GET | `/api/v3/spot/account/assets` |
| 获取最新成交价 | GET | `/api/v3/spot/market/tickers` |
| 获取 K 线数据 | GET | `/api/v3/spot/market/candles` |
| 下单 | POST | `/api/v3/spot/trade/order` |
| 撤单 | POST | `/api/v3/spot/trade/cancel-order` |
| 查询当前挂单 | GET | `/api/v3/spot/trade/open-orders` |

## 响应处理

WEEX 响应遵循以下格式：

```json
{
  "code": "0",
  "msg": "success",
  "data": [...]
}
```

- `code: "0"` 或 `"00000"` 表示成功。
- 其他代码表示错误，详见 `references/error-codes.md`。

## 示例代码

请参考 `examples/` 目录下的 Python 脚本，使用 `scripts/weex_auth.py` 进行请求。
