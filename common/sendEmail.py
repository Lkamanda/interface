import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import readConfig

readC = readConfig()


def send_mail_html(file):
    '''发送html内容邮件，非附件形式，即直接在邮件中显示html'''

    sender = readConfig.getConfig_email('mail_user')
    receiver = readConfig.getConfig_email('receiver')

    # 发送邮件主题
    t = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    subject = '自动化测试结果_'

    mail_user = readConfig.getConfig_email('mail_user')
    mail_pass = readConfig.getConfig_email('mail_pass')

    # 读取html文件内容
    with open(file, 'rb') as f:
        mail_body = f.read()

    # 组装邮件内容和标题，中文需要参数‘utf-8’
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(subject, "utf-8")
    msg['from'] = sender
    msg['to'] = receiver

    # 添加邮邮件内容
    att = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename={}.html'.format(subject)
    msg.attach(att)

    # 登录并发送邮件
    try:
        # 1-- 实例化smtp类
        smtp = smtplib.SMTP()
        # 2-- 链接smtp服务器



# https://github.com/rainshine1190/VIPtest2/blob/master/Pra_email/%E5%8F%91%E9%80%81html%E9%99%84%E4%BB%B6%E9%82%AE%E4%BB%B6.py