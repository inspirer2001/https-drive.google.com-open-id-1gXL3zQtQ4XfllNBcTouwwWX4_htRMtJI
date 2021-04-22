from django.shortcuts import render
from .des import *
from django.http import HttpResponse
def Home(request):
	return render(request,'project1/Home.html',{})

def xyz(request):
    return render(request,'project1/output.html',{})
def net1(request): 
    kk1=""
    itemValue1=""
    kk="";
    itemValue=""
    if request.method=='POST' and 'btnform1' in request.POST:
     yourForm= request.POST.dict()
     itemValue = yourForm.get("input1")
     for i in range(0,len(itemValue)):
        if(ord(itemValue[i])!=32):
         if(itemValue[i]>='A'and itemValue[i]<='Z'):
          kk=kk+(chr)(ord('Z')-ord(itemValue[i])+ord('A'))
         else:
          kk=kk+(chr)(ord('z')-ord(itemValue[i])+ord('a'))
        else:
         kk=kk+itemValue[i]
     # return render(request,'project1/net1.html',{'value1' : itemValue, 'value2': kk,'value3':" ",'value4':" "})
    elif request.method=='POST' and 'btnform2' in request.POST:
     yourForm= request.POST.dict()
     itemValue1 = yourForm.get("input2")
     for i in range(0,len(itemValue1)):
        if(ord(itemValue1[i])!=32):
         if(itemValue1[i]>='A'and itemValue1[i]<='Z'):
          kk1=kk1+(chr)(ord('Z')-ord(itemValue1[i])+ord('A'))
         else:
          kk1=kk1+(chr)(ord('z')-ord(itemValue1[i])+ord('a'))
        else:
         kk1=kk1+itemValue1[i]
    return render(request, 'project1/net1.html', {'value1':itemValue,'value2':kk,'value3': itemValue1 ,'value4':kk1}) 
def sdes(request):
    if request.method=='POST' and 'net3' in request.POST:
     yourForm= request.POST.dict()
     number_rounds = yourForm.get("nr")
     halfwidth=yourForm.get("hw")
     plain_text=yourForm.get("pt")
     key=yourForm.get("key")
     halfwidth=int(halfwidth)
     number_rounds=int(number_rounds)
     key1=key;
     k=number_rounds
     d=halfwidth
     s=plain_text
     key=str(key)
     plain_text=str(plain_text)
     key=text_hex(key)
     key=hex_bin(key)
     plain_text=text_hex(plain_text)
     plain_text=hex_bin(plain_text)
     key=key_preprocessor(key,halfwidth)
     key,_=round_keys_generator(key,number_rounds,halfwidth)
     plain_text=plaintext_preprocessor(plain_text,halfwidth)
     l,m=des_encryption(plain_text,key,number_rounds,halfwidth)
     m=merge_round_ciphertext(m)
     p=hex_bin(l)
     y=bin_text(p)
     return render(request,'project1/net5.html',{"val":l,"val1":k,"val2":d,"val3":s,"val4":key1,"val5":p,"val6":m,"val20":y})
    else:
     return render(request,'project1/net5.html',{})

def wkey(request):
    if request.method=='POST' and 'nt' in request.POST:
     yourForm= request.POST.dict()
     key=yourForm.get("key")
     number_rounds=yourForm.get("nr")
     key1=key
     number_rounds=int(number_rounds)
     key=str(key)
     # key=text_hex(key)
     key=hex_bin(key)
     key=key_preprocessor(key,32)
     key,hkey=round_keys_generator(key,number_rounds,32)
     return render(request,'project1/wkey.html',{"val25":key1,"val26":hkey,"val27":number_rounds})
    else:
     return render(request,'project1/wkey.html',{})

def avl(request):
    if request.method=='POST' and 'ne' in request.POST:
     yourForm= request.POST.dict()
     number_rounds = yourForm.get("nr")
     halfwidth=yourForm.get("hw")
     plain_text=yourForm.get("pt")
     key=yourForm.get("key")
     halfwidth=int(halfwidth)
     number_rounds=int(number_rounds)
     cplain_text=yourForm.get("cp")
     ckey=yourForm.get("ck")
     key1=key;
     ckey1=ckey
     cs=cplain_text
     k=number_rounds
     d=halfwidth
     s=plain_text
     key=str(key)
     plain_text=str(plain_text)
     key=text_hex(key)
     key=hex_bin(key)
     plain_text=text_hex(plain_text)
     plain_text=hex_bin(plain_text)
     ckey=str(ckey)
     cplain_text=str(cplain_text)
     ckey=text_hex(ckey)
     ckey=hex_bin(ckey)
     cplain_text=text_hex(cplain_text)
     cplain_text=hex_bin(cplain_text)
     key=key_preprocessor(key,halfwidth)
     key,_=round_keys_generator(key,number_rounds,halfwidth)
     ckey=key_preprocessor(ckey,halfwidth)
     ckey,_=round_keys_generator(ckey,number_rounds,halfwidth)
     plain_text=plaintext_preprocessor(plain_text,halfwidth)
     cplain_text=plaintext_preprocessor(cplain_text,halfwidth)
     l,m=des_encryption(plain_text,key,number_rounds,halfwidth)
     r,t=des_encryption(cplain_text,ckey,number_rounds,halfwidth)
     p=hex_bin(l)
     e=hex_bin(r)
     u=calculate_diff(m,t)
     m=merge_round_ciphertext(m)
     t=merge_round_ciphertext(t)
     return render(request,'project1/avl.html',{"val":l,"val1":k,"val2":d,"val3":s,"val4":key1,"val5":p,"val6":m,"val8":cs,"val9":ckey1,"val10":r,"val11":e,"val12":t,"val13":u})
    else:
     return render(request,'project1/avl.html',{})