
# Examen Teórico — Python para Bioinformática

## Opción Múltiple

  

**Licenciatura en Ciencias Genómicas — UNAM · 2026**

**Valor:** 1 punto por pregunta correcta · **Sin penalización** por error

**Instrucciones:** Selecciona la única opción correcta para cada pregunta.

  

---
## Bloque A · Python — Fundamentos, ciclos y condicionales

  

**1.** ¿Cuál es la diferencia entre una lista y una tupla en Python?
  

- a) Las listas son inmutables; las tuplas son mutables

- b) Las listas son mutables; las tuplas son inmutables

- c) Ambas son mutables, pero las tuplas no permiten duplicados

- d) Las tuplas solo pueden contener valores numéricos

  **Mi respuesta es b)**
  >  Las listas son mutables, por lo que se le pueden agregar o eliminar elementos después de haber sido 
  >  creadas, mientras que las tuplas son inmutables, es decir una vez creadas no se pueden modificar (adecuadas para claves de diccionarios

---

  

**2.** Dado el siguiente código, ¿qué imprime?

 ```python

genes = ["IFIT1", "MX1", "GAPDH"]

for i, g in  enumerate(genes):

if i % 2 == 0:

print(g)

```

  

- a) `MX1`

- b) `IFIT1` y `GAPDH`

- c) `IFIT1`, `MX1` y `GAPDH`

- d) `IFIT1` y `MX1`
 
---

** Mi respuesta es b  **
> enumarate enumera los genes con i junto con los elementos que contiene, por lo que al iterar sobre el índice (i) y los genes (g) si i es igual a 0 y 2 o en general los numeros pares imprimirá g (los genes)

  

**3.** ¿Cuál es el resultado de ejecutar el siguiente fragmento?

  

```python

resultado = []

  
for x in  range(4):

if x > 1:

resultado.append(x**2)

  

print(resultado)

```

- a) `[0, 1, 4, 9]`

- b) `[4, 9]`

- c) `[1, 4, 9]`

- d) `[4, 6]`

---

** Mi respuesta es b **
> x itera 4 veces, donde se va incrementando su valor por cada iteración. Cuando x sea mayor a 1, se agrega en la lista x al cuadrado. Cuando se imprime resultado imprime 4 y 9 (empieza desde 0 hasta 3 x) 

## Bloque B · Manejo de errores con `try/except`

  
  

**4.** ¿Qué imprime el siguiente código?

  

```python

try:

values = {"padj": "NA"}

v = float(values["padj"])

except  ValueError:

print("valor no numérico")

except  KeyError:

print("clave no encontrada")

```

  

- a) `clave no encontrada` y `fin del bloque`

- b) `valor no numérico` y `fin del bloque`

- c) Solo `valor no numérico`

- d) Solo `fin del bloque`

** Mi respuesta es c¨**
> Valor no numérico, porque el valor de padj es NA (string) y no puede convertirse a float, por lo que sería un error y no hay ningun sys.exit(1) o un comando para finalizar forzosamente el programa por lo que no estoy segura de considerarlo ' fin del bloque '

---

  

**5.** Al leer el archivo `iav_deseq2_results.tsv`, una línea tiene "NA" en una columna que debe convertirse a float. ¿Qué estrategia es más adecuada?

  - a) Ignorar todos los errores usando except Exception

- b) Usar try/except ValueError al convertir el valor

- c) Convertir directamente con float() sin validación

- d) Terminar el programa inmediatamente si ocurre un error


---

** Mi respuesta es b ** 
> Es necesario usar un try/except para que pueda avisarnos si hay un error y poder corregirlo de forma controlada (como asignarle un "None" o no contarlo para el resultado final o salirse del programa una vez mandado un mensaje, dependiendo de la implementación que se le quiera dar posteriormente 
  

## Bloque C · Archivos y formatos bioinformáticos

  

**6.** ¿Cuál es la forma correcta de abrir un archivo en Python garantizando que se cierre

aunque ocurra un error?

  

- a) `f = open("archivo.tsv"); datos = f.read(); f.close()`

- b) `with open("archivo.tsv") as f: datos = f.read()`

- c) `try: f = open("archivo.tsv") except: f.close()`

- d) `open("archivo.tsv", autoclose=True)`

  ** Mi respuesta es b**
> with Garantiza el cierre del archivo incluso si ocurre una excepción. 



---

**7.** En el archivo `human_genes.gff`, la columna 9 de una línea contiene:
```
ID=ENSG0001_MX1;Name=MX1;description=GTPase antiviral;gene_type=protein_coding
```
 

¿Qué produce el siguiente código?

  

