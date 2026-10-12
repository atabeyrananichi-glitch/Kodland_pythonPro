meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" :"ponerse agresivo/enojado"
            }


print("¡Hola! Bienvenida a la aplicación de diccionario de memes.")
print("Instrucciones:")
print("- Escribe palabras en MAYÚSCULAS.")
print("- El programa te explicará su significado.")
print("- Podrás consultar 5 palabras en esta ejecución.\n")

for i in range(5):
    print( str(i+1) + "/5) Escribe una palabra que no entiendas: ")
    word = input()
    if word.upper() in meme_dict.keys():
        print(word.upper() +":"+ meme_dict[word.upper()]+"\n")
    else:
       print("La palabra "+ word +" no está en el diccionario")
        #print("Puedes añadirla más adelante si quieres.\n")
 
        
print("¡Gracias por usar el diccionario de memes! 😄")
