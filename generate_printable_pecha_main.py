from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os, time

target_folder = 'C:\\Users\\HP\\Desktop\\Dharma\\Pecha\\_Py'
pdfs = []

#PASO1 Buscar todos los pdfs en la carpeta
for file in os.listdir(target_folder):
    if file.lower().endswith('.pdf'):
        pdfs.append(file)

    print("La lista de archivos es: ", pdfs)

    #Unir los pdfs
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    
#Generar el pdf resultante en la carpeta
merger.write('paso1-merged.pdf')
merger.close()

#Centrar los bordes de la pecha
os.system("pdflatex paso1-merged-centered.tex")

#Leer el archivo 'paso1-merged.pdf' y obtener su número de páginas.
mergedCenteredPdf = PdfFileReader('paso1-merged-centered.pdf')
num_pages = mergedCenteredPdf.getNumPages()

#PASO 2 Crear writers vacíos y advertir si el número de páginas no es divisible por 4.
evenWriter = PdfFileWriter()
oddWriter = PdfFileWriter()

#Advertir si el numero de páginas es divisible por 4

CEND = '\033[0m' #Sirve para dar color a las advertencias.

if num_pages%4 != 0:
    CRED = '\033[91m'    
    print(CRED + "OJO!" + CEND +" la cantidad de páginas no es divisible por 4!")    
else: 
    CGREEN2  = '\33[92m'
    print(CGREEN2 + "OK!" +CEND+" la cantidad de páginas SI es divisible por 4!")
rotation = input("Quieres las páginas pares rotadas? Y/N ")
print("rotation is: " + rotation)
time.sleep(1.5)

#Rotar páginas pares de paso1-merged.pdf e ir escribiendo en su respectivo Writer
for i in range (num_pages):
    page = mergedCenteredPdf.getPage(i)
    if i%2 == 0:                    #si la página es impar, agregar al writer... (ojo: numeración empieza en cero)
        oddWriter.addPage(page)
    else:                           #si la página es par, rotar y agregar al writer
        if rotation in ['y', 'Y', 'yes', 'Yes', 'YES']:
            page.rotateClockwise(180)

        evenWriter.addPage(page)

#Generar los pdfs resultantes en la carpeta
rotatedPdfOdd = open('paso2-rotated-odd.pdf', 'wb')
oddWriter.write(rotatedPdfOdd)
rotatedPdfOdd.close()

rotatedPdfEven = open('paso2-rotated-even.pdf', 'wb')
evenWriter.write(rotatedPdfEven)
rotatedPdfEven.close()

#PASO 3 imprimir páginas impares en un archivo con X pechas por hoja (No cambiar tamaño!)
os.system("pdflatex paso3-nup-odd.tex")
os.system("pdflatex paso3-nup-even.tex")

#PASO4 Mezclar archivos con páginas pares e impares
#Leer los archivos 'paso3-nup-odd.pdf' y 'paso3-nup-even.pdf' y obtener su número de páginas.
nupOdd  = PdfFileReader('paso3-nup-odd.pdf')
nupEven = PdfFileReader('paso3-nup-even.pdf')
num_final_pages = nupOdd.getNumPages() #el archivo paso3-nup-odd.pdf y paso3-nup-even.pdf deberían tener la misma cantidad de páginas

print("num_final_pages" + str(num_final_pages))

#crear writer para el paso corespondiente y recorrer para mezclar
mixedWriter = PdfFileWriter()

for i in range (num_final_pages):
    oddPage = nupOdd.getPage(i)
    evenPage = nupEven.getPage(i)

    mixedWriter.addPage(oddPage)
    mixedWriter.addPage(evenPage)

#Generar el pdf resultante en la carpeta
mixedPdf = open('paso4-mixed.pdf', 'wb')
mixedWriter.write(mixedPdf)
mixedPdf.close()

#PASO5 Cortar pdf de tamaño LEGAL a OFICIO
mixedPdfReader = PdfFileReader('paso4-mixed.pdf','r')
num_pages = mixedPdfReader.getNumPages()
finalWriter = PdfFileWriter()

for i in range (num_pages):
    page = mixedPdfReader.getPage(i)
    page.cropBox.setLowerLeft((36.283,0))
    page.cropBox.setUpperRight((971.716,612))
    finalWriter.addPage(page)

outstream=open('paso5-final.pdf','wb')
finalWriter.write(outstream)
outstream.close()

#Borrar archivos generados en la carpeta y dejar el resultado final
os.system("cleanFolder.bat")