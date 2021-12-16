from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import random

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})

def HomePage(request):
    if request.method == 'GET':
        user = ''
        with open("session.txt", "r") as file:
            for line in file:
                user = line.strip('\n')
        status_data = ''
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == user:
                    status_data = row[5]
                    break
            if status_data == 'none':
                status_data = ''   
            output = ''
            output+='<table border=0 align=center width=100%><tr><td><img src=/static/profiles/'+user+'.png width=200 height=200></img></td>'
            output+='<td><font size=3 color=black>'+status_data+'</font></td><td><font size=6 color=black> Welcome : '+user+'</font></td></tr></table></br></br>'
            output+=getPostData()
            context= {'data':output}
            return render(request, 'UserScreen.html', context)

def getPostData():
    output = '<table border=1 align=center>'

    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select * FROM post")
        rows = cur.fetchall()
        for row in rows:
            username = row[0]
            post_id = str(row[1])
            image = row[2]
            name = row[3]
            topic = row[4]
            description = row[5]
            output+='<tr><td><font size=3 color=black>'+username+'</font></td>'
            output+='<td><img src=/static/post/'+post_id+'.png width=200 height=200></img></td>'
            output+='<td><font size=3 color=black>'+image+'</font></td>'
            output+='<td><font size=3 color=black>'+name+'</font></td>'
            output+='<td><font size=3 color=black>'+topic+'</font></td>'
            output+='<td><font size=3 color=black>'+description+'</font></td>'
            output+='<td><a href=\'PostComment?id='+post_id+'\'><font size=3 color=black>Click Here</font></a></td></tr>'
    output+="</table><br/><br/><br/><br/><br/><br/>"        
    return output

def EditProfile(request):
    if request.method == 'GET':
        output = ''
        user = ''
        with open("session.txt", "r") as file:
            for line in file:
                user = line.strip('\n')
        output = ''
        username = ''
        password = ''
        contact = ''
        email = ''
        address = ''
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register where username='"+user+"'")
            rows = cur.fetchall()
            for row in rows:
                username = row[0]
                password = row[1]
                contact = row[2]
                email = row[3]
                address = row[4]
        output+='<tr><td><b>Username</b></td><td><input type=text name=username style=font-family: Comic Sans MS size=30 value='+username+' readonly></td></tr>'
        output+='<tr><td><b>Password</b></td><td><input type=password name=password style=font-family: Comic Sans MS size=30 value='+password+'></td></tr>'
        output+='<tr><td><b>Contact&nbsp;No</b></td><td><input type=text name=contact style=font-family: Comic Sans MS size=20 value='+contact+'></td></tr>'
        output+='<tr><td><b>Email&nbsp;ID</b></td><td><input type=text name=email style=font-family: Comic Sans MS size=40 value='+email+'></td></tr>'
        output+='<tr><td><b>Address</b></td><td><input type=text name=address style=font-family: Comic Sans MS size=60 value='+address+'></td></tr>'
        context= {'data':output}
        return render(request, 'EditProfile.html', context)    

def Signup(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      contact = request.POST.get('contact', False)
      email = request.POST.get('email', False)
      address = request.POST.get('address', False)
      myfile = request.FILES['image']

      fs = FileSystemStorage()
      filename = fs.save('C:/Users/AISHWARYA THAKUR/Desktop/WebApplication/WebApp/static/profiles'+username+'.png', myfile)
      
      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO register(username,password,contact,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'User registered successfully'}
       return render(request, 'Register.html', context)
      else:
       context= {'data':'Error in Signup process'}
       return render(request, 'Register.html', context)

def EditMyProfile(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      contact = request.POST.get('contact', False)
      email = request.POST.get('email', False)
      address = request.POST.get('address', False)
      
      myfile = request.FILES['image']
      if os.path.exists('C:/Users/AISHWARYA THAKUR/Desktop/WebApplication/WebApp/static/profiles'+username+'.png'):
          os.remove('C:/Users/AISHWARYA THAKUR/Desktop/WebApplication/WebApp/static/profiles'+username+'.png')

      fs = FileSystemStorage()
      filename = fs.save('C:/Users/AISHWARYA THAKUR/Desktop/WebApplication/WebApp/static/profiles'+username+'.png', myfile)
      
      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "update register set username='"+username+"',password='"+password+"',contact='"+contact+"',email='"+email+"',address='"+address+"' where username='"+username+"'"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record updated")
      status_data = ''
      if db_cursor.rowcount == 1:
          con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
          with con:
              cur = con.cursor()
              cur.execute("select * FROM register")
              rows = cur.fetchall()
              for row in rows:
                  if row[0] == username and row[1] == password:
                      status_data = row[5]
                      break
          if status_data == 'none':
              status_data = ''            
          output = ''
          output+='<table border=0 align=center width=100%><tr><td><img src=/static/profiles/'+username+'.png width=200 height=200></img></td>'
          output+='<td><font size=3 color=black>'+status_data+'</font></td><td><font size=6 color=black>Welcome : '+username+'</font></td></tr></table></br></br>'
          output+=getPostData()
          context= {'data':output}
          return render(request, 'UserScreen.html', context)
      else:
       context= {'data':'Error in editing profile'}
       return render(request, 'EditProfile.html', context)    
        
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        status = 'none'
        status_data = ''
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '1234', database = 'user',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    status = 'success'
                    status_data = row[5]
                    break
        if status_data == 'none':
            status_data = ''
        if status == 'success':
            file = open('session.txt','w')
            file.write(username)
            file.close()
            output = ''
            output+='<table border=0 align=center width=100%><tr><td><img src=/static/profiles/'+username+'.png width=200 height=200></img></td>'
            output+='<td><font size=3 color=black>'+status_data+'</font></td><td><font size=6 color=black>Welcome : '+username+'</font></td></tr></table></br></br>'
            output+=getPostData()
            context= {'data':output}
            return render(request, 'UserScreen.html', context)
        if status == 'none':
            context= {'data':'Invalid login details'}
            return render(request, 'Login.html', context)