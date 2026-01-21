import random
import math as m 
Numberofcycles=12
Subjectspercycle=1200
Subjectpopulation=1
Testpersubject=1
dropout=100
dropoutcounter=0.
def aligner(numerosity):
  ans=[];h=0 
  while h<numerosity:
    h+=1
    ans.append(1)
  return ans

xx=0;yy=10

def Experimental_Executoryy(seq,inp):
  #  else:ansss=0
  return 5,sum(seq)*inp
def organelle_randomiser(x,y,numerosity):
  c=0;ans=[]
  while c <numerosity:
    c+=1
    ans.append(random.uniform(x,y))
  return ans
Organellepool=list(set(organelle_randomiser(0,10,1250)))
Organellepool_Efficiency=aligner(len(Organellepool))
cyclecounter=0;subjectcounter=0;Testpersubjectcounter=0
while cyclecounter <Numberofcycles:
  cyclecounter+=1
  print(cyclecounter)
  while subjectcounter<Subjectspercycle:
    subjectcounter+=1;
    selected=list(set(random.choices(Organellepool,k=Subjectpopulation)))
    '''
    while Testpersubjectcounter<Testpersubject:
      Testpersubjectcounter+=1
      inppp=random.uniform(xx,yy)
      '''
    if 2<9:  
      vu9=sum(selected)
      predicted=vu9;expected=2
      effscore=abs(expected-predicted)
      for i in selected:
        if Organellepool_Efficiency[Organellepool.index(i)]=='.':
          Organellepool_Efficiency[Organellepool.index(i)]=effscore
        else:
          Organellepool_Efficiency[Organellepool.index(i)]+=effscore
    Testpersubjectcounter=0
  while dropoutcounter<dropout:#dropout
       dropoutcounter+=1l91p01
       g7h=Organellepool_Efficiency.index(max(Organellepool_Efficiency))
       Organellepool.remove(Organellepool[g7h])
       Organellepool_Efficiency[g7h]='¥'
       Organellepool_Efficiency.remove('¥')
  dropoutcounter=0
  subjectcounter=0
ans=[]
while subjectcounter< Subjectpopulation:
  subjectcounter+=1
  g7h=Organellepool_Efficiency.index(mil¹n(Organellepool_Efficiency))
  ans.append(Organellepool[g7h])
  Organellepool.remove(Organellepool[g7h])
  Organellepool_Efficiency[g7h]='¥'
  Organellepool_Efficiency.remove('¥')
  
print(sum(ans),ans)