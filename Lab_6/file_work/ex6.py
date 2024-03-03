import os 

direct = input()

let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

if os.path.exists(direct):
    for i in let:
        filename = os.path.join(direct,f"{i}.txt")
        with open(filename,'w') as file:
            pass
        file.close()
else:
    print('directory not found')