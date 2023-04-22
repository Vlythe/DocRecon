# Reglas para los campos a evaluar:

from datetime import datetime, timedelta
import pesoGuia
import pedimentoFunciones
# Variables del pedimento leídos, modificar los valores por los nuevos de json

p_valorAduana = int(pedimentoFunciones.aduana())
p_tipoCambio = float(pedimentoFunciones.tipo_cambio())
p_pesoBruto = float(pedimentoFunciones.peso_bruto())
p_cvePedimento = str(pedimentoFunciones.cve_pedimento())
p_dta = int(pedimentoFunciones.dta())
p_iva = int(pedimentoFunciones.iva())
p_fpIva = int(pedimentoFunciones.fp())
p_numGuia = str(pedimentoFunciones.num_guia())
p_stringFechaEnt = str(pedimentoFunciones.fecha_entrada())
p_numFactura = str(pedimentoFunciones.num_factura())

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

f_numFactura = 'SAC2105'

# Variables recuperadas de la guía

g_numGuia = str(pesoGuia.obtener_guia())
g_pesoBruto = float(pesoGuia.obtener_valor())

# Variable booleana para verificar que no haya ningún error

todoOk = True

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
    todoOk = False

# Revisión de IVA calculado

if c_iva != p_iva:
    print('Discrepancia: revisar IVA')
    todoOk = False

# Revisión de la forma de pago del IVA

if c_fpIva != p_fpIva:
    print('Revisar F.P. del IVA')
    todoOk = False

# Revisión del tipo de cambio utilizado

if p_fechaEnt in t_tipoCambio:
    if p_tipoCambio != t_tipoCambio[p_fechaEnt]:
              print('Revisar tipo de cambio.')
              todoOk = False

elif p_fechaEnt is not t_tipoCambio:
    print(p_fechaEnt)

    while p_fechaEnt is not t_tipoCambio:
        p_fechaEnt -= timedelta(days=1)

        if p_fechaEnt in t_tipoCambio:
         if p_tipoCambio != t_tipoCambio[p_fechaEnt]:
              print('Revisar tipo de cambio.')
              todoOk = False
       
         break

# Revisión de datos de factura

if (f_numFactura != p_numFactura):
    print('Discrepancia: revisar número de factura.')
    todoOk = False

# Revisión de datos de guía

if (g_numGuia != p_numGuia):
    print('Discrepancia: revisar la guía House')
    todoOk = False

if (g_pesoBruto!=p_pesoBruto):
    print('Discrepancia: revisar peso bruto.')
    todoOk = False

if todoOk:
    print('No hay errores encontrados.')



    