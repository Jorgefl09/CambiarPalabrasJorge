# cambiar palabra original por nueva en un archivo de texto

""""
1. leer el archivo
2. cambiar la palabra
3. guardar el archivo
"""

palabra_original = "tizas"
palabra_nueva = "yesos"

fichero = open("fichero.txt", "r")
texto = fichero.read()
fichero.close()

texto_final = texto.replace(palabra_original, palabra_nueva)

fichero = open("fichero.txt", "w")
fichero.write(texto_final)
fichero.close()