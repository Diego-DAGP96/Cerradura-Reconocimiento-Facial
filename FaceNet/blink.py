import pyfirmata

puerto = "\\.\COM9"  # Puerto COM de emulación en USB
LedRed = (13)  # PIN donde va conectado el LED
LedGreen = (12)  # PIN donde va conectado el LED

# Conexión con placa Arduino
print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(puerto)
print("Conectado a Arduino por USB...")
while True:
    print("Encendiendo LED Rojo...")
    tarjeta.digital[LedRed].write(1)
    print("Encendido LED Rojo...")
    tarjeta.pass_time(10)
    print("Apagando LED Rojo...")
    tarjeta.digital[LedRed].write(0)
    print("Apagado LED Rojo...")
    tarjeta.pass_time(3)

    print("Encendiendo LED Verde...")
    tarjeta.digital[LedGreen].write(1)
    print("Encendido LED Verde...")
    tarjeta.pass_time(10)
    print("Apagando LED Verde...")
    tarjeta.digital[LedGreen].write(0)
    print("Apagado LED Verde...")
    tarjeta.pass_time(3)
tarjeta.exit()