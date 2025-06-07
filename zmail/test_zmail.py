# 测POP3和SMTP功能：
import zmail

server = zmail.server('215687736@qq.com', 'ydxfdadlqphobhhd') # 邮箱账号和应用专用密码

# if server.smtp_able():
#     print(True)
#     # SMTP function.
# if server.pop_able():
#     print(True)
import os
report_path = os.path.join(os.path.dirname(__file__),'report.html')
with open(report_path, 'r', encoding="utf-8") as f:
    content_html = f.read()

mail = {
    'subject': '邮件主题：Success!',  # Anything you want.
    # 'content_text': '邮件正文内容：This message from zmail! QQ交流群:717225969 ',  # Anything you want.
    'content_html': content_html
}

server = zmail.server('215687736@qq.com',
                      'ydxfdadlqphobhhd',
                      smtp_host="smtp.qq.com",
                      smtp_port=465)
# server.send_mail('215687736@qq.com', mail)
# server.quit()
# 发送邮件
for k,v in mail.items():
    print(k,v)