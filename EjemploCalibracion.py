from RobotObject import Robot
from SensorObject import Sensor
import time
import matplotlib.pyplot as plt
from FuncionesSensores import  *

mi_robot = Robot()
mi_robot.connect(puerto="COM5")

# Defino comandos con su identificador
comando = {
    "RX_MS_SENSOR_ULTRA_SONIDO_ONETIME" : "SENUS1",
    "RX_MS_SENSOR_OPTICO_ONETIME" : "SENOP1",
    "RX_MOV_SERVO" : "MOV1",
    "RX_RECORRIDO_SERVO" : "MOVR",
    "RX_MS_SENSOR_ULTRA_SONIDO" : "SENUS",
    "RX_MS_SENSOR_OPTICO" : "SENOP",
    "RX_MS_SENSOR_ACELEROMETRO" : "SENAC",
    "RX_MS_SENSOR_GIROSCOPO" : "SENGI",
    "RX_RECORRIDO_SERVO" : "MOVR",

}

# Asigno los comandos al objeto robot
mi_robot.set_commands(comandos=comando)

# Defino sensores y los asigno al objeto robot
ultra_sonido = Sensor()
optico = Sensor()


sensores = {
    "SENUSD" : ultra_sonido,
    "SENOPD" : optico,
}

mi_robot.set_sensors(sensores)

# Inicializo la adquisicion de datos de sensores a los objetos "Sensor"
mi_robot.start_sensor_log()

# Cambio la posicion del servo
mi_robot.send_command("RX_MOV_SERVO",[0]) 

num_mediciones = 30

for i in range(num_mediciones):

    time.sleep(0.2)
    # Pido medicion de sensor ultrasonido    
    mi_robot.send_command("RX_MS_SENSOR_ULTRA_SONIDO_ONETIME")

    time.sleep(0.2)
    # Pido medicion de sensor optico 
    mi_robot.send_command("RX_MS_SENSOR_OPTICO_ONETIME")

    print(f"medicion {i}")


# Creación de los gráficos
plt.figure(figsize=(10, 5))

# Gráfico para sensor ultrasonido
plt.subplot(1, 2, 1)
plt.plot(range(num_mediciones),ultra_sonido.get_values(), marker='o', color='b')
plt.title('Medición Sensor Ultrasonido')
plt.xlabel('Medicion N°')
plt.ylabel('Distancia (mm)')
plt.grid(True)

# Gráfico para sensor óptico
plt.subplot(1, 2, 2)
plt.plot(range(num_mediciones),optico.get_values(), marker='s', color='r')  
plt.title('Medición Sensor Óptico')
plt.xlabel('Medicion N°')
plt.ylabel('Distancia (mm)')
plt.grid(True)

# Ajustar el diseño
plt.tight_layout()

# Mostrar los gráficos
plt.show()

## ahora con los sensores calibrados

calibracion_sensores([ultra_sonido,optico])

ultra_sonido.queue_clear()
optico.queue_clear()

for i in range(num_mediciones):

    time.sleep(0.2)
    # Pido medicion de sensor ultrasonido    
    mi_robot.send_command("RX_MS_SENSOR_ULTRA_SONIDO_ONETIME")

    time.sleep(0.2)
    # Pido medicion de sensor optico 
    mi_robot.send_command("RX_MS_SENSOR_OPTICO_ONETIME")

    print(f"medicion {i}")


# Creación de los gráficos
plt.figure(figsize=(10, 5))

# Gráfico para sensor ultrasonido
plt.subplot(1, 2, 1)
plt.plot(range(num_mediciones),ultra_sonido.get_values(), marker='o', color='b')
plt.title('Medición Sensor Ultrasonido')
plt.xlabel('Medicion N°')
plt.ylabel('Distancia (mm)')
plt.grid(True)

# Gráfico para sensor óptico
plt.subplot(1, 2, 2)
plt.plot(range(len(optico.get_values())),optico.get_values(), marker='s', color='r')  
plt.title('Medición Sensor Óptico')
plt.xlabel('Medicion N°')
plt.ylabel('Distancia (mm)')
plt.grid(True)

# Ajustar el diseño
plt.tight_layout()

# Mostrar los gráficos
plt.show()

mi_robot.disconnect()
