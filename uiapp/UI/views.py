from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
import jwt
import requests
# Create your views here.
SECRET="rakesh"
from django.http import HttpResponseRedirect

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    #print(dir(jwt))
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3000),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET

        )
    except Exception as e:
        return e



def login(request):
    return render(request,"index.html")


def home(request):
    print(request.POST)

    payload={"name":request.POST.get("user"),'email': request.POST.get('email'),"password":request.POST.get('password')}
    print(payload)
    response=requests.get("http://52.151.218.85/auth/login",data=payload)
    print(response.text)
    res=response.json()
    if res["status"]=="success":
       request.session["token"]=res["auth_token"]
       resp=render(request,"home.html")
       resp.set_cookie("token",res["auth_token"])
       print(request.session['token'])
       return resp
    else:
       return render(request,"index.html")