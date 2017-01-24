from django.shortcuts import render
from django.shortcuts import  HttpResponse
from cmdb import models
# Create your views here.
'''
user_list=[
  {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"}]
'''
def index(request):
    #request.post
    #request.get
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
     #   print(username,password)
      #  temp = {"user":username,"pwd":password}
       # user_list.append(temp)
        models.UserInfo.objects.create(user  =username,pwd = password)  #保存到数据库中
        user_list = models.UserInfo.objects.all()   # 读所有行
    return render(request,"index.html",{"data":user_list})
