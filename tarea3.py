import cv2

# Ruta de la imagen en tu dispositivo
ruta_imagen = r"public/descarga.jpg"

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verifica si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta de la imagen.")
    exit()

# Obtén las dimensiones de la imagen
height, width = imagen.shape[:2]

# Dibuja una línea recta azul en el centro de la imagen
# Coordenadas de inicio (x = 0, y = height // 2) y de fin (x = width, y = height // 2)
color_linea = (0, 255, 0)  # Azul en formato BGR
grosor_linea = 2

cv2.line(imagen, (0, height // 2), (width, height // 2), color_linea, grosor_linea)

# Muestra la imagen con la línea recta
cv2.imshow('Imagen con Línea Recta Azul', imagen)

# Espera hasta que se presione una tecla
cv2.waitKey(0)

# Cierra todas las ventanas abiertas
cv2.destroyAllWindows()