```python

attrs = {}

for campo in col9.split(";"):

if  "="  in campo:

k, v = campo.split("=", 1)

attrs[k] = v

```

  

- a) Un error porque `split("=", 1)` no es válido

- b) Un diccionario `{"ID": "ENSG0001_MX1", "Name": "MX1", "description": "GTPase antiviral", "gene_type": "protein_coding"}`

- c) Una lista de tuplas con los pares clave-valor

- d) Solo el primer campo porque el loop se detiene en el primer `;`

---
** Mi respuesta es b ** 
> se crea un diccionario donde id es la clave (porque va antes del = ) y el valor es todo lo que le sigue al = 

  

**8.** ¿Por qué es importante usar `split("=", 1)` (con el argumento `1`) al parsear los

atributos del GFF en lugar de `split("=")`?

  

- a) Por eficiencia: es más rápido

- b) Para evitar dividir en más de dos partes si el valor contiene el carácter `=`

- c) Porque `split("=")` no funciona con cadenas que contienen `;`

- d) No hay diferencia; ambas formas producen el mismo resultado

 ** Mi respuesta es b **
> Permite dividir en dos cadenas, una para el valor y otra para el caracter, de otra forma, solo accederería hasta el primer = y no todo lo demás
  

## Bloque D · Funciones, módulos y buenas prácticas

**9.** ¿Cuál es la diferencia entre un **parámetro** y un **argumento** en Python?

  
- a) Son sinónimos; se pueden usar indistintamente

- b) El parámetro es la variable en la definición de la función; el argumento es el valor

que se pasa al llamarla

- c) Los argumentos se definen con `def`; los parámetros se pasan al llamar la función

- d) Los parámetros son siempre opcionales; los argumentos son siempre obligatorios

  ** Mi respuesta es b**
>  El parámetro es la forma que interpreta la función el valor, mientras que el argumento es el valor que se le pasa cuando se le llama

---

  

**10.** ¿Qué ventaja tiene documentar una función con docstring en formato NumPy/Google style

(con secciones `Parameters` y `Returns`) en lugar de un comentario simple?

  

- a) Es la única forma que Python reconoce; los comentarios simples son ignorados

- b) Los docstrings son accesibles en tiempo de ejecución con `help()`, son procesados por

herramientas como Sphinx y sirven como contrato explícito de la función

- c) Los docstrings hacen que el código corra más rápido

- d) Solo es necesario en funciones con más de 5 parámetros
---
** Mi respues es b ** 
> Los docstrings pueden servir como un contrato de qué debe cumplir una función y permiten mantener los documentos de forma más controlada 



**11.** ¿Cuál de los siguientes nombres de variable sigue mejor las convenciones de

estilo (PEP 8) para Python?

  

- a) `LogFoldChange`

- b) `log2FoldChange`

- c) `log2_fold_change`

- d) `L2FC`

  

---
** Mi respuesta es b**
> Porque se entiende qué es cual es el logaritmo y está todo junto (sin espacio) 
  

## Bloque E · Argumentos por línea de comandos

  

**12.** ¿Cuál es la diferencia entre `add_argument("--lfc-threshold")` y

`add_argument("lfc_threshold")` en `argparse`?

  

- a) No hay diferencia; ambas formas crean el mismo argumento

- b) `--lfc-threshold` crea un argumento opcional (flag); `lfc_threshold` crea un argumento

posicional obligatorio

- c) `lfc_threshold` con guion bajo no es válido en `argparse`

- d) `--lfc-threshold` solo funciona en Linux; `lfc_threshold` es multiplataforma

  ---
** Mi respuesta es b **
> permite designar aquellos arguments posicionales obligatorios u opcionales que hay un valor estandar establecido

  

**13.** Un script con `argparse` se ejecuta con el comando:

  

```bash

python  analyze_degs.py  --input  datos/resultados.tsv  --lfc-threshold  2.0

```

  

¿Cómo se accede al valor `2.0` dentro del script?

  

- a) `args["lfc-threshold"]`

- b) `args.lfc_threshold`

- c) `args.lfc-threshold`

- d) `args.get("lfc_threshold")`

  ** Mi respuesta es b  **
  > Se optine desde arg.variable, pero se cambia el - por guión bajo par aque sea reconocido como variable (no resta)

---

  

## Bloque F · Git y GitHub

  

**14.** ¿Cuál es el orden correcto de comandos para registrar cambios locales y

subirlos a GitHub?

  

- a) `git push` → `git commit -m "msg"` → `git add archivo.py`

- b) `git add archivo.py` → `git commit -m "msg"` → `git push`

- c) `git commit -m "msg"` → `git add archivo.py` → `git push`

