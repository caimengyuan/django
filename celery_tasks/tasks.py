# 使用celery
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

# 在任务处理者一端加这些（可以在终端输入）
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dailyfresh.settings")
django.setup()  # 初始化

# 创建一个celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/0')

# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    # 发邮件
    subject = '天天生鲜欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    message_html = '<h1>%s，欢迎您成为注册会员</h1>请点击下面得链接激活你的账户</br><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
    send_mail(subject, message, sender, receiver, html_message=message_html, fail_silently=False)