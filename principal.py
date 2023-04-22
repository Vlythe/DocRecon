from datetime import datetime, timedelta
import pesoGuia
import pedimentoFunciones
import facture

rutaPytess = rutaPytess = r'D:\Documentos\Programas\tesseract\tesseract.exe'

def revisarDocs(rutaImgFact, rutaImgPed, rutaImgGuia):

    # Variables del pedimento leídos

    pedimentoFunciones.definir_rutas(rutaPytess)
    p_valorAduana = int(pedimentoFunciones.aduana(rutaImgPed))
    p_tipoCambio = float(pedimentoFunciones.tipo_cambio(rutaImgPed))
    p_pesoBruto = float(pedimentoFunciones.peso_bruto(rutaImgPed))
    p_cvePedimento = str(pedimentoFunciones.cve_pedimento(rutaImgPed))
    p_dta = int(pedimentoFunciones.dta(rutaImgPed))
    p_iva = int(pedimentoFunciones.iva(rutaImgPed))
    p_fpIva = int(pedimentoFunciones.fp(rutaImgPed))
    p_numGuia = str(pedimentoFunciones.num_guia(rutaImgPed))
    p_stringFechaEnt = str(pedimentoFunciones.fecha_entrada(rutaImgPed))
    p_numFactura = str(pedimentoFunciones.num_factura(rutaImgPed))

    # Variables que se van a calcular y comparar contra los leídos.

    p_fechaEnt = datetime.strptime(p_stringFechaEnt, "%d/%m/%Y")
    c_iva = 0

    # Variables de tasas

    t_tipoCambio = {
        datetime.strptime("13/09/2019", "%d/%m/%Y"):19.56612, 
        datetime.strptime("17/09/2019", "%d/%m/%Y"):19.22310, 
        datetime.strptime("18/09/2019", "%d/%m/%Y"):19.36650}

    t_fraccionDTA = { 'I':0.008, 'II':0.00176, 'III': 331}
    t_iva = 0.16

    # Variables recuperadas de la factura

    f_numFactura = str(facture.numFactura(rutaImgFact, rutaPytess))

    # Variables recuperadas de la guía

    g_numGuia = str(pesoGuia.obtener_guia(rutaImgGuia))
    g_pesoBruto = float(pesoGuia.obtener_valor(rutaImgGuia))

    # Diccionario de campos a evaluar

    resultados = {

        "TIPO CAMBIO": True,
        "PESO BRUTO": True,
        "DTA": True,
        "IVA": True,
        "F.P. IVA": True,
        "NUM GUIA": True,
        "NUM FACTURA": True

    }

    # Cálculos de DTA, IVA y FP de acuerdo a CVE PEDIMENTO

    if (p_cvePedimento == 'AF'):

        if (p_valorAduana*t_fraccionDTA['II'])<t_fraccionDTA['III']:
            c_dta=t_fraccionDTA['III']
        else:
            c_dta=round((p_valorAduana*t_fraccionDTA['II']), 0)
        
        c_fpIva = 21

    elif (p_cvePedimento == 'A1'):

        if ((p_valorAduana*t_fraccionDTA['I'])<t_fraccionDTA['III']):
            c_dta=t_fraccionDTA['III']
        else:
            c_dta=round((p_valorAduana*t_fraccionDTA['I']),0)

        c_fpIva = 0

    c_iva = round(((c_dta+p_valorAduana)*t_iva),0)

    # Revisión de DTA

    if c_dta != p_dta:
        print('Discrepancia: revisar DTA')
        resultados["DTA"] = False

    # Revisión de IVA calculado

    if c_iva != p_iva:
        print('Discrepancia: revisar IVA')
        resultados["IVA"] = False

    # Revisión de la forma de pago del IVA

    if c_fpIva != p_fpIva:
        print('Revisar F.P. del IVA')
        resultados["F.P. IVA"] = False

    # Revisión del tipo de cambio utilizado

    if p_fechaEnt in t_tipoCambio:
        if p_tipoCambio != t_tipoCambio[p_fechaEnt]:
                print('Revisar tipo de cambio.')
                resultados["TIPO CAMBIO"] = False

    elif p_fechaEnt is not t_tipoCambio:
        print(p_fechaEnt)

        while p_fechaEnt is not t_tipoCambio:
            p_fechaEnt -= timedelta(days=1)

            if p_fechaEnt in t_tipoCambio:
                if p_tipoCambio != t_tipoCambio[p_fechaEnt]:
                    resultados["TIPO CAMBIO"] = False
        
            break

    # Revisión de datos de factura

    if (f_numFactura != p_numFactura):
        print('Discrepancia: revisar número de factura.')
        resultados['NUM FACTURA']=False

    # Revisión de datos de guía

    if (g_numGuia != p_numGuia):
        print('Discrepancia: revisar guia House.')
        resultados['NUM GUIA']=False

    if (g_pesoBruto!=p_pesoBruto):
        print('Discrepancia: revisar peso bruto.')
        resultados['PESO BRUTO']=False


    return resultados




    