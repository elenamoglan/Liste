with open ('input.txt','r') as f:
    a=list(eval(f.readline()))
with open ('output.txt', 'w') as f: 
    f.write('Lista 1 = ' + str(a) + '\n')
    f.write('Lista 2 = ' + str(sorted(a)) + '\n')
    f.write('Lista 3 = ' + str(sorted(a, reverse=True)) + '\n')
    f.write('Numarul de elemente din lista = ' + str(len(a)) + '\n' + 'Elementul MAX = ' + str(max(a)) + '\n' + 'Elementul MIN = ' + str(min(a)) + '\n')
    f.write('Lista 4 = ' + str(a + [111]) + '\n')
    a[1]=222
    f.write('Lista 5 = ' + str(a))
