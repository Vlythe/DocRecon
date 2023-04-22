import principal

rutaImgFact = 'D:\\Documentos\\Google Drive\\B_UAQ Software\\6to Semestre\\Hackathon\\Code Hackathon\\ejemplo factura - rotated_page-0001.jpg'
rutaImgPed = 'D:\\Documentos\\Google Drive\\B_UAQ Software\\6to Semestre\\Hackathon\\Code Hackathon\\ejemplo pedimento censurado_page-0001.jpg'
rutaImgGuia = 'D:\\Documentos\\Google Drive\\B_UAQ Software\\6to Semestre\\Hackathon\\Code Hackathon\\ejemplo guía_page-0001.jpg'
rutaPytess = r'D:\Documentos\Programas\tesseract\tesseract.exe'

resultados = principal.revisarDocs(rutaImgFact,rutaImgPed, rutaImgGuia, rutaPytess)

for campos, valor in resultados.items():
    if not valor:
        print(campos, ':', valor)
