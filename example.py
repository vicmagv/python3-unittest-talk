#HMIS demo unitest

# Ejercicio 5
# Escriba el código de un sencillo método o función que tome cómo parámetros
# de entrada dos cadenas de caracteres, P1, P2, y devuelva otra cadena que
# contenga los caracteres de P1 que no están en P2.

#Returns the characters of 'string1' not included in 'string2'
def characters_not_included(p1, p2):
    return "".join(set(p1).difference(set(p2)))

if __name__ == '__main__':

    string1 = input("Introduce first string: ")
    string2 = input("Introduce second string: ")
    print ("Result:", characters_not_included(string1, string2))
