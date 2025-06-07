import zmail
import os
EMAIL_INFO = {
        'username': '215687736@qq.com',  # 切换成你自己的地址
        'password': '授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }
report_path = os.path.join(os.path.dirname(__file__),'report.html')
# print(report_path)
def send_mail():
    with open(report_path,'r') as f:
        content_html = f.read()
    try:
        message = {
            'from': EMAIL_INFO['username'],
            'subject': "测试报告",
            'content_html': content_html,
            'attachments': [],
        }
        server = zmail.server(*EMAIL_INFO.values())
        server.send_mail("215687736@qq.com",message)
        server.quit()
    except Exception as e:
        print("Error: 无法发送邮件",e)



if __name__ == '__main__':
    send_mail()
