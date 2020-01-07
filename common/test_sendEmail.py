from smtplib import SMTP
import smtplib, time, os
from common.readConfig import readConfig
from email.mime.text import MIMEText
from email.header import Header

readC = readConfig()


def sendEmail():
    ''' 发送html内容邮件 '''
    # 发送邮件邮箱
    sender = readC.getConfig_email('sender')
    # 接收邮箱
    receiver = readC.getConfig_email('receiver')

    # 发送邮箱主题
    t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    print(t)
    subject = '接口自动化测试结果' + t

    # 发送邮件服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户/密码
    mail_user = readC.getConfig_email('mail_user')

    mail_pass = readC.getConfig_email('mail_pass')

    content = 'python 发送邮件测试'

    # 第二步 组装邮件内容和标题，中文需要参数‘utf-8’
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # 第三步 登录并发送邮件
    try:
        # 1-- 实例化smtp 类
        smtp = smtplib.SMTP()
        # 2-- 连接stmp服务器
        smtp.connect(smtpserver)
        # 3--登录邮箱
        smtp.login(mail_user, mail_pass)
        # 设置发件人，收件人，邮箱内容
        smtp.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print('邮件发送失败', e)
    else:
        print('邮件发送成功')
    finally:
        smtp.quit()


if __name__ == '__main__':
    sendEmail()


