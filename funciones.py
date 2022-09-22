x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z[0]['y'] = 30
print(z)

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
'''
arreglo = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

diccionario = {'first_name':  'Michael', 'last_name' : 'Jordan'}
llave = 'first_name'
print('first_name', 'Michael')
llave = 'last_name'
print('last_name', 'Jordan')

diccionario = {'first_name' : 'John', 'last_name' : 'Rosales'}
llave = 'first_name'
print('first_name', 'John')   
llave = 'last_name' 
print('last_name', 'Rosales')

diccionario = {'first_name' : 'Mark', 'last_name' : 'Guillen'}
llave = 'first_name'
print('first_name', 'Mark')
llave = 'last_name'
print('last_name', 'Guillen')

diccionario = {'first_name' : 'KB', 'last_name' : 'Tonel'}
llave = 'first_name'
print('first_name', 'KB')
llave = 'last_name'
print('last_name', 'Tonel')
'''
def iterateDictionary(arreglo):
    for diccionario in arreglo:
        for llave in diccionario:
            print(llave, diccionario[llave])

iterateDictionary(estudiantes) 