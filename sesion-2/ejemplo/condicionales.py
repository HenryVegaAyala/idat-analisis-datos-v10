# if: "¿Se cumple esto?"
# elif: "Si no cumple lo anterior, ¿se cumple esto otro?"
# else: "Si no se cumple ninguna de las condiciones anteriores, haz esto."

nota = 15

if nota >= 18:
    print("Nota excelente")
elif nota >= 14:
    print("Nota buena")
elif nota >= 12:
    print("Nota suficiente")
else:
    print("Nota insuficiente")

if nota >= 18:
    print("Nota excelente")
else:
    print("Nota insuficiente")