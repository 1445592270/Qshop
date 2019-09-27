from alipay import AliPay
## 公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2kS6XyMGm59Bse/Ry7IuKBSpb4+fPvWMM0086a2zCiVgFzV44Yln/oGV/MUztd5JlH3Oqhv2ldMfCxLuppU9fgS/KqbCdaDMnlLLm9b5P5KYLzc58FU/LILfXpisncI9iIuQBfoDFF/AQrS1KZw0FWCr/y0V5xl2ky4bshVKGkgY8qKlJK2O0FR0tySvHNM/uyfvPcMSwlnm5EncRaHL0IE75pgFM5az1zKoVQ+6X6sZPOxKlZLlbhNyMHJaBnsIGKW7SAkdhyOljBemR/FF3YvAIIQacrBVKB0l/5oHMIvJJIG0Hc7q2SKgxlpoxrRAB8gyJo+mVRu/NnyVoX+TVwIDAQAB
-----END PUBLIC KEY-----"""
## 私钥
alipay_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2kS6XyMGm59Bse/Ry7IuKBSpb4+fPvWMM0086a2zCiVgFzV44Yln/oGV/MUztd5JlH3Oqhv2ldMfCxLuppU9fgS/KqbCdaDMnlLLm9b5P5KYLzc58FU/LILfXpisncI9iIuQBfoDFF/AQrS1KZw0FWCr/y0V5xl2ky4bshVKGkgY8qKlJK2O0FR0tySvHNM/uyfvPcMSwlnm5EncRaHL0IE75pgFM5az1zKoVQ+6X6sZPOxKlZLlbhNyMHJaBnsIGKW7SAkdhyOljBemR/FF3YvAIIQacrBVKB0l/5oHMIvJJIG0Hc7q2SKgxlpoxrRAB8gyJo+mVRu/NnyVoX+TVwIDAQABAoIBAC7L23V4Sftlmq0usLlOe2zmeSlNDqRt+uAo6C1lq2Q6fS6crU0Vq7E6UVD/asXMYdQvYPbBxg17VUWHipk2mBeDpwTa+ghEMHqlX7gK0CecI3rECW0IqeG+MWvTqfas5Yp3+an+X1in6s2idtD0B4qpzlaIcRC6Odz2XsPAosGdXC036pmSox/j4R6zFpcjPuqQS9AMYMsOVuWssvl4muMrMWBimAW7/2RO4C1v3DVZtoY+kRoHip/x9h8KLxXZlngUjsWi5VxhMhvg1BzKFFASi9rp/sKw8cqomNxlWuXwKmsW6b+JpQAwV28qIT7GlzHtyvwX68i4s96yKo7+9QECgYEA8xowCN7ki6yGTT5He2fi8PW84mBQb0qvcgIyF+7Q8PY8+zU/QohTCnHEQDcp2Y6H0ZkBPeA7FzD1XBDiAzvlmWG2b3Hw34fMzTbVS0CG5zDsMCf/lqwSzmUc4a2QQHUoq5afsatjZ7nZ0nS5jY+gyjZAst0szIHQxpDAQBUnCoECgYEA5dk/ZjBM3wT/DgJX7BUad14JqTeX+Q3Tx2X4yEDQhTnOsQp57jBkhvAYBRtwCrxeg2HfEr8PdoD0p4gnz/ezZcG4WXFPs7B5zI/fOWvWR/hhw4FBrIUfRpm1fDewZ7HNeTYKlkU/P2K+kH3Myz0OEV2i4ej4mQ/mVccFkkCLQdcCgYEAjbPRFgqem4/oBPRthFBs51nGTQopOIYHOGRxQKQTJLHTn/ZMtoJyLR9dbrT47vh20MToBWJD72O5UX4B0DLExaBAUDvRVOp6hZAVyjSFrhNFSVi3UeNhXu9vY1jhQcFJAKPe2Bh37AlYH6WsVwjGh7gSBHCJ4Xc189iCR5hM1oECgYEAvyWqietFIntfOWFNiTILrpVv52AqbJ7JLpxpBvCP+RuX/re9qw5nq6hj8WteBC+fUhfEkix+SYj47ZJXuaY/dTJjg06uf7sVr78+XtyFeZjghNwrp7OVzPrraQBPHg1J2bHNoCa6cJZH8JYOCD8gQeTjHojGpVQJs/Ate/FdXkUCgYAq13wVODoGBurIAnuzkO5A1tPHASMsh2OtK2Wv3hU9Rkz4QuNmP80ZnnDNgQHkWgI6Pm0AioKiZge2QE6Jjvao9KF6RxHTtU7u+1zytG97Z3DCWwaVWTeW7WDIVVrXwNgV2Yzrm+Ucdgm/YbRva1FusF276K3790AuPTsr2nW0yw==
-----END RSA PRIVATE KEY-----"""
## 实例化支付对象
alipay = AliPay(
    appid='2016101300674021',
    app_notify_url = None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
)
## 实例化订单
order_string = alipay.api_alipay_trade_page_pay(
    subject = '牛羊生鲜',   ## 交易主题
    out_trade_no = '100000000005',    ## 订单号
    total_amount = '1000000',     ## 交易总金额
    return_url=None,         ##  请求支付，之后及时回调的一个接口
    notify_url=None          ##  通知地址，
)
##   发送支付请求
## 请求地址  支付网关 + 实例化订单
result = "https://openapi.alipaydev.com/gateway.do?"+order_string
print(result)