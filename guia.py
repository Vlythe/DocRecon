
# Importar las bibliotecas necesarias
import pytesseract
from PIL import Image, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'D:\Documentos\Programas\tesseract\tesseract.exe'


def obtener_guia():


        # Cargar la imagen y recortar la sección deseada
    imagen = Image.open('D:\\Documentos\\Google Drive\\B_UAQ Software\\6to Semestre\\Hackathon\\Code Hackathon\\ejemplo guía_page-0001.jpg')
    # coordenadas de la sección a recortar
    seccion = imagen.crop((400, 500, 1200, 644))
    # 200,250,600,322
    # Convertir la sección a escala de grises y aplicar un filtro para mejorar la legibilidad del texto
    seccion_gris = seccion.convert('L')
    seccion_filtrada = seccion_gris.filter(ImageFilter.SHARPEN)

    # Aplicar OCR a la sección y obtener el texto
    texto = pytesseract.image_to_string(seccion_filtrada, lang='eng')

    # Imprimir el texto extraído
    
    return texto
