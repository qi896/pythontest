from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import smtplib





#读取测试报告中的内容作为邮件的内容
with open("D:\xun.txt",'r',encoding='utf8') as f:
    mail_body = f.read()
#发件人地址
from_addr = '19983732827@163.com'
#收件人地址
to_addr = 'qishi@glacierxpress.com,'
#发送邮箱的服务器地址
mail_server = 'smtp.126.com'
#邮件的标题
subject = 'megav接口测试报告'
#发件人的邮箱地址
username = '19983732827@163.com'
password = '1902653704'
#邮箱的内容和标题
message = MIMEText(mail_body,'html','utf8')
message['Subject'] = Header(subject,charset='utf8')
#发送邮件
smtp = smtplib.SMTP()
smtp.connect(mail_server)
smtp.login(username,password)
smtp.sendmail(from_addr,to_addr.split(','),message.as_string())
smtp.quit()