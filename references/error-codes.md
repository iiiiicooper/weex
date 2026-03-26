# WEEX API Error Codes

错误由两部分组成：错误代码 (`code`) 和消息 (`msg`)。代码是通用的，但是消息可能会有所不同。

## 10xx - 常规服务器或网络问题
- `-1000` `UNKNOWN_ERROR`: 处理请求时发生未知错误。
- `-1054` `SYSTEM_ERROR`: 系统错误，请稍后重试。

## 10xx - 认证/访问
- `-1040` `ACCESS_KEY_EMPTY`: 请求头 ACCESS_KEY 不能为空。
- `-1041` `ACCESS_SIGN_EMPTY`: 请求头 ACCESS_SIGN 不能为空。
- `-1042` `ACCESS_TIMESTAMP_EMPTY`: 请求头 ACCESS_TIMESTAMP 不能为空。
- `-1043` `INVALID_ACCESS_TIMESTAMP`: 无效的 ACCESS_TIMESTAMP。
- `-1044` `INVALID_ACCESS_KEY`: 无效的 ACCESS_KEY。
- `-1045` `INVALID_CONTENT_TYPE`: 无效的 Content-Type，请使用 `application/json` 格式。
- `-1046` `ACCESS_TIMESTAMP_EXPIRED`: 请求时间戳已过期。
- `-1047` `API_AUTH_ERROR`: API 校验失败。
- `-1049` `API_KEY_OR_PASSPHRASE_INCORRECT`: API key 或 passphrase 不正确。
- `-1050` `USER_STATUS_FORBIDDEN`: 用户状态异常。
- `-1051` `PERMISSION_DENIED`: 权限被拒绝。
- `-1052` `INSUFFICIENT_PERMISSIONS`: 该操作所需权限不足。
- `-1053` `PERMISSION_VALIDATION_FAILED`: 权限校验失败。
- `-1055` `USER_AUTH_NOT_SAFE`: 用户必须绑定手机或谷歌验证器。
- `-1056` `ILLEGAL_IP`: 非法的 IP 地址。
- `-1057` `USER_LOCKED`: 用户账户已被锁定。
- `-1058` `NO_PERMISSION_TRADE_PAIR`: 没有权限交易此币对。

## 11xx - 请求参数
- `-1115` `INVALID_TIME_IN_FORCE`: 无效的 timeInForce。
- `-1116` `INVALID_ORDER_TYPE`: 无效的订单类型。
- `-1117` `INVALID_SIDE`: 无效的方向。
- `-1121` `INVALID_SYMBOL`: 无效的交易对。
- `-1128` `INVALID_PARAM_COMBINATION`: 可选参数组合无效。
- `-1135` `INVALID_JSON`: 无效的 JSON 请求。
- `-1140` `PARAM_VALIDATE_ERROR`: 参数校验失败。
- `-1141` `PARAM_EMPTY`: 参数不能为空。
- `-1142` `PARAM_ERROR`: 参数错误。
- `-1150` `REQUEST_METHOD_NOT_SUPPORTED`: 不支持的请求方法。
- `-1160` `DECIMAL_PRECISION_ERROR`: 小数精度错误。
- `-1170` `QUERY_TIME_OUT_OF_RANGE`: 查询时间超出范围。
- `-1171` `START_TIME_AFTER_END_TIME`: 开始时间不能大于结束时间。
- `-1180` `CLIENT_OID_LENGTH_ERROR`: client_oid 长度不得超过40，且不能包含特殊字符。
- `-1190` `FORBIDDEN_ACCESS`: 访问被禁止，请联系支持。

## 20xx - 现货配置/校验
- `-2007` `SPOT_SYMBOL_NOT_EXIST`: 交易对不存在。

## 22xx - 现货交易
- `-2200` `SPOT_ORDER_NOT_EXIST`: 订单不存在。

## 频率限制 (Rate Limits)
如果请求过于频繁，系统将自动限制请求，并在 HTTP Header 中返回 `429 Too Many Requests` 状态码。
- **公共接口**：如行情接口，统一限频为 2秒最多20个请求。
- **授权接口**：通过 apikey 限制授权接口的调用，参考每个接口的具体限频规则。
