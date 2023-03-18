printPecha project:
Is a set of Python and TeX files to generate printable tibetan pechas: https://en.wikipedia.org/wiki/Pecha

Spanish:
Proyecto printPecha:
Es un set de archivos Python y TeX diseñado para preparar la impresión de textos en formato Pecha: https://en.wikipedia.org/wiki/Pecha

PREREQUISITOS

> python: Para correr algoritmo principal alojado en

    			pecha_pdf_project_main.py

> pdflatex: Para correr los scripts de LaTeX
> paso1-merged-centered.tex
> paso3-nup-odd.tex
> paso3-nup-even.tex
> MiKTeX > instalar los paquetes:

    	pdfpages > https://ctan.org/pkg/pdfpages?lang=en

> PyPDF2: Biblioteca con funciones necesarias de manejo de PDF

    	https://pypi.org/project/PyPDF2/
    	simplemente ejecutar el comando en terminal:
    		pip install PyPDF2

ALGORITMO

Cada uno de los pasos citados aqui genera un archivo que inicia con "pasoX", en donde X corresponde al numero de paso corespondiente:

1.1 Hacer un merge de todos los pdfs necesarios y completar paginas para que no hayan sobras de papel
1.2 Centrar el archivo unificado
2 Rotar pàginas pares: https://deftpdf.com/rotate-pdf-pages
3.1 imprimir páginas impares en un archivo con X pechas por hoja (No cambiar tamaño LEGAL)
3.2 hacer lo mismo con las páginas pares en otro archivo (No cambiar tamaño LEGAL)
4 Mezclar archivos con páginas pares e impares https://deftpdf.com/es/alternate-mix-pdf
5 Imprimir ultimo archivo en tamaño final (OFICIO colombiano)
usar https://deftpdf.com/crop-pdf
con los siguientes parametros:
top 0, right 0.505, bottom 0, left 0.505

PARA USAR

Simplemente pegar los archivos en la carpeta \_Py, y ejecutar el archivo generate_printable_pecha_main.py.

En caso de no reconocer los archivos (FileNotFoundError: [Errno 2]), intentar en DEBUG

CUIDADO, al finalizar se eliminarán los archivos que han sido pegados en la carpeta y únicamente quedará el pdf resultante del proceso
