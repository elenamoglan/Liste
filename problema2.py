with open ('input.txt','r') as f:
    a=list(eval(f.readline()))
with open ('output.txt', 'w') as f: 
    f.write('lista 1 =' + str(a)+'\n')
    b=sorted(a)
    f.write('lista 2 =' + str(b)+'\n')
    c=sorted(a, reverse=True)
    f.write('lista 3 =' + str(c)+'\n')
    f.write('Numarul de elemente din lista =' + str(len(a))+'\n' + 'elementul MAX =' + str(max(a))+'\n' + 'elementul MIN =' + str(min(a))+'\n')
    f.write('lista 4 =' + str(a + [111])+'\n')
    a[1]=222
    f.write('lista 5 =' + str(a)+'\n')