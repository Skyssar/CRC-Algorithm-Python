# ALGORITMO PARA EL CALCULO DEL CRC by Skyssar (YasarJosé)

mensajeStr = input("Introduzca el mensaje D ")
generadorStr = input("Introduzca el generador G ")

def emisor(mensajeStr: str, generadorStr: str):

    # Convertimos los mensajes de string a listas de integers
    mensajeD = convertToList(mensajeStr)
    generadorG = convertToList(generadorStr)

    if (mensajeD != 0 and generadorG != 0):
        crc = calcularCRC(mensajeD, generadorG)
        tramaX = mensajeD.copy()    # La trama X a enviar al receptor 
        for x in crc:
            tramaX.append(x)

        salida = {}
        salida.update( {"Mensaje D" : mensajeD} )
        salida.update( {"Generador G" : generadorG} )
        salida.update( {"CRC" : crc} )
        salida.update( {"Trama X" : tramaX} )

        for clave, valor in salida.items():
            salida[clave] = convertToStr(valor)
        
        return salida

    else:
        return 0

def receptor(tramaXStr:str, generadorStr: str):
    # Convertimos los mensajes de string a listas de integers
    tramaX = convertToList(tramaXStr)
    generadorG = convertToList(generadorStr)

    if (tramaX != 0 and generadorG != 0):
        result = verificarReceptor(tramaX, generadorG)
        return result
    else:
        return 0 

def sendMessage():
    if mensajeStr and generadorStr:
        infoEmisor = emisor(mensajeStr, generadorStr)
        if infoEmisor == 0:
            print("No se aceptan valores no binarios (0, 1)")
        else:
            print(infoEmisor)
            mensajeEmisor = infoEmisor["Trama X"]
            # mensajeEmisorStr = convertToStr(mensajeEmisorList)

            infoReceptor = receptor(mensajeEmisor, generadorStr)
            print(infoReceptor)
    else:
        print("the message can not be empty")

# Convierte el string del input en una lista de integers
def convertToList(text: str)->list:
    binarioList = list(text)

    for i in range(len(binarioList)):
        try:
            binarioList[i] = int(binarioList[i])
        except:
            return 0    # El método explota si intenta convertir letras en int
    
    for x in binarioList:
        if (x != 0 and x != 1): # Verifica si el número es binario
            return 0
        else:
            return binarioList

# Convierte la lista binaria nuevamente a string
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
                    residuo.append(0)
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
    while (len(crc)>r):
        crc.pop(0)
    print(result)
    return crc

def verificarReceptor(tramaX: list, generadorG: list):
    
    tramaY = tramaX.copy()
    result = divisionBinaria(tramaY, generadorG)
    verResiduo = result["Residuo"]
    verResiduo = depurarBinario(verResiduo)
    salida = {}

    if (len(verResiduo)>0):
        salida.update({ "Info" : "El mensaje no fue enviado correctamente" })

    else:
        salida.update({ "Info" : "Mensaje enviado correctamente" })
    
    salida.update({ "Sended Message" : tramaX })
    salida.update({ "Residuo" : verResiduo })

    return salida

sendMessage()    

