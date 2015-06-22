#s = raw_input("Enter text: ")

s_len = len(s)

#print s_len

i=0
count=0

#print s[1]

while i<s_len and i+1<s_len and i+2<s_len:
    if(s[i]=='b'):
        if(s[i+1]=='o'):
            if(s[i+2]=='b'):
                count+=1
    i+=1

print count
