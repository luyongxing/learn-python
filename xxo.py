file=open('xx.gv','w')
file.write('digraph, G { \n')
D=[
    [1 , 9 , 8], 
	[2 , 9 , 7],
	[3 , 8 , 7],
	[4 , 8 , 6],
	[5 , 7 , 6]
]
for d in D :
      file.write('%d->%d\n' % (d[1] , d[2] ) )
file.write('}')