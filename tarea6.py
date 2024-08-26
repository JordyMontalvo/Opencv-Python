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

# Añadir texto a la imagen
texto = "Hola, OpenCV!"
posicion = (50, height // 2)
fuente = cv2.FONT_HERSHEY_SIMPLEX
escala_fuente = 1
color_texto = (255, 255, 256)  # Blanco en formato BGR
grosor_texto = 2

cv2.putText(imagen, texto, posicion, fuente, escala_fuente, color_texto, grosor_texto)

# Muestra la imagen con el texto
cv2.imshow('Imagen con Texto', imagen)

# Espera hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
