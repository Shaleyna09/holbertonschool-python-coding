#!/usr/bin/python3
my_square = Square(3)
print(type(my_square))            ➜ <class '0-square.Square'>
print(my_square.__dict__)         ➜ {'_Square__size': 3}
print(my_square.size)             ➜ 🔴 Erreur : attribut public introuvable
print(my_square.__size)           ➜ 🔴 Erreur : name mangling empêche l'accès
