import secrets


def main():
    """
    Python secrets 模块使用方法演示
    secrets 模块用于生成加密安全的随机数，适用于管理密码、账户认证、安全令牌等场景
    """

    print("=== secrets 模块使用方法演示 ===")

    # 1. 生成安全的十六进制令牌
    # token_hex(n) 生成 n 字节的随机数，返回 2n 位的十六进制字符串
    token_hex: str = secrets.token_hex(16)  # 16字节 = 32位十六进制字符
    print(f"1. 十六进制安全令牌 (16字节): {token_hex}")
    print(f"   长度: {len(token_hex)} 字符")

    # 2. 生成安全的URL安全令牌
    # token_urlsafe(n) 生成 n 字节的随机数，返回URL安全的Base64编码字符串
    token_url: str = secrets.token_urlsafe(16)  # 16字节，URL安全
    print(f"2. URL安全令牌 (16字节): {token_url}")
    print(f"   长度: {len(token_url)} 字符")
    print("   用途: 密码重置链接、会话ID等")

    # 3. 生成随机字节
    # token_bytes(n) 生成 n 字节的随机字节串
    random_bytes: bytes = secrets.token_bytes(16)
    print(f"3. 随机字节串 (16字节): {random_bytes}")
    print(f"   类型: {type(random_bytes)}")
    print(f"   长度: {len(random_bytes)} 字节")

    # 4. 安全地随机选择序列中的元素
    # secrets.choice(sequence) 从序列中安全地随机选择一个元素
    choices = ["apple", "banana", "cherry", "date", "elderberry"]
    selected: str = secrets.choice(choices)
    print(f"4. 从列表中随机选择: {selected}")
    print(f"   原始列表: {choices}")

    # 5. 比较令牌（防时序攻击）
    # secrets.compare_digest(a, b) 安全比较两个字符串/字节，防止时序攻击
    token1 = "user_token_12345"
    token2 = "user_token_12345"
    token3 = "user_token_67890"

    print("5. 安全令牌比较:")
    print(f"   比较相同令牌: {secrets.compare_digest(token1, token2)}")
    print(f"   比较不同令牌: {secrets.compare_digest(token1, token3)}")
    print("   用途: 防止时序攻击的密码验证")

    # 6. 生成指定范围内的随机数
    # secrets.randbelow(n) 生成 0 到 n-1 之间的随机整数
    rand_num = secrets.randbelow(100)
    print(f"6. 生成0-99的随机数: {rand_num}")

    # secrets.randbits(k) 生成 k 位随机整数
    rand_bits = secrets.randbits(8)  # 8位 = 0-255
    print(f"   生成8位随机整数: {rand_bits}")

    # 7. 实际应用示例：生成临时密码
    def generate_temp_password(length=12):
        """生成包含大小写字母和数字的临时密码"""
        import string

        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        return password

    temp_password = generate_temp_password(16)
    print(f"7. 生成的临时密码: {temp_password}")
    print(f"   密码长度: {len(temp_password)} 字符")

    # 8. 实际应用示例：生成API密钥
    def generate_api_key():
        """生成API密钥"""
        prefix = "sk_"
        random_part = secrets.token_urlsafe(32)
        return f"{prefix}{random_part}"

    api_key = generate_api_key()
    print(f"8. 生成的API密钥: {api_key}")
    print("   格式: 前缀 + 32字节随机部分")

    # 9. 实际应用示例：生成验证码
    def generate_verification_code(length=6):
        """生成数字验证码"""
        digits = "0123456789"
        return "".join(secrets.choice(digits) for _ in range(length))

    verification_code = generate_verification_code()
    print(f"9. 生成的验证码: {verification_code}")
    print("   用途: 短信验证、邮箱验证等")

    print("=== 演示完成 ===")
    print("注意事项:")
    print("- secrets模块专门用于密码学相关的安全随机数生成")
    print("- 不要使用random模块处理密码、令牌等安全敏感数据")
    print("- token_hex/token_urlsafe/token_bytes的参数是字节数，不是最终字符串长度")
    print("- compare_digest可以防止时序攻击，适用于密码验证")


if __name__ == "__main__":
    main()
