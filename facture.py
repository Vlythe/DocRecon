
# Importar las bibliotecas necesarias
import pytesseract
from PIL import Image, ImageFilter



def numFactura(rutaImg, rutaPytess):
    pytesseract.pytesseract.tesseract_cmd = rutaPytess
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion = imagen.crop((1245,802,1922,1040)) # coordenadas de la sección a recortar
    #1245,802,1922,1040
    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    texto = texto.replace("\n", "")

    return texto

