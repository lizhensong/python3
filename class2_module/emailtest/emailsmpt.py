import smtplib
#smtp连接
from email.header import Header

from email.mime.text import MIMEText
#文本
from email.mime.multipart import MIMEMultipart
#附件
from email.mime.image import MIMEImage
#图片
from email.utils import parseaddr, formataddr

from_addr = 'li_zhen_song@sina.com'
password = '94380596ZHenSong'
to_addr = '965234670@qq.com'

msg = MIMEMultipart()
msg['From'] =formataddr((Header('李师傅','utf-8').encode(),'li_zhen_song@sina.com'))
#smtp.sina.com 会解析邮件正文内容，如果里面包含“from:XXX@sina.com”信息，与 msg [‘From’] 一致，就算作 match
msg['Subject'] = Header('来自李某人的问候', 'utf-8').encode()

#添加文本
msgtext=MIMEText('小鱼你好！洗好没？', 'plain', 'utf-8')
msg.attach(msgtext)

#添加html
html='<html><body><h1>小鱼你好！洗好没？</h1>' +'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'<p><img src="cid:0"></p>' +'</body></html>'
msghtml=MIMEText(html,'html','utf-8')
msg.attach(msghtml)

#添加文件发送附件
msgfile=MIMEText(open('123','rb').read(),'base64','utf-8')
msgfile["Content-Type"] = 'application/octet-stream'
msgfile["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(msgfile)

#添加图片文件
msgfile=MIMEText(open('123.png','rb').read(),'base64','utf-8')
msgfile["Content-Type"] = 'application/octet-stream'
msgfile["Content-Disposition"] = 'attachment; filename="123.png"'
msgfile['Content-ID'] = '<0>'
msg.attach(msgfile)

server = smtplib.SMTP('smtp.sina.com', 25)
server.starttls()
#smtp 加密
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()