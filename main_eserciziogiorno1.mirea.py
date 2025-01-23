print("Inizio programma")

# Assegno la variabile foo
foo = False

# Questi controlli assert devono passare tutti
assert bool(1)
assert False == False
assert True is True
assert True != False

# Faccio alcune operazioni aritmetiche sui numeri interi
bar = 0
baz = 1
if bar != 0 :
    result = baz / bar
    print(result)
else :
    print("Errore: bar non può essere zero!")
    result = 0


# Incremento il risultato di uno

result += 1
print ("Il risultato è: ", result)
# Decremento il risultato di uno

result -= 1
print ("Il risultato è: ", result)

# Controllo che il valore non sia negativo
assert result <= 0

# Creo una lista e la estendo
li1 = [1, 2]
li1 += [3]
print(li1)
# Non mi ricordo come si "prepende" un valore...
li1.insert(0,0)
print(li1)

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo
tu1 = (1, 2)
tu1 += (3, )
print(tu1)
assert tu1 == (1, 2, 3)

# Creo un dict

d1 = {}
d2 = {}
d2["a"] = 1
d1["b"] = 2


assert d1["b"] != 1

d1 = {"a":1, "b":2}
assert d1 == {"a": 1, "b": 2}

# Cancello la chiave "b"
del d1["b"]


# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1 :
    assert True
else:
    assert False

if "a" in d1:
    assert True
else:
    assert False

# Stampo la scritta "Ciao" tre volte poi esco
# Conto le volte che l'ho stampata
count = 0
for idx in [1, 2, 3]:
    count += 1
    print("Ciao")


# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num > 0:
    print("Ciao")
    num -= 1

print("Fine programma")

# Bonus: verifico la seguente operazione sui float

print(0.1 + 0.2)
assert 0.1 + 0.2 == 0.30000000000000004
