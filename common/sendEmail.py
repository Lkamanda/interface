import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import readConfig

readC = readConfig()


def send_mail_html(file):
    '''发送html内容邮件，非附件形式，即直接在邮件中显示html'''
    sender = readC.getConfig_email('mail_user')
    receiver = readC.getConfig_email('receiver')

    # 发送邮件主题
    t = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    subject = '自动化测试结果_' + t
    smtpserver = 'smtp.163.com'

    mail_user = readC.getConfig_email('mail_user')

    mail_pass = readC.getConfig_email('mail_pass')

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
    # att['Content-Disposition'] = 'attachment; filename={}.html'.format(subject)
    att['Content-Disposition'] = 'attachment; filename={}'.format(file)
    msg.attach(att)


    # 登录并发送邮件
    try:
        # 1-- 实例化smtp类
        smtp = smtplib.SMTP()
        # 2-- 链接smtp服务器
        smtp.connect(smtpserver)
        # 3登录服务器
        smtp.login(mail_user, mail_pass)
        # 4.设置发件人，收件人，邮件内容
        smtp.sendmail(sender, receiver, msg.as_string())

    except Exception as e:
        print('邮件发送失败', e)
    else:
        print('邮件发送成功')
    finally:
        smtp.quit()


def find_new_file(dir):
    # 将指定目录下文件添加到一个列表中返回
    file_lists = os.listdir(dir)
    # print(file_lists)
    # os.get.getatime(file)返回文件的最后修改时间
    # os.path.isdire(file) 判断file 是否为路径， 返回true， false
    file_lists.sort(key=lambda fn: os.path.getatime(dir + "\\" + fn) if not os.path.isdir(dir +"\\"+ fn)else 0)
    # print(file_lists)
    print(file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print(file)
    return file


if __name__ == '__main__':
    dir = r"C:\Users\zhoujialin\PycharmProjects\interface\testReport"
    send_mail_html(file=find_new_file(dir))




