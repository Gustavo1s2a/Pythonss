import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Crear una imagen en blanco con fondo blanco
width, height = 356, 356
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Definir colores
blue = (26, 83, 255)
red = (237, 28, 36)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Usar la fuente predeterminada de Pillow
font_large = ImageFont.load_default()
font_medium = ImageFont.load_default()
font_small = ImageFont.load_default()

# Dibujar fondo azul
draw.rectangle([0, 0, width, height//2], fill=blue)

# Dibujar banner rojo
draw.rectangle([0, height//2, width, height], fill=red)

# Añadir texto
draw.text((10, 10), "AGENCIA DE EMPLEOS", fill=white, font=font_large)
draw.text((10, 50), "SERVICIO EXCLUSIVO", fill=white, font=font_medium)
draw.text((10, 100), "CONTAMOS CON", fill=white, font=font_medium)
draw.text((10, 130), "LAS MEJORES", fill=white, font=font_medium)
draw.text((10, 160), "EMPLEADAS", fill=yellow, font=font_large)
draw.text((10, 190), "DEL HOGAR", fill=yellow, font=font_large)
draw.text((200, 250), "UBICANOS:", fill=white, font=font_medium)
draw.text((10, 300), "Av. Nicolas Ayllon N 5695 3er piso OFICINA 304 ATE-Vitarte", fill=black, font=font_small)

# Añadir caja de contacto
draw.rectangle([250, 0, width, 60], fill=red)
draw.text((255, 10), "CONTACTANOS:", fill=white, font=font_medium)
draw.text((255, 30), "918-162-502", fill=white, font=font_large)

# Guardar la imagen
image_path = "employment_agency.png"
image.save(image_path)
image.show()
