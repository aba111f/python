import json
file = open('Lab_4/myjson/task.txt')

j_son = file.read()

j_son = json.loads(j_son)




print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
print(j_son['imdata'][0]['l1PhysIf']['attributes']['dn'], '                            ',j_son['imdata'][0]['l1PhysIf']['attributes']['speed'],' ', j_son['imdata'][0]['l1PhysIf']['attributes']['mtu'])                                                                      
print(j_son['imdata'][1]['l1PhysIf']['attributes']['dn'], '                            ',j_son['imdata'][1]['l1PhysIf']['attributes']['speed'],' ', j_son['imdata'][1]['l1PhysIf']['attributes']['mtu'])                                                                      
print(j_son['imdata'][2]['l1PhysIf']['attributes']['dn'], '                            ',j_son['imdata'][2]['l1PhysIf']['attributes']['speed'],' ', j_son['imdata'][2]['l1PhysIf']['attributes']['mtu'])                                                                      
