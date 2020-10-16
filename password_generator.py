import random

Max_len=12

Digit=[1,2,3,4,5,6,7,8,9,0]
Upper=['Q','W','E','R','T','Y','U','I','O','P','A','S','F','G','H','J','K','L','Z','X','C','V','B','N','M','D']
Lower=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
spec=['!','@','#','$','%','^','&','*','+','-','/','|','?','.',',']

a=Digit+Upper+Lower+spec

rand_d=random.choice(Digit)
rand_u=random.choice(Upper)
rand_l=random.choice(Lower)
rand_s=random.choice(spec)
password=str(rand_d)+rand_l+rand_s+rand_u
for i in range(Max_len-1):
    temp=random.choice(a)
    password=password+str(temp)

print(password)