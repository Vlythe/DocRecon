# Importar las bibliotecas necesarias
import pytesseract
from PIL import Image, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'D:\Documentos\Programas\tesseract\tesseract.exe'
rutaImg = 'D:\\Documentos\\Google Drive\\B_UAQ Software\\6to Semestre\\Hackathon\\Code Hackathon\\ejemplo pedimento censurado_page-0001.jpg'

def tipo_cambio():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(
        rutaImg)
    seccion_cambio = imagen.crop((670,260, 900, 350)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion_cambio.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    return texto

def peso_bruto():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1100,260, 1350, 350)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def num_guia():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1380,1900, 2400, 2035)) # coordenadas de la sección a recortar - TIPO DE CAMBIO
    seccion_filtrada = seccion_cambio.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')
    
    texto = texto.replace("\n", "")

    return texto

def num_factura():
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

def iva():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((380,1430, 700, 1500)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def fp():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((340,1430, 600, 1500)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    return texto

def fecha_entrada():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((300,1100, 700, 1150)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto

def dta():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((200,1400, 700, 1450)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto

def cve_pedimento():
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

def aduana():
    # Cargar la imagen y recortar la sección deseada
    imagen = Image.open(rutaImg)
    seccion_cambio = imagen.crop((1200,380, 1770, 420)) # coordenadas de la sección a recortar - TIPO DE CAMBIO

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_cambio, lang='eng')

    texto = texto.replace("\n", "")

    return texto


