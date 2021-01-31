with open ('doc.txt','r') as f:
    a=f.readline().split(',')
a.sort()
with open ('doc1.txt', 'w') as f: 
    f.write('Lista clasei a X-a "A"'+'\n')
    for i in a:
        f.write(str(i)+'\n')