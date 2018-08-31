#popis osoba za veceru
names = ['zelje','kolence','vulkan',]
print(names)
message = " i invite you to dinner."
print("\nHello " + names[0].title() + message)
print("\nHello " + names[1].title() + message)
print("\nHello " + names[2].title() + message)
 
#Vulkan nazalost ne moze doci na veceru, moramo naci zamjenu
print("\nVulkan ne moze doci na veceru i moramo naci zamjenu.")
names = ['zelje','kolence','vulkan',]
names[2] = 'bajo'
print(names)
print("\nHello " + names[0].title() + message)
print("\nHello " + names[1].title() + message)
print("\nHello " + names[2].title() + message)

#pronasli smo veci stol i zelimo pozvati jos gostiju
print("\nNasli smo veci stol i zelimo pozvati jos gostiju.")
names.insert(0, 'mrci')
names.insert(3, 'keko')
names.insert(6, 'dugi')
print(names)

#stol nece stici na vrijeme pa nam ostaje stol za dvije osobe
print("\nStol nece stici na vrijeme i ostaje nam stol za dvoje.")
gost1 = names.pop(0)
gost2 = names.pop(0)
gost3 = names.pop(0)
gost4 = names.pop(0)
message = " the table is full."
print("\nSory " + gost1.title() + message)
print("\nSory " + gost2.title() + message)
print("\nSory " + gost3.title() + message)
print("\nSory " + gost4.title() + message)
print(names)
message = " i invite you to dinner."
print("\nHello " + names[0].title() + message)
print("\nHello " + names[1].title() + message)
del names[0]
del names[0]
print(names)
