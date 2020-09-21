m=open("resourceTable.txt","r")
line = m.readlines()

def find(z,y) :
    for x in range(300):
        k=line[x].split()
        if(float(k[0])==z):
            return float(k[y+1])



p = [50,49.5,49.4,49.3,49.2,49.1,49]
j = [1,1,1,1,1,1,1]
r = []
for i in range(7):
    s = find(p[i],j[i])
    r.append(s)

print(r)