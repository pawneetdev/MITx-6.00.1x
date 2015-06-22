#s = raw_input("Enter text: ")

s_len = len(s)

#print s_len

i=0
count=0

#print s[1]

while i<s_len:
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        count+=1
    i+=1

print count
