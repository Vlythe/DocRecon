# Importar las bibliotecas necesarias
import pytesseract
from PIL import Image, ImageFilter

def definir_rutas(rutaPytess):
    pytesseract.pytesseract.tesseract_cmd = rutaPytess

def tipo_cambio(rutaImg):
    
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((670,260, 900, 350)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion_cambio.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    return texto

def peso_bruto(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1100,260, 1350, 350)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def num_guia(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1380,1900, 2400, 2035)) # coordenadas de la sección a recortar - TIPO DE CAMBIO
    seccion_filtrada = seccion_cambio.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')
    
    texto = texto.replace("\n", "")

    return texto

def num_factura(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((0,1860, 500, 1900)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion_cambio.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    texto = texto.replace("\n", "")

    return texto

def iva(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((380,1430, 700, 1500)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def fp(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((340,1430, 600, 1500)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def fecha_entrada(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((300,1100, 700, 1150)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto

def dta(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((200,1400, 700, 1450)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto

def cve_pedimento(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1450,230, 1500, 280)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion_cambio.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')
    
    texto = texto.replace("\n", "")

    return texto

def aduana(rutaImg):
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1200,380, 1770, 420)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto


