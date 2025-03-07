s=input().split()
print(s)
#strStrip
print(s.strip())
#strMatch
s1=input()
s2=input()
if s1==s2:
    print('yes')
else:
    print('no')


#subString
s=input()
print(s[3:])
sub=s.find('puji')
print(s[sub:])

#upperToLower
s=input()
print(s.lower())

#waysOfCreate
s1='pujitha'
s2="pujitha"
s3='''pujitha
gayathri'''
s4=''.join('pujitha gayathri')
print(s1,s2,s3,s4)
s5=str('puji')
s6='pujitha'+'gayathri'
print(s5,s6)