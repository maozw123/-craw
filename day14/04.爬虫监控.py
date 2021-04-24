from redis import Redis
import pymongo
import smtplib
from email.mime.text import MIMEText

r = Redis('127.0.0.1', '6379')
# 获取任务总数
def total_task():
    value=r.get('total_task')
    return value


# 获取当前未执行完的任务总数
def finished_task():
    value=r.lrange('taoche:start_urls',0,-1)
    return len(value)

# 爬取的数据量
def data_count():
    client=pymongo.MongoClient()
    db=client['SC']
    data=db['cars'].find()
    return len(list(data))

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
    content=('总任务数量为：'+str(total)+'\n'+'任务完成量'+str(finished/int(total)*100)+'\n+''当前已经爬取到的数据总量'+str(nums))
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
    # 总任务数
    total=total_task()
    print('总任务数量为：',total)

    # 获取当前已经执行完的任务总数
    unfinish=finished_task()
    print(unfinish)
    finished=int(total)-int(unfinish)
    print('任务完成量',finished/int(total)*100)

    #数据量
    nums=data_count()
    print('当前已经爬取到的数据总量',nums)

    s = send_email()
