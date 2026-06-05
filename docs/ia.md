## Documentación de uso de IA — Proyecto Análisis de DEGs

**Herramienta utilizada:** ChatGPT (modelo de asistencia)  
**Rol del estudiante:** Decisión sobre estructura del código, escritura de funciones, corrección de errores lógicos y de sintaxis.  
**Rol de la IA:** Orientación paso a paso, resolución de dudas técnicas, sugerencias de buenas prácticas y depuración.

---

### Fase 1 · Planificación y estructura general

- **Ayuda de implementación:**  
  La IA guió la organización del proyecto en dos módulos (`analyze_degs.py` y `deseq_utils.py`), explicó la conveniencia de separar funciones reutilizables del orquestador principal y recomendó el uso de `uv` para manejo de dependencias.

- **Decisiones del estudiante:**  
  El estudiante aceptó la estructura de dos archivos, definió los nombres de las funciones y estableció el flujo principal en `main()`.

---

### Fase 2 · Implementación de `deseq_utils.py`

#### Función `read_tsv`

- **Dudas técnicas:**  
  - ¿Por qué usar `csv.DictReader` en lugar de `split()` manual?  
  - ¿Cómo convertir columnas numéricas sin romper `gene_id`?  
  - ¿Qué hace `sys.exit(1)` y por qué es necesario?

- **Ayuda de implementación:**  
  La IA explicó la ventaja de `csv.DictReader` para manejo robusto de TSV, mostró cómo aplicar `try/except` para conversión de tipos y cómo usar `reader.line_num` para errores de línea. También aclaró la necesidad de convertir solo columnas numéricas a `float`.

- **Soporte técnico (correcciones):**  
  El estudiante inicialmente intentó convertir `gene_id` a `float`. La IA señaló el error y propuso la corrección manteniendo `gene_id` como cadena. El estudiante aplicó el cambio.

#### Función `read_gff`

- **Dudas técnicas:**  
  - ¿Cómo ignorar líneas de comentario (`#`)?  
  - ¿Cómo dividir la columna de atributos por `;` y luego por `=`?  
  - Diferencia entre `attr.split('=')` y `split('=', 1)`.

- **Ayuda de implementación:**  
  La IA proporcionó el patrón para leer líneas, dividir por tabulador, extraer la columna 9 y parsear atributos. Explicó la robustez de `split('=', 1)` para evitar problemas si la descripción contiene `=`. También sugirió usar `annotations.get(gene_id, "sin anotación")` para manejo seguro.

- **Soporte técnico (correcciones):**  
  El estudiante escribió una versión con `attr.startswith("Name=")` y `attr[5:]`. La IA señaló que ese método es frágil y recomendó la versión con `split`. El estudiante optó por mantener `startswith` por claridad, pero corrigió la asignación de `name` y `description` usando `split('=', 1)[1]`. También ajustó la condición de guardado para incluir `"sin anotación"`.

#### Funciones `classify_gene` y `find_extremes`

- **Dudas técnicas:**  
  - ¿Cómo usar `max()` y `min()` con `lambda`?  
  - ¿Qué hacer si la lista de genes está vacía?

- **Ayuda de implementación:**  
  La IA mostró la versión manual con un bucle `for` para que el estudiante entendiera la lógica antes de usar funciones de orden superior. Explicó cómo inicializar variables con el primer elemento y cómo comparar valores numéricos sin modificar los diccionarios originales.

- **Soporte técnico (correcciones):**  
  El estudiante inicialmente asignaba `upregulated["log2FoldChange"] = gene` (error de tipo). La IA detectó que se estaba reemplazando un número por un diccionario y corrigió la asignación a `upregulated = gene`. El estudiante incorporó la corrección y añadió manejo de lista vacía devolviendo tuplas con `"Ninguno"`.

---

### Fase 3 · Implementación de `analyze_degs.py`

#### Función `parse_arguments`

- **Dudas técnicas:**  
  - ¿Cómo definir argumentos obligatorios y opcionales con `argparse`?  
  - ¿Qué tipo de datos usar para `padj-threshold` y `lfc-threshold`?

- **Ayuda de implementación:**  
  La IA proporcionó el esqueleto con `add_argument` y explicó el parámetro `type=float` y `default`. Sugirió agregar mensajes `help` para cada argumento.

- **Decisiones del estudiante:**  
  El estudiante escribió la función, incluyó `required=True` para `--input` y `--gff`, y definió los valores por defecto.

#### Funciones `write_genes` y `write_summary_report`

- **Dudas técnicas:**  
  - ¿Cómo construir rutas seguras (Windows/Linux)?  
  - ¿Para qué sirve `os.makedirs(..., exist_ok=True)`?  
  - ¿Cómo formatear números a 4 y 6 decimales en f-strings?

- **Ayuda de implementación:**  
  La IA explicó `os.path.join` y el especificador de formato `:.4f` y `:.6f`. Mostró cómo usar `annotations.get()` para evitar `KeyError`. También aclaró la diferencia entre escribir en `write_genes` y dentro del reporte.

- **Soporte técnico (correcciones):**  
  El estudiante olvidó pasar `annotations` a `write_summary_report`. La IA detectó el error y sugirió agregar el parámetro. El estudiante lo incluyó y actualizó la llamada en `main`. También ajustó el formato de los archivos TSV para que coincidiera con el reporte.

#### Función `main` y salida en pantalla

- **Dudas técnicas:**  
  - ¿Cómo calcular porcentajes y alinear columnas en la impresión?  
  - ¿Qué hacer si no hay genes significativos?

- **Ayuda de implementación:**  
  La IA guió la creación del bucle de clasificación, el uso de `extremos = find_extremes(up_genes + down_genes)` y la impresión con formato de ancho fijo (`:8s`, `:8.4f`). También sugirió manejar el caso de lista vacía.

- **Soporte técnico (correcciones):**  
  El estudiante escribió `extremes = find_extremes(up_genes + down_genes + representative)` donde `representative` no existía. La IA señaló el error y lo corrigió a `significativos = up_genes + down_genes`. El estudiante aplicó el cambio y añadió una comprobación para imprimir mensaje si no hay significativos.

---

### Fase 4 · Pruebas y depuración final

- **Dudas técnicas:**  
  - ¿Cómo escribir pruebas unitarias con `pytest` para funciones que leen archivos?

- **Ayuda de implementación:**  
  La IA explicó cómo usar `tmp_path` para archivos temporales y `pytest.raises` para excepciones. Proporcionó ejemplos de pruebas para `classify_gene` y `find_extremes`.

- **Decisiones del estudiante:**  
  El estudiante implementó las pruebas en `tests/test_deseq_utils.py` siguiendo los ejemplos y verificó que pasaran con `uv run pytest`.

---

### Fase 5 · Soporte técnico posterior a la ejecución

- **Soporte técnico:**  
  - Ayuda para interpretar errores de `KeyError` cuando faltaba `annotations`.  
  - Corrección de la comparación numérica en `find_extremes` (evitar asignación incorrecta).  
  - Verificación de la salida en pantalla para que coincidiera con el formato solicitado (espacios, alineación).

---

### Fase 6. Documentación
  - Ayuda en redacción de documentos como README.md, diagrama_flujo y documentación con supervición del estuduiante y cambios 
**Declaración final:**  
El estudiante tomó todas las decisiones de diseño, escribió el código, realizó los cambios estructurales y corrigió los errores. La IA actuó como un recurso de consulta, proporcionando explicaciones, alternativas y detectando problemas lógicos. La documentación fue realizada por IA con cambios realizados por el estudiante