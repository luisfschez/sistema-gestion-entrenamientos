# ==========================================
# ACTIVIDAD FORMATIVA 2
# DESARROLLO DE UNA APLICACIÓN SIMPLE
# SISTEMA DE GESTIÓN DE ENTRENAMIENTOS
# Lenguaje de programación: Python
# ==========================================


# ==========================================
# CLASE EJERCICIO
# ==========================================

class Ejercicio:
    """
    Representa un ejercicio de entrenamiento.
    Almacena su nombre y el peso utilizado.
    """

    # Constructor: inicializa un ejercicio con su nombre y peso.
    def __init__(self, nombre, peso):
        self.nombre = nombre  # Nombre del ejercicio.
        self.peso = peso      # Peso utilizado en kilogramos.

    # Método que aumenta en 1 kg el peso del ejercicio.
    def aumentar_peso(self):
        self.peso += 1

    # Método que muestra el nombre y el peso del ejercicio.
    def mostrar(self):
        print(f"Ejercicio: {self.nombre} | Peso: {self.peso} kg")


# ==========================================
# CLASE RUTINA
# ==========================================

class Rutina:
    """
    Representa una rutina de entrenamiento.
    Contiene un nombre y una lista de ejercicios.
    """

    # Constructor: inicializa la rutina y crea una lista vacía.
    def __init__(self, nombre):
        self.nombre = nombre       # Nombre de la rutina.
        self.ejercicios = []       # Lista que almacenará los ejercicios.

    # Método que agrega un objeto Ejercicio a la lista de la rutina.
    def agregar_ejercicio(self, ejercicio):
        self.ejercicios.append(ejercicio)

    # Método que muestra el nombre de la rutina y sus ejercicios.
    def mostrar_rutina(self):
        print(f"\n===== RUTINA DE {self.nombre.upper()} =====")

        # Recorre la lista y muestra cada ejercicio registrado.
        for ejercicio in self.ejercicios:
            ejercicio.mostrar()

    # Método que aumenta 1 kg al peso de todos los ejercicios.
    def aumentar_peso(self):
        # Recorre los ejercicios y utiliza su método aumentar_peso().
        for ejercicio in self.ejercicios:
            ejercicio.aumentar_peso()

        # Informa al usuario que se realizó el aumento.
        print(
            f"\nSe aumentó 1 kg a todos los ejercicios "
            f"de {self.nombre}."
        )


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    """
    Función principal de la aplicación.
    Crea las rutinas, registra los ejercicios
    y permite al usuario interactuar con el menú.
    """

    # ==========================================
    # CREACIÓN DE OBJETOS DE TIPO RUTINA
    # ==========================================

    # Se crean tres objetos de la clase Rutina.
    pierna = Rutina("Pierna")
    brazo = Rutina("Brazo")
    pecho = Rutina("Pecho")


    # ==========================================
    # RUTINA DE PIERNA
    # ==========================================

    # Se crean cuatro objetos Ejercicio y se agregan a la rutina.
    pierna.agregar_ejercicio(Ejercicio("Sentadilla", 40))
    pierna.agregar_ejercicio(Ejercicio("Prensa", 80))
    pierna.agregar_ejercicio(Ejercicio("Extension de cuadriceps", 30))
    pierna.agregar_ejercicio(Ejercicio("Curl femoral", 25))


    # ==========================================
    # RUTINA DE BRAZO
    # ==========================================

    # Se registran los cuatro ejercicios de brazo.
    brazo.agregar_ejercicio(Ejercicio("Curl con barra", 20))
    brazo.agregar_ejercicio(Ejercicio("Curl martillo", 12))
    brazo.agregar_ejercicio(Ejercicio("Curl predicador", 15))
    brazo.agregar_ejercicio(Ejercicio("Extension de triceps", 20))


    # ==========================================
    # RUTINA DE PECHO
    # ==========================================

    # Se registran los cuatro ejercicios de pecho.
    pecho.agregar_ejercicio(Ejercicio("Press inclinado", 30))
    pecho.agregar_ejercicio(Ejercicio("Press plano", 35))
    pecho.agregar_ejercicio(Ejercicio("Press en maquina", 40))
    pecho.agregar_ejercicio(Ejercicio("Aperturas", 15))


    # ==========================================
    # MENÚ PRINCIPAL
    # ==========================================

    # El ciclo mantiene el menú activo hasta que el usuario salga.
    while True:

        # ------------------------------------------
        # RUTINA SEMANAL
        # ------------------------------------------

        # Muestra la distribución semanal de entrenamiento y descanso.
        print("\n========================================")
        print("           RUTINA SEMANAL")
        print("========================================")
        print("Lunes      → Brazo")
        print("Martes     → Pecho")
        print("Miércoles  → Pierna")
        print("Jueves     → Descanso")
        print("Viernes    → Brazo")
        print("Sábado     → Pierna")
        print("Domingo    → Descanso")


        # ------------------------------------------
        # OPCIONES DEL SISTEMA
        # ------------------------------------------

        # Presenta las acciones disponibles para el usuario.
        print("\n========================================")
        print("       SISTEMA DE ENTRENAMIENTO")
        print("========================================")
        print("1. Ver rutina de Pierna")
        print("2. Ver rutina de Brazo")
        print("3. Ver rutina de Pecho")
        print("4. Aumentar peso en Pierna (+1 kg)")
        print("5. Aumentar peso en Brazo (+1 kg)")
        print("6. Aumentar peso en Pecho (+1 kg)")
        print("7. Salir")

        # Lee la opción elegida desde el teclado.
        opcion = input("\nSelecciona una opcion: ")


        # ==========================================
        # SELECCIÓN DE OPCIONES Y USO DE MÉTODOS
        # ==========================================

        # Muestra la rutina de pierna.
        if opcion == "1":
            pierna.mostrar_rutina()

        # Muestra la rutina de brazo.
        elif opcion == "2":
            brazo.mostrar_rutina()

        # Muestra la rutina de pecho.
        elif opcion == "3":
            pecho.mostrar_rutina()

        # Aumenta 1 kg a los ejercicios de pierna y muestra los resultados.
        elif opcion == "4":
            pierna.aumentar_peso()
            pierna.mostrar_rutina()

        # Aumenta 1 kg a los ejercicios de brazo y muestra los resultados.
        elif opcion == "5":
            brazo.aumentar_peso()
            brazo.mostrar_rutina()

        # Aumenta 1 kg a los ejercicios de pecho y muestra los resultados.
        elif opcion == "6":
            pecho.aumentar_peso()
            pecho.mostrar_rutina()

        # Finaliza el ciclo y termina el programa.
        elif opcion == "7":
            print("\nPrograma finalizado.")
            break

        # Informa cuando se introduce una opción no disponible.
        else:
            print("\nOpcion no valida.")


# ==========================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================

# Comprueba que el archivo se ejecute directamente.
# Si es así, llama a la función principal main().
if __name__ == "__main__":
    main()