guests = ['ivan','marko','petar',]
message = "pozivamo vas na veceru gopson "
print(message + guests[0].title() + ".")
print(message + guests[1].title() + ".")
print(message + guests[2].title() + ".")
umro_je = ('marko')
guests.remove(umro_je)
print(guests)
print("\n Gospodin " + umro_je.title() + " je umro i nece moci doci.")

