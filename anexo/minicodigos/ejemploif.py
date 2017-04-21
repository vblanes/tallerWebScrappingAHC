dicc_edades = {'Vicent' : 24, 'Maria' : 20, 'Damian' : 47}
# queremos saber si Vicent esta en nuestro diccionario
# y si lo esta mostrar su edad
if 'Vicent' in dicc_edades.keys():
    print(dicc_edades['Vicent'])

# es posible anyadir un bloque de codigo que se ejecute
# si la condicion no se cumple

if 'Laura' not in dicc_edades.keys():
    print(dicc_edades['Laura'])
else:
    dicc_edades['Laura'] = 27
# si Laura esta en el diccionario mostramos su edad
# si no esta la anyadimos
# En este ejemplo el programa ignoraria el bloque de codigo
# interior al if y ejecutaria el del else
