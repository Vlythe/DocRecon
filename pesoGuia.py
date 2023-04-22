
# Importar las bibliotecas necesarias
import pytesseract
from PIL import Image, ImageFilter

def pesoGuia_pytess(rutaPytess):
    pytesseract.pytesseract.tesseract_cmd = rutaPytess

def obtener_valor(rutaImg):

    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion = imagen.crop((1790,1228,1866,1303)) # coordenadas de la sección a recortar
    
    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    # Imprimir el texto extraído

    cadena_con_coma = texto
    cadena_con_punto = cadena_con_coma.replace(",", ".")

    return cadena_con_punto

def obtener_guia(rutaImg):

        # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    # coordenadas de la sección a recortar
    seccion = imagen.crop((400, 500, 1200, 644))
    # 200,250,600,322
    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    texto = texto.replace("\n", "")
    
    return texto
