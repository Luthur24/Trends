import AppModulator as A
import random
import os
import datetime
#Handles all frontend request
def frontend_request_protocol(x):
  ans={}
  x=x.split(A.global_seperator);request_status=x[0]
  if request_status=="signup":
    username=x[1];email=x[2];password=x[3]
    acc_exist=Account_existence_verifier(email,request_status)
    if acc_exist==1:
      ans["Request_return_status"]="An account associated with this email already exists."
    else:#updating database for new account
      open("username_db",'a').write(username+'\n');open("email_db",'a').write(email+'\n');open("password_db",'a').write(password+'\n')
      ans["Request_return_status"]='Account  created successfully.'
      keyofuserbeingpersonalized=len(open('username_db','r').readlines())-1
      ans['Trendspage']=Trendspage_contentgenerator(keyofuserbeingpersonalized)
      ans['Explorepage']=Explore_contentgenerator()
      ans['Biopage']=Biopagecontentgenerator(keyofuserbeingpersonalized)
  elif request_status=="signin":
    email=x[1];password=x[2]
    acc_exist=Account_existence_verifier(email,request_status)
    if acc_exist==1:
      ans["Request_return_status"]='Signed in successfully.'
      keyofuserbeingpersonalized=open('email_db','r').index(email+'\n')
      ans['Trendspage']=Trendspage_contentgenerator(keyofuserbeingpersonalized)
      ans['Explorepage']=Explore_contentgenerator()
      ans['Biopage']=Biopagecontentgenerator(keyofuserbeingpersonalized)
    elif acc_exist==0:
      ans["Request_return_status"]='This account does not exist .'
    elif acc_exist==2:
      ans["Request_return_status"]='Incorrect Password.'
  elif request_status=='like':
    open('whatwaslikedandstatus_db','w').write(f'{x[2]}.{x[3]}.1\n')
    open('userwholikedandwhstwasliked_db','w').write(f'{x[1]}.{x[2]}.{x[3]}\n')
    
  elif request_status=='unliked':
    open('whatwaslikedandstatus_db','w').write(f'{x[2]}.{x[3]}.0\n')
    open('userwholikedandwhstwasliked_db','w').write(f'{x[1]}.{x[2]}.{x[3]}\n')
  return ans
        
def Account_existence_verifier(email,request_statusss,Password):
  ui=open("email_db",'r').readlines()
  hy=open("password_db",'r').readlines()
  if request_statusss=='signup':
     if email+'\n' in ui:
       ans=1
     else:ans=0
  else:
   xQ= email+'\n' in ui
   kQ= password+'\n' in hy
   if xQ:
     einx=ui.index(email+'\n')
     pinx=hy.index(password+'\n')
     if einx==pinx:
       ans=1#account exists
     else:
       ans=2#incorrect password
   else:
      ans=0#account does not exist
     
  return ans
  
def Trendspage_contentgenerator(keyofuserbeingpersonalized):
    ans=""
    rt=os.listdir('ContentUpload_db')
    ci=set(random.choices(list(range(0,len(rt))),k=A.personalizabletrendspagecontent_numerosity))
    yio='profileupload_db'
    Dyh=open('username_db','r').readlines()
    Drcj=open('email_db','r').readlines()
    qwyd89=open('selfcomment_db','r').readlines()
    tf6fs=open('indexofcontentanduserwhopostedselfcomment_db','r').readlines()
    for i in ci:
      iinfo=rt[i].split('_');iemail=iinfo[1]
      bhq=Drcj.index(iemail+'\n')
      kio9=tf6fs.index(f'{iinfo[0]}.{bhq}\n')
      ta6=qwyd89[kio9].removesuffix('\n')
      zu8b=otherpeoplecommentsys(bhq,iinfo[0])
      dateposted=dateparser(open('contentposteddate_db','r').readlines()[kio9])
      dt3v=Dyh[bhq].removesuffix('\n')
      dr="<div>"
      ys7=likes_countercolor(keyofuserbeingpersonalized,rt[i])
      tji=f"<span><img src='{yio}/{iemail}'><span>{dt3v}</span></span> <img src='ContentUpload_db/{rt[i]}'><aside><span style='color:{ys7[1]}' id='{iinfo[0]}-TrendspageContentLike-{bhq}' onclick='LikeFunction(\"{iinfo[0]}-TrendspageContentLike-{bhq}\")'>&hearts; <r id='{iinfo[0]}-TrendspageContentLikecount-{bhq}'>{ys7[0]}</r></span><span onclick='document.getElementById(\"{iinfo[0]}-TrendspageContentOthercommentsection-{bhq}\").style.display=\"block\";'>&aleph; <r>{zu8b[0]}</r></span></aside><ui>{ta6}</ui><dp>{dateposted}</dp>{zu8b[1]}"
      dr+=tji
      dr+="</div>"
    return ans
def likes_countercolor(keyofuserbeingpersonalized,contentfilename):
  tu7=contentfilename.split('_')
  t6k=open('whatwaslikedandstatus_db','r').readlines()
  r6g8=open('email_db','r').readlines().index(tu7[1]+'\n')
  likednumerosity=t6k.count(f'{tu7[0]}.{r6g8}.1\n')-t6k.count(f'{tu7[0]}.{r6g8}.0\n')
  yu6c=open('userwholikedandwhstwasliked_db','r').readlines();ds4=f'{keyofuserbeingpersonalized}.{tu7[0]}.{r6g8}\n';v6o=yu6c.count(ds4)
  if v6o==0:
    color='aliceblue'
  else:
    x=0
    while ds4 in yu6c:
      x+=1;p9e=yu6c.index(ds4)
      if x==v6o:
        f4=t6k[p9e]
      else:yu6c[p9e]='.'
    if '1\n' in f4:
      color='#ff0028eb'
    else:color='aliceblue'
      
  return likednumerosity,color
def dateparser(date_str):#input '2025-12-25'
    date_format='%Y-%m-%d'
    """
    Convert a date string to month and day.
    :param date_str: Date as a string (e.g., "2025-12-25")
    :param date_format: Format of the input string (default: '%Y-%m-%d')
    :return: Month and day (e.g., "December 25")
    """
    try:
        dt = datetime.strptime(date_str, date_format)
        return f'{dt.strftime('%B %d')}.'
    except ValueError:
        return f"Error: Could not parse date '{date_str}'. Ensure format matches '{date_format}'."
  
def otherpeoplecommentsys(keyofuserwhoposted,indexofcontentinuserposted):
  othercomm=f"<section id='{indexofcontentinuserposted}-TrendspageContentOthercommentsection-{keyofuserwhoposted}' style='display:none'><spc onclick='document.getElementById(\"{indexofcontentinuserposted}-TrendspageContentOthercommentsection-{keyofuserwhoposted}\").style.display=\"none\";'>&cent;</spc>"
  youme=f'{indexofcontentinuserposted}.{keyofuserwhoposted}\n'
  g7f=open('indexofcontentanduserwhopostedothercomments_db','r').readlines()
  f67=open('keyofuserwhocommentedotherpeoplecomment_db','r').readlines()
  h57g=open('otherpeoplecomments_db','r').readlines()
  t5r5=open('email_db','r').readlines()
  b67yg=open('username_db','r').readlines()
  z24g=g7f.count(youme)
  while youme in g7f:
    inxi=g7f.index(youme)
    d56=eval(f67[inxi].removesuffix('\n'))
    pp=t5r5[d56].removesuffix('\n')
    un5g=b67yg[d56].removesuffix('\n')
    cys77=h57g[inxi].removesuffix('\n')
    aeu98= f"<div><span><img src='profileupload_db/{pp}'><txt>{un5g}</txt></span><ut>{cys77}</ut></div>"
    othercomm+=aeu98
    g7f[inxi]='.'
  return z24g,othercomm+='</section>'

def Explore_contentgenerator():
  ans="<section><h>Now Trending</h>"
  Nowtrending=remove_all_occurrences(random.choices(open("Nowtrending_db","r").readlines(),k=A.maxtrending),'\n')
  Timelessbuzz=remove_all_occurrences(random.choices(open("Timelessbuzz_db","r").readlines(),k=A.maxtrending),'\n')
  return ans+f"<div>{Nowtrending}</div><br><br><br><br><br><h>'Timelessbuzz'<\h><div>{Timelessbuzz}</div>"
  
def remove_all_occurrences(data, x):
    """
    Removes all occurrences of 'x' from the string 'data'.
    
    Parameters:
        data (str): The original string
        x (str): The character or substring to remove (must be non-empty)
    
    Returns:
        str: New string with all occurrences of 'x' removed
    """
    if not x:  # Handle empty x (nothing to remove)
        return data
    
    return data.replace(x, '')
  
def Biopagecontentgenerator(keyofuserbeingpersonalized):
  ans=""
  g6t9=os.listdir('profileupload_db')
  t67ko=open('email_db','r').readlines()[keyofuserbeingpersonalized].removesuffix('\n')
  frrrs2=open('username_db','r').readlines()
  t45se=frrrs2[keyofuserbeingpersonalized].removesuffix('\n')
  f56yf3333=open('whatwaslikedandstatus_db','r').read()
  if t67ko in g6t9:
    ans+=f"<div><img src='profileupload_db/{t67ko}'></div>"
  ans+=f"<span>{t45se}</span> <ll>{f56yf3333.count(f'{keyofuserbeingpersonalized}.1\n')-f56yf3333.count(f'{keyofuserbeingpersonalized}.0\n')} likes</ll><aside>Posts</aside><mc>"
  g5e9x=open("indexofcontentanduserwhopostedselfcomment_db",'r').read()
  start=f".{keyofuserbeingpersonalized}\n"
  ty6g=g5e9x.count(start);gy=0
  f7do9n=open('email_db','r').readlines()
  io4=f7do9n[keyofuserbeingpersonalized].removesuffix('\n')
  if ty6g>0:
    while gy<ty6g:
      gy+=1 
      ans+=f"<ic><img src='ContentUpload_db/{gy-1}_{io4}'></ic>"
  ans+='</mc>'