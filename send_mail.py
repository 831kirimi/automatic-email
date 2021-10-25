#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  import datetime
  import smtplib, ssl
  from email.mime.text import MIMEText
  import sys, io
  sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

  # set gmail account
  gmail_account = "***@****"
  gmail_password = "*******"

  # set To and Cc
  to = "****@****,****@****" 
  cc = "****@****" 

  name = "kirimi"
  today_date = datetime.date.today()

  next_workday = today_date + datetime.timedelta(days=1)
  
  subject = "【日報】{0:%Y%m%d} {1}".format(today_date,name)
  f = open('body.html', 'r', encoding='UTF-8')
  body = f.read()
  body = body.format(name,next_workday.strftime("%#m月%#d日"))

  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = to
  msg["Cc"] = cc
  msg["From"] = gmail_account

  server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
  server.login(gmail_account, gmail_password)
  server.send_message(msg)
  print("Email was sent successfully.")

  print(subject)
  print(body)
  print(msg)

if(__name__ == '__main__'):
  main()
