import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Algoritmo CRC")
window.geometry("530x300")
window['bg'] = '#083E8E'

lblMensaje = tk.Label(window, text="Mensaje D", bg='#083E8E', fg="white")
lblMensaje.place(x=50, y=20)
entryMensaje = tk.Entry(window, width=25)
entryMensaje.place(x=50, y=40)
entryMensaje.focus()

lblGenerador = tk.Label(window, text="Generador G", bg='#083E8E', fg="white")
lblGenerador.place(x=50, y=80)
entryGenerador = tk.Entry(window, width=25)
entryGenerador.place(x=50, y=100)

lblCRC = tk.Label(window, text="CRC", bg='#083E8E', fg="white")
lblCRC.place(x=300, y=20)
edtbTextCRC = tk.StringVar() # El texto editable
txtCRC = tk.Entry(window, width=25, state="readonly", textvariable=edtbTextCRC)
txtCRC.place(x=300, y=40)

lblTramaX = tk.Label(window, text="Trama TX", bg='#083E8E', fg="white")
lblTramaX.place(x=300, y=80)
edtbTextTramaX = tk.StringVar() # El texto editable
txtTextTramaX = tk.Entry(window, width=25, textvariable=edtbTextTramaX)
txtTextTramaX.place(x=300, y=100)

def switchButtonState():
    btnEnviarMensaje['state'] = tk.NORMAL

def validar(valor1: str, valor2: str):
    valido = False

    if (valor1 and valor2):
        if convertToList(valor1) != 0 and convertToList(valor2) != 0:
            valido = True
        else:
            messagebox.showerror("Syntax Error", "No se aceptan valores no binarios (0,1)")
    else:
        messagebox.showerror("Syntax Error", "Message/Generator can not be empty")
    
    return valido

def windowCalcularCRC():
    mensajeStr = entryMensaje.get()
    generadorStr = entryGenerador.get()

    valido = validar(mensajeStr, generadorStr)
    if valido:
        infoEmisor = emisor(mensajeStr, generadorStr)

        CRC = infoEmisor["CRC"]
        tramaX = infoEmisor["Trama X"]
        edtbTextCRC.set(CRC)
        edtbTextTramaX.set(tramaX)

        switchButtonState()

def windowEnviarMensaje():
    mensajeX = txtTextTramaX.get()
    generadorStr = entryGenerador.get()

    valido = validar(mensajeX, generadorStr)
    if valido:

        infoReceptor = receptor(mensajeX, generadorStr)

        if (infoReceptor["Info"] == False):
            messagebox.showerror("Receptor", "El mensaje no se envió correctamente \n" + "Sended Message: "+ mensajeX )
        else:
            messagebox.showinfo("Receptor", "El mensaje fue enviado correctamente \nSended Message: " + infoReceptor["Sended Message"])

def emisor(mensajeStr: str, generadorStr: str):

    # Convertimos los mensajes de string a listas de integers
    mensajeD = convertToList(mensajeStr)
    generadorG = convertToList(generadorStr)

    crc = calcularCRC(mensajeD, generadorG)
    tramaX = mensajeD.copy()    # La trama X a enviar al receptor 
    for x in crc:
        tramaX.append(x)

    salida = {}
    salida.update( {"CRC" : crc} )
    salida.update( {"Trama X" : tramaX} )

    for clave, valor in salida.items():
        salida[clave] = convertToStr(valor)
    
    return salida

def receptor(tramaXStr:str, generadorStr: str):
    # Convertimos los mensajes de string a listas de integers
    tramaX = convertToList(tramaXStr)
    generadorG = convertToList(generadorStr)

    result = verificarReceptor(tramaX, generadorG)
    return result


# Convierte el string del input en una lista de integers
def convertToList(text: str)->list:
    binarioList = list(text)

    for i in range(len(binarioList)):
        try:
            binarioList[i] = int(binarioList[i])
        except:
            return 0    # El método explota si intenta convertir letras en int
    
    binario = True
    for x in binarioList:
        if (x != 0 and x != 1): # Verifica si el número es binario
            binario = False
            break

    if binario: return binarioList
    else: return 0

def convertToStr(binario: list)->str:
    
    for i in range(len(binario)):
        binario[i] = str(binario[i])
    
    binarioStr = "".join(binario)
    return binarioStr

# Depura los binarios (quita los ceros a la izquierda)
def depurarBinario(binario: list):
    depurated = False
    
    while (depurated == False):
       if len(binario) == 0: depurated = True
       elif binario[0] == 1: depurated = True
       else: binario.pop(0)

    return binario

# Realiza la división binaria
def divisionBinaria(dividendo:list, divisor:list):
    cociente = []
    residuo = []
    dividendoActual = []
    ended = False

    while (ended == False):

        dividendoActual = residuo.copy()
        dividendoActual = depurarBinario(dividendoActual)

        while (len(dividendoActual) < len(divisor)):
            if (len(dividendo)>0):
                dividendoActual.append(dividendo[0])
                dividendo.pop(0)
                if (len(dividendoActual) < len(divisor)):
                    cociente.append(0)
            else:
                break

        if len(dividendoActual) >= len(divisor):
            cociente.append(1)
            residuo = []
            for i in range(len(dividendoActual)):
                if (dividendoActual[i] != divisor[i]):
                    residuo.insert(i, 1)
                else:
                    residuo.insert(i, 0)      
        else:
            ended = True
    
    salida = {}
    cociente = depurarBinario(cociente)
    salida.update({"Residuo" : residuo})
    salida.update({"Cociente": cociente})

    return salida

# función para calcular el CRC
def calcularCRC (mensajeD: list, generadorG: list)-> list:

    r = len(generadorG)-1 # calcula el r
    tramaDividendo = mensajeD.copy() # el dividendo a agregarle los bits de r

    for _ in range(r):
        tramaDividendo.append(0)

    result = divisionBinaria(tramaDividendo, generadorG)
    crc = result.get("Residuo")
    crc.pop(0)
    # print(result)
    return crc

def verificarReceptor(tramaX: list, generadorG: list):
    
    tramaY = tramaX.copy()
    result = divisionBinaria(tramaY, generadorG)
    verResiduo = result["Residuo"]
    verResiduo = depurarBinario(verResiduo)
    salida = {}

    if (len(verResiduo)>0):
        salida.update({ "Info" : False })

    else:
        salida.update({ "Info" : True })
    
    salida.update({ "Sended Message" : convertToStr(tramaX) })
    salida.update({ "Residuo" : convertToStr(verResiduo) })

    return salida

btnCalcularCRC = tk.Button(window, text="Calcular CRC", command=windowCalcularCRC)
btnCalcularCRC.place(x=50, y=140)

btnEnviarMensaje = tk.Button(window, text="Enviar mensaje", state="disabled", command=windowEnviarMensaje)
btnEnviarMensaje.place(x=300, y=140)

window.mainloop()