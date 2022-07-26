from django.http import HttpResponse
from django.shortcuts import render

def talk(request):
    return render(request,'index.html')

def pic(request):
    return HttpResponse(
        '''
        <h1>This is the About GFG</h1>
        <a href="https://practice.geeksforgeeks.org/explore?page=2&category[]=Arrays&sortBy=submissions"> Geeks </a>
        '''
    )

def aboutus(request):
    return render(request,'About_us.html')


def Modified(request):
    dj = request.GET.get('name')
    rp = request.GET.get('rempunc','off')
    rn = request.GET.get('remnum','off')
    rc = request.GET.get('makecap','off')
    rl = request.GET.get('makelow','off')
    res = request.GET.get('remexsp','off')
    rel = request.GET.get('remexli','off')
    punc = '''!()-[];:'"\,<>./?@#$%^&*_'''
    nums = "0123456789"
    alpha ="abcdefghijklmnopqrstuvwxyz"
    ans = dj
    if(rp == 'on'):
        dj = ans 
        ans = ""
        for i in dj:
            if i in punc:
                ans += " "
            else:
                ans += i
    if(rn == 'on'):
        dj = ans 
        ans = ""
        for i in dj:
            if i not in nums:
                ans += i
    if(rc == 'on'):
        dj = ans 
        ans = ""
        for i in dj:
            if i.lower() in alpha:
                ans += i.upper()
            else:
                ans += i
    if(rl == 'on'):
        dj = ans
        ans = ""
        for i in dj:
            if i.lower() in alpha:
                ans += i.lower()
            else:
                ans += i
    if(res == 'on'):
        dj = ans
        ans = ""
        for i in dj:
            if(ans != "" and ans[-1]==" " and i == " "):
                pass
            else:
                ans+= i
    if(rel == 'on'):
        dj = ans
        ans = "" 
        for i in dj:
            if i!="\n" and i!="\r":
                ans += i
    dic = {'name':ans}
    return render(request,'index2.html',dic)

def help(request):
    return render(request,'Help.html')
