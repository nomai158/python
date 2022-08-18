file=open('noman.txt','w')

file.write("this is written by noman")

file.close()

file=open('noman.txt','r')

content=file.read()

file.close()

print( 'contnt in the file is  = ' , content)