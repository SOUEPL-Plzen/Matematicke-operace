x = input("Zadejte proměnou x: ") # Čeká na uživatele, než zadá číslo. 
                                  # Číslo se náslodně uloží do proměnné x.
y = input("Zadejte proměnou y: ")

# Přetupujeme str na int
x = int(x)
y = int(y)

# Výpis do terminálu - Kontrolujeme co je v x a y.
print(f"Proměnná x = {x} a proměnná y = {y}")

print("------------------------")
print(f"Příklad {x} + {y}:")
print(f"Sčítání výsledek {x+y}")
print("------------------------")
print(f"Příklad {x} - {y}:")
print(f"Odčítání výsledek {x-y}")
print("------------------------")
print(f"Příklad {x} * {y}:")
print(f"Násobení výsledek {x*y}")
print("------------------------")
print(f"Příklad {x} / {y}:")
print(f"Dělení výsledek {x/y}")
print("------------------------")
print(f"Příklad {x} ^ {y}:") # ^ píšeme levý alt + numerická klávesnice 94
print(f"Mocnění výsledek {x**y}") # Mocníme pomocí **
print("------------------------")
print(f"Odmocnina {x} √ {y}:") # Znak odmocnina najdeme na intenetu - zkopírujeme a vložíme
print(f"Odmocněný výsledek {x**(1/y)}") # Základní matematická operace, nejdříve vydělíme a pak mocníme

