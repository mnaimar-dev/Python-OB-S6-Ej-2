# Crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print('Nombre:', self.nombre, 'Nota:', self.nota)
        
    def resultado(self):
        if self.nota >= 6:
            print('El alumno ha aprobado.' )
        else:
            print('El alumno ha desaprobado.' )
    
nicolas = Alumno()
nicolas.inicializar('Nicolas', 8)
nicolas.imprimir()
nicolas.resultado()