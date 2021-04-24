
import smtplib
from email.mime.text import MIMEText

def send_email():
    # 一：准备环节
    # 接收方邮件地址
    receivers=['liulidong@tju.edu.cn']

    # 发送方邮件地址
    msg_from='1262013975@qq.com'

    passwd='vsdmzwsjorqlfeda'

    # 邮件内容
    # 主题
    subject='毛志文'
    # 正文
    content='刘老师真帅'
    # 使用MIMEText对邮件进行封装
    msg=MIMEText(content,'plain','utf-8')
    # 邮件数据包含以上内容
    msg['subject']=subject
    msg['From']=msg_from
    msg['To']=','.join(receivers)

    # 二：发送环节
    try:
        smtp=smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.login(msg_from,passwd)#注意登录邮箱使用授权码发送
        smtp.sendmail(msg_from,msg['To'].strip(','),msg.as_string())
        print('发送成功')
    except:
        print('发送失败')

if __name__ == '__main__':
    s=send_email()