import cv2

# Ruta de la imagen en tu dispositivo
ruta_imagen = r"C:\Users\usuario\Pictures\image.png"

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verifica si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta de la imagen.")
    exit()

# Obtén las dimensiones de la imagen
height, width = imagen.shape[:2]

# Dibuja un rectángulo verde
inicio_rect = (width - 100, 0)  # Esquina superior derecha
fin_rect = (width, 100)  # Final del rectángulo
color_rect = (0, 255, 0)  # Verde en formato BGR
grosor_rect = 3

cv2.rectangle(imagen, inicio_rect, fin_rect, color_rect, grosor_rect)

# Muestra la imagen con el rectángulo
cv2.imshow('Imagen con Rectángulo Verde', imagen)

# Espera hasta que se presione una tecla
cv2.waitKey(0)

cv2.destroyAllWindows()