- d) `git push` → `git add archivo.py` → `git commit -m "msg"`

  ---
** Mi respuesta es **
  > Primero debe añadirse el documento del git, luego se añade un commit que describa la acción relizada y luego se publica en github en nuestro branch

**15.** ¿Cuál de los siguientes mensajes de commit está mejor escrito según convenciones comunes como Conventional Commits?

  

- a) docs: update README with installation steps

- b) feat add new parser

- c) new changes

- d) chore fixing bug in filter

  
  ** Mi respuesta es  a**
> De esta forma decimos qué tipo de cambio se relizó y cuál fue específicamente
---

  

**16.** Estás trabajando en un proyecto que usa GitHub y tienes un archivo llamado credentials.txt con contraseñas y claves de acceso. ¿Qué es lo más recomendable hacer?

  

- a) Subirlo al repositorio para que todos puedan usarlo

- b) Renombrarlo antes de subirlo

- c) Agregarlo al archivo .gitignore

- d) Comprimirlo en .zip antes de subirlo

  
  ** Mi respuesta es  c**
  con .gitignore son aquellos archivos que se encuentran en el repo local, pero no se vuelve publico (lo ignora github) 

---

  

## Bloque G · Gestión de entornos con `uv`

  

**17.** ¿Cuál es la diferencia entre `uv add matplotlib` y `uv add --dev pytest`?

  

- a) No hay diferencia práctica; ambos instalan paquetes en el mismo entorno

- b) `uv add` registra la dependencia en `[project.dependencies]` del `pyproject.toml`;

`uv add --dev` la registra en `[tool.uv.dev-dependencies]`, que no se instala en

producción

- c) `--dev` instala el paquete de forma global en el sistema

- d) `uv add --dev` es solo un alias más verboso de `uv add`

   
** Mi respuesta es b **
> uv add se intala tanto en el desarrollo como en la producción mientras que uv add --dev no se intalaría en la producción


---

  

**18**. En un proyecto de Python administrado con uv, ¿cuál es la mejor práctica para asegurar que otras personas puedan recrear el mismo entorno de trabajo?

  

- a) Subir únicamente los archivos .py

- b) Compartir solo la versión de Python instalada localmente

- c) Incluir archivos como pyproject.toml en el repositorio

- d) Subir la carpeta completa .venv a GitHub
** Mi respuesta es  c**
  Incluir la forma en la que se instala el proyecto y las dependencias que tiene que instalarse para su correcto funcionamiento

---

  

## Bloque H · Pruebas con `pytest`

  

**19.** ¿Cuál es el principal propósito de las pruebas (tests) en un proyecto de programación?

  

- a) Hacer que el código se ejecute más rápido

- b) Verificar que el código funciona como se espera

- c) Reducir el tamaño de los archivos del proyecto

- d) Evitar usar git

  ** Mi respuesta es b**
  > nos permite hacer prubeas para evaluar su correcto funcionamiento

---

  

**20.** ¿Cuál es un test válido en pytest para la función suma(2, 3)?

  

- a) assert suma(2, 3) == 5

- b) print(suma(2, 3))

- c) suma(2, 3) = 5

- d) echo suma(2, 3)

  
  ** Mi respuesta es a**
> se le indica la función, los argumento y el valor que debería dar
---

  

## Bloque I · GitHub Copilot — Ask, Plan y Agent

  

**21.** ¿Cuál es la diferencia entre el modo **Ask** y el modo **Agent** de GitHub Copilot?

  

- a) Ask es para preguntas sobre código existente; Agent puede crear archivos, ejecutar

comandos y modificar múltiples archivos de forma autónoma para completar una tarea

- b) Ask genera código completo; Agent solo responde preguntas de documentación

- c) Agent funciona solo en proyectos con Git inicializado; Ask funciona en cualquier archivo

- d) No hay diferencia funcional; son nombres distintos para la misma característica

  
  ** Mi respuesta es  a**
  >al usar ask se le puede preguntar con base en un codigo, mientras que aget auyuda a relizar codigo desde 0 por medio de un prompt

---

  

**22.** Estás usando el modo **Plan** de Copilot para diseñar tu solución antes de escribir

código. ¿Cuál es el propósito principal de este modo?

  

- a) Escribir el código completo del proyecto automáticamente sin intervención del usuario

- b) Generar un plan de implementación paso a paso que puedes revisar, ajustar y aprobar

antes de que Copilot empiece a escribir código

- c) Detectar errores de sintaxis en el código ya escrito

- d) Crear diagramas UML del proyecto

  
  ** Mi respuesta es  b**
> Permite tener claro el razonamiento y pasos lógicos que hará el programa antes de codificar, permite ser más certero de qué hará y cómo lo hará
---

  

**23.** Al usar Copilot en modo **Ask** para entender una función de tu código, ¿cuál de los

siguientes prompts producirá la respuesta más útil?

  

- a) `"explica esto"`

- b) `"¿qué hace esta función y qué tipo de datos espera en cada parámetro?"`

- c) `"¿es buena práctica?"`

- d) `"arréglalo"`

  
  ** Mi respuesta es b**
  > permite dar una respuesta específica y certera, para poder entender el comportmiento de dicha función 
  ---

  

**24.** En el contexto del **uso consciente de IA**, ¿cuál de las siguientes afirmaciones

describe mejor la responsabilidad del programador al usar Copilot?

  

- a) Si Copilot genera el código, el programador no es responsable de los errores que tenga

- b) El programador debe revisar, entender y validar todo el código generado por Copilot,

documentar qué fue generado y qué modificó, y ser capaz de explicar cada línea

- c) El código generado por IA siempre es correcto y no necesita revisión si viene de un

modelo entrenado en código de alta calidad

- d) Está prohibido usar Copilot en un contexto académico porque constituye deshonestidad

 
  ** Mi respuesta es b**
> La IA es una herramienta que se debe usar con honestidad y no como un agente que sustituye al programador, el objetivo es que podamos comprender el código 
---

  

## Bloque J · Diagramas y documentación

  

**25.** Observa el siguiente fragmento en

  

```

flowchart TD

A{padj < 0.05?}

A -->|Sí| B[Significant]

A -->|No| C[Not significant]

```

  

¿Qué representa mejor este diagrama?

  

- a) Una comparación entre archivos

- b) Una decisión basada en una condición

- c) Un test de pytest

- d) Una instalación de paquetes

  
  ** Mi respuesta es b**
> Representa una comparación entre 2 archivos lo que nos permite entender visualemente el proceo a realizar
---

  

**26.** ¿Qué diferencia hay entre un **documento de requisitos** y un **documento de diseño**

en el desarrollo de software?

  

- a) Son el mismo documento con distinto nombre según la empresa

- b) El documento de requisitos describe **qué** debe hacer el sistema (funcionalidades,

restricciones); el documento de diseño describe **cómo** se implementará

(módulos, estructuras de datos, flujo)

- c) El documento de diseño se escribe antes que el de requisitos

- d) Solo los proyectos grandes necesitan documentos de requisitos; los scripts pequeños

no los requieren

  
  ** Mi respuesta es b**
  > El documento de requisitos es para comprender que requiere para su ejecución y el documento de diseño funciona para comprender su diseño 

---

  

## Refactorización, módulos y manejo de datos
 
**27.** ¿Cuál es una ventaja de dividir un programa en funciones pequeñas con responsabilidades claras?

- a) Hace más difícil reutilizar el código

- b) Facilita leer, probar y mantener el programa

- c) Evita usar módulos

- d) Elimina la necesidad de comentarios

  
  ** Mi respuesta es b**
>Así podemos revisar funciones con una sola responsabilidad para revisar si funciona o corregirla de forma eficiente, mantener el programa y probarlo 
---

**28.** ¿Qué situación sugiere que una función debería refactorizarse?
- a) La función realiza varias tareas diferentes

- b) La función tiene un nombre descriptivo

- c) La función recibe parámetros

- d) La función usa `return`
 
  ** Mi respuesta es a**
> La refactorización permite dividir una función en varias para designar tareas congretas a cada una de las funciones derivadas de esa 
---

  

**29.** ¿Cuál es una ventaja de colocar funciones relacionadas en un módulo?

  

- a) Evitar usar `import`

- b) Organizar y reutilizar mejor el código

- c) Hacer que Python compile más rápido

- d) Reemplazar los tests

  
  ** Mi respuesta es b**
> Permite agrupar por funciones generales el codigo, nos permite reutilizarlo y organizarlo para mejorar la comprensión

---

  

**30.** En `pandas`, ¿qué estructura representa una tabla con filas y columnas?

  

- a) `Series`

- b) `DataFrame`

- c) `dict`

- d) `tuple`

  
  ** Mi respuesta es b**
> DataFrame está ordenado en 2 dimensiones (filas y columnas) similar a una tabla de base de datos
---

  

**31.** ¿Cuál de las siguientes operaciones es común al trabajar con `DataFrame`?

  

- a) Filtrar filas según una condición

- b) Compilar código Python

- c) Ejecutar `pytest`

- d) Crear módulos automáticamente

  
  ** Mi respuesta es  a**
>  Permite obtener de forma eficiente una fila a partir de  una condición 