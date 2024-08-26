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

# Dibuja un círculo rojo en el centro
centro = (width // 2, height // 2)  # Centro de la imagen
radio = 50
color_circulo = (0, 0, 255)  # Rojo en formato BGR
grosor_circulo = 2

cv2.circle(imagen, centro, radio, color_circulo, grosor_circulo)

# Muestra la imagen con el círculo
cv2.imshow('Imagen con Círculo Rojo', imagen)

# Espera hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
