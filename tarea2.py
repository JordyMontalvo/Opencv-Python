import cv2
import os  

# Limpia la pantalla
os.system("cls")

# Inicializa la cámara; prueba con el índice 0 primero
muestra = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not muestra.isOpened():
    print("Error: No se pudo abrir la cámara. Verifica el índice de la cámara o la conexión.")
    exit()

# Bucle principal para capturar y mostrar imágenes
while True:
    # Captura un frame de la cámara
    estado, imagen = muestra.read()

    # Verifica si la captura fue exitosa
    if not estado:
        print("Error: No se pudo capturar la imagen.")
        break

    # Obtén las dimensiones de la imagen para calcular la diagonal
    height, width = imagen.shape[:2]

    # Dibuja una línea diagonal desde la esquina superior izquierda a la esquina inferior derecha
    cv2.line(imagen, (0, 0), (width, height), (0, 255, 0), 2)

    # Muestra la imagen capturada con la línea diagonal
    cv2.imshow('camara web', imagen)

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
muestra.release()
cv2.destroyAllWindows()

print("camara web")
