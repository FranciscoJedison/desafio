def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))
