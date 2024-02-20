import datetime

word = str(input())

if word == "today":
    x = datetime.datetime.now()
elif word == "yesterday":
    x = datetime.datetime.now() - datetime.timedelta(days = 1)
else:
    x = datetime.datetime.now() + datetime.timedelta(days = 1)

   

print(x)
