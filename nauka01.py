# coding=utf8
# UWAGA! sololearn nie rozpoznaje polskich znaków w czytanych liniach kodu 
# i będzie przy kompliacji zawsze wysypywać błędy

print('Hello world!')

# dzielenie bez reszty
print(9 // 4)

# modulo - reszta z dzielenia
print(9 % 4)

#nowy wiersz tekstu robimy po prostu enterem lub \n
print("""A
a
a""")

#input("Jak masz na imie?")

# w konstrukcji if statement musi być wcięty bo inaczej program wysypie błąd
if 5 > 3:
    print('\ncos tam')
    
# if + else - ważne wcięcia!
if 7 > 5:
    print('liczba wieksza od pieciu')
else:
    print('liczba mniejsza lub rowna piec')
    
# elif to skrócona opcja zapisu powyższego kodu, ułatwia pisanie kodu z wieloma if else
num = 7
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")
    
#prosta pętla

i = 1
while i <=5:
    print(i)
    i+=1
    
print('koniec')

#prosta pętla z zatrzymaniem break
i=0
while 1==1:
    print(i)
    i+=1
    if i>5:
        print('koniec')
        break

# pętla z opcją continue
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")

# lista jednowymiarowa z wypisywaniem treści - UWAGA! tak jak w Javie indeksowanie jest od 0
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# przykład tablicy składującej pozycje różnych rodzajów / wypisywanie zawartości tablicy
#(w tym tablicę tablicy - podany przykład odnoszenia się do niej)
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

# sprawdzanie czy w tablicy są określone wartości
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# dodawanie kolejnej wartości do tablicy (w następnym indeksie, powiększając jej rozmiar)
tablica = [1, 2, 3, 4]
tablica.append(5)
print(tablica)
# wywoływanie długości tablicy
print(len(tablica))
# dopisanie wartości w dowolnym miejscu (bez usuwania istniejącego rekordu)
tablica.insert(0, 8)
print(tablica)

#pętla
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1 
   
# ta sama pętla w uproszeniu (for loop)
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
  
# definiowanie funkcji
def moja_funkcja():
    print('To jest moja pierwsza funkcja')

moja_funkcja()

# return (zwracanie wartości)
def max(x, y):
    if x >=y:
        return x
    else:
        return y
print(max(4, 5))

"""
to są komentarze do dokumentacji
coś innego niż zwykły komentarz
"""

# funkcje mogą być argumentami innych funkcji 
# w poniższym przykładzie "funkcja" oznacza miejsce w polu argumentów gdzie należy wybrać funkcję (chyba z puli
# wcześniej zdefiniowanych) chyba tak można sobie zrobić kalkulator
def dodawanie(x, y):
    return x + y

def do_twice(funkcja, x, y):
    return funkcja(funkcja(x, y), funkcja(x, y))

a = 5
b = 10

print(do_twice(dodawanie, a, b))

