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

    # Muestra la imagen capturada
    cv2.imshow('camara web', imagen)

    # Presiona 's' para guardar la imagen
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Guarda la imagen capturada
        cv2.imwrite('captura.png', imagen)
        print("Imagen guardada como captura.png")

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
muestra.release()
cv2.destroyAllWindows()

print("Cámara web cerrada.")
