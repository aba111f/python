import os 

mylist = str(["1,2,3,4,5","fsefs",'vsvsdvs'])

filename = input()
if os.path.exists(filename):
    with open(filename,'w') as file:
        file.write(mylist)
        file.close()
else:
    print('file not found')