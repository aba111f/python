import json
file = open('Lab_4/myjson/task.json')

j_son = file.read()

j_son = json.loads(j_son)




print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(0, len(j_son['imdata'])):
    print(j_son['imdata'][i]['l1PhysIf']['attributes']['dn'], '                            ',j_son['imdata'][i]['l1PhysIf']['attributes']['speed'],' ', j_son['imdata'][i]['l1PhysIf']['attributes']['mtu'])                                                                      
