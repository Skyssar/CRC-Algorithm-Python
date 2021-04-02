# CRC-Algorithm-Python
## Algoritmo que permite simular el cálculo del CRC (Chequeo de Redundancia Cíclica) en redes locales.
El presente código corresponde a una simulación del cálculo del Chequeo de Redundancia Cíclica, un código de detección de errores usado frecuentemente en redes digitales y en dispositivos de almacenamiento para detectar cambios accidentales en los datos. Fue realizado en el lenguaje Python y su biblioteca gráfica para interfaces de usuario, Tkinter.

El código CRC opera de la siguiente forma: 

Considere la secuencia de datos de d bits, D, que el nodo emisor quiere transmitir al nodo receptor. El emisor y el receptor tienen que acordar primero un patrón de r+1 bits, conocido como generador, que denominaremos con la letra G. Impondremos la condición de que el bit más significativo (el bit situado más a la izquierda) de G sea 1.  Para una determinada secuencia de datos D, el emisor seleccionará r bits adicionales, R, y se los añadirá a D, de modo que el patrón de d+r bits resultante (interpretado como un número binario) sea exactamente divisible por G (es decir, no tenga ningún resto). 

El proceso de comprobación de errores con los códigos CRC es, por tanto, muy simple: el receptor divide los d+r bits recibidos entre G. Si el resto es distinto de cero, el receptor sabrá que se ha producido algún error; en caso contrario, se aceptarán los datos como correctos. 
Fuente :Kurose, J., & Ross, K. W. (2010). Redes de computadoras (Vol. 5). 

Así, el presente algoritmo permite realizar una simulación del funcionamiento del código CRC, en el cual el usuario podrá ingresar los valores binarios correspondientes al Mensaje D y el Generador G, devolviéndole el programa los patrones de bits correspondientes al CRC y a la trama G+r que se enviará al receptor. El usuario podrá también modificar dicha trama emulando errores en el mensaje transmitido que el programa se encargará de identificar.

El código está dividido en un archivo denominado crcAlgorithm.py que posee el funcionamiento lógico del algoritmo, y un archivo llamado crcInterfaz, que posee la versión de usuario del código, dotado de una interfaz gráfica en la que se puede interactuar.

==========================================================================

## Algorithm that allows to simulate the CRC (Cyclic Redundance Check) calculation in local networks.
The present code corresponds to a Cyclic Redundance Check calculate simulation, an error-detecting code frequently used in digital networks and storage devices to detect accidental changes in the raw data. 
It was performed in Python Language and its GUI Tkinter. 

CRC code operates as follows:

Considering the d-bits data sequence, D, which the sender node wants to transmite to the receiver node. Sender and receiver must to agree a pattern of r+1 bits first, known as generator, which we will denote by the letter G. We will impose the condicion that the most significant bit (the lef-most bit) of G is 1. For a given data sequence D, sender will select r additional bits, R, and add them to D, so that the resulting pattern of d+r bits (interpreted as a binary number) is exactly divisible by G (i. e, the pattern has no remaining).

The error-detecting process with CRC codes is, therefore, very simple: the receiver divides the d+r bits received by G. If the remaining is non-zero, receiver will know that an error has ocurred; otherwise, the data will be acepted as correct.

Thus, the present algorithm allows a simulation of the CRC code operation, in which the user will can type the binaries values corresponding to Message D and Generator G, and the program will return the bits patterns corresponding to CRC and G+r frame to be sent to receiver. The user can also modify this frame by emulating error in the transmited message, which the program will identify.
