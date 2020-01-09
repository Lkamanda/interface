import smtplib
import time
import os
from email.mime.text import MIMEText
from common.readConfig import readConfig
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail_html(email_dir):
    '''发送html内容邮件，非附件形式，即直接在邮件中显示html'''
    readC = readConfig()
    sender = readC.getConfig_email('sender')
    print(sender)
    receiver = readC.getConfig_email('receiver')

    # 发送邮件主题
    t = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    subject = '接口自动化测试结果_' + t

    # 使用smtp服务
    smtpserver = readC.getConfig_email('mail_host')

    mail_user = readC.getConfig_email('mail_user')

    mail_pass = readC.getConfig_email('mail_pass')

    # 开始打包邮件
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # 邮件content
    file = r"{}".format(find_new_file(dir=email_dir))
    pureText = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
    msg.attach(pureText)

    # 添加邮件附件
    att = MIMEApplication(open(file, 'rb').read())
    # att.add_header('Content-Disposition', 'p_w_upload', file_name='interfaceReport.html')
    att.add_header('Content-Disposition', 'p_w_upload', filename='interface.html')
    msg.attach(att)
    try:
        server = smtplib.SMTP(smtpserver)
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print('发送邮件成功')
    except Exception as e:
        print('发送邮件失败')
        print(e)


def find_new_file(dir):
    # 将指定目录下文件添加到一个列表中返回
    file_lists = os.listdir(dir)
    # print(file_lists)
    # os.get.getatime(file)返回文件的最后修改时间
    # os.path.isdire(file) 判断file 是否为路径， 返回true， false
    file_lists.sort(key=lambda fn: os.path.getatime(dir + "\\" + fn) if not os.path.isdir(dir +"\\"+ fn)else 0)
    # print(file_lists)

    file = os.path.join(dir, file_lists[-1])

    return file


if __name__ == '__main__':
    dir = r"C:\Users\zhoujialin\PycharmProjects\interface\testReport"

    send_mail_html(dir)


















