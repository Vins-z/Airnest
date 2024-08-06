a="""1,VI101,Vistara,Delhi,Mumbai,8:00,10:00
2,6E202,IndiGo,Delhi,Mumbai,10:30,12:30
3,SG702,SpiceJet,Delhi,Bangalore,9:00,11:00
4,VI502,Vistara,Mumbai,Delhi,8:30,10:30
5,6E303,IndiGo,Mumbai,Delhi,11:00,13:00
6,SG803,SpiceJet,Mumbai,Bangalore,12:00,14:00
7,VI903,Vistara,Bangalore,Delhi,9:30,11:30
8,6E404,IndiGo,Bangalore,Delhi,11:30,13:30
9,SG905,SpiceJet,Bangalore,Mumbai,10:00,12:00
10,6E505,IndiGo,Delhi,Bangalore,14:00,16:00
11,SG106,SpiceJet,Delhi,Mumbai,15:30,17:30
12,VI307,Vistara,Delhi,Bangalore,16:30,18:30
13,6E708,IndiGo,Mumbai,Delhi,17:00,19:00
14,SG209,SpiceJet,Mumbai,Bangalore,18:00,20:00
15,VI810,Vistara,Mumbai,Bangalore,19:30,21:30
16,6E611,IndiGo,Bangalore,Delhi,20:30,22:30
17,SG512,SpiceJet,Bangalore,Mumbai,21:00,23:00
18,VI413,Vistara,Bangalore,Delhi,22:00,0:00
19,6E114,IndiGo,Delhi,Mumbai,7:30,9:30
20,SG215,SpiceJet,Delhi,Bangalore,8:30,10:30
21,VI316,Vistara,Delhi,Mumbai,9:00,11:00
22,6E417,IndiGo,Mumbai,Delhi,10:30,12:30
23,SG518,SpiceJet,Mumbai,Bangalore,11:30,13:30
24,VI619,Vistara,Mumbai,Bangalore,12:00,14:00
25,6E720,IndiGo,Bangalore,Delhi,13:30,15:30
26,SG821,SpiceJet,Bangalore,Mumbai,14:30,16:30
27,VI922,Vistara,Bangalore,Delhi,15:00,17:00
28,6E823,IndiGo,Delhi,Mumbai,16:30,18:30
29,SG124,SpiceJet,Delhi,Bangalore,17:30,19:30
30,VI325,Vistara,Delhi,Mumbai,18:00,20:00
31,6E526,IndiGo,Mumbai,Delhi,19:30,21:30
32,SG627,SpiceJet,Mumbai,Bangalore,20:30,22:30
33,VI728,Vistara,Mumbai,Bangalore,21:00,23:00
34,6E829,IndiGo,Bangalore,Delhi,22:30,0:30
35,SG930,SpiceJet,Bangalore,Mumbai,23:30,1:30
36,VI131,Vistara,Bangalore,Delhi,7:00,9:00
37,6E232,IndiGo,Delhi,Mumbai,8:30,10:30
38,SG333,SpiceJet,Delhi,Bangalore,9:30,11:30
39,VI434,Vistara,Delhi,Mumbai,10:00,12:00
40,6E535,IndiGo,Mumbai,Delhi,11:30,13:30
41,SG636,SpiceJet,Mumbai,Bangalore,12:30,14:30
42,VI737,Vistara,Mumbai,Bangalore,13:00,15:00"""
b=a.split('\n')
c=[]

for i in b:
    c.append((i.split(','),'202306'))

for i in c:
    print(i)
    
        