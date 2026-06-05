```markdown
# Análisis de Genes Diferencialmente Expresados (DEGs) en respuesta a Influenza A

Este proyecto procesa los resultados de un experimento de RNA-seq (análisis DESeq2) para clasificar genes inducidos (`upregulated`) o reprimidos (`downregulated`) durante la infección por el virus de la Influenza A (IAV). Utiliza un archivo GFF de anotación humana para añadir descripciones funcionales a los genes diferencialmente expresados.

## Dataset: 
El análisis diferencial fue realizado con **DESeq2** -> ..datos\iav_deseq2_results.tsv
Las anotaciones usadas fueron obtenidas de https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9606 -> ..datos\human_genes.gff

## Dependencias y librerías

El proyecto usa la biblioteca estándar de Python más dos librerías externas:

| Librería       | Uso                                                          |
|----------------|--------------------------------------------------------------|
| `csv`          | Lectura del archivo TSV de resultados DESeq2                 |
| `argparse`     | Manejo de argumentos por línea de comandos                   |
| `os`, `sys`    | Manejo de rutas, creación de directorios, salida con errores |
| `matplotlib`   | (Opcional) Generación del volcano plot                       |
| `numpy`        | (Opcional) Soporte para el volcano plot                      |
| `pytest`       | (Solo desarrollo) Ejecución de pruebas unitarias             |

## Instalación y configuración

El proyecto está gestionado con **`uv`**, un gestor de entornos y dependencias rápido y moderno.

### 1. Clonar el repositorio

```bash
git clone <URL-de-tu-repositorio>
cd degs_analysis
```

### 2. Inicializar el entorno e instalar dependencias

```bash
uv init                     # si no existe pyproject.toml
uv add matplotlib numpy     # dependencias principales
uv add --dev pytest         # dependencias de desarrollo
```

### 3. Verificar la estructura de archivos

Tu repositorio debe contener:

```
degs_analysis/
├── analyze_degs.py
├── deseq_utils.py
├── tests/
│   └── test_deseq_utils.py
├── datos/
│   ├── iav_deseq2_results.tsv
│   └── human_genes.gff
├── pyproject.toml
├── uv.lock
└── README.md
```

> **Nota:** El archivo GFF se llama `human_genes.gff` aunque en el repositorio aparezca como `.txt`. No cambies su nombre, el programa lo maneja como GFF.

## 🧪 Ejecución del programa

El script principal es `analyze_degs.py`. Debes especificar al menos los archivos de entrada y opcionalmente los umbrales y directorio de salida.

### Comando básico

```bash
uv run python analyze_degs.py \
    --input datos/iav_deseq2_results.tsv \
    --gff datos/human_genes.gff
```

### Comando completo con todos los argumentos

```bash
uv run python analyze_degs.py \
    --input datos/iav_deseq2_results.tsv \
    --gff datos/human_genes.gff \
    --padj-threshold 0.05 \
    --lfc-threshold 1.0 \
    --output-dir results/
```

### Explicación de los argumentos

| Argumento            | Tipo    | Default       | Descripción                                                                 |
|----------------------|---------|---------------|-----------------------------------------------------------------------------|
| `--input`            | `str`   | **Requerido** | Ruta al archivo TSV con los resultados de DESeq2                            |
| `--gff`              | `str`   | **Requerido** | Ruta al archivo GFF3 de anotación (puede tener extensión `.gff` o `.txt`)   |
| `--padj-threshold`   | `float` | `0.05`        | Valor p ajustado máximo para considerar un gen significativo                |
| `--lfc-threshold`    | `float` | `1.0`         | Valor absoluto de `log2FoldChange` mínimo para clasificar (positivo o negativo) |
| `--output-dir`       | `str`   | `results/`    | Directorio donde se guardarán los archivos de salida                        |

## 📄 Archivos de salida

Dentro del directorio `--output-dir` se generan:

| Archivo                    | Contenido                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `upregulated_genes.tsv`    | Genes inducidos con `gene_id`, `log2FoldChange`, `padj` y descripción      |
| `downregulated_genes.tsv`  | Genes reprimidos (mismo formato)                                          |
| `summary_report.txt`       | Resumen completo (conteos, porcentajes, genes extremos y listas DE)       |
| `volcano_plot.png`         | **(Opcional)** Gráfico de volcano con los genes coloreados y etiquetados  |

## ✅ Pruebas unitarias

Las pruebas verifican la correcta clasificación de genes y el manejo de casos extremos.

```bash
uv run pytest tests/ -v
```

Se espera que todas las pruebas pasen sin errores.

## 📈 Volcano plot (punto opcional)

Si deseas obtener los 10 puntos extra, el programa generará automáticamente un gráfico de volcano (`volcano_plot.png`) en el directorio de salida. Para ello necesitas las librerías `matplotlib` y `numpy` (ya incluidas en las dependencias). El gráfico muestra:

- Eje X: `log2FoldChange`
- Eje Y: `-log10(padj)`
- Colores: rojo = upregulated, azul = downregulated, gris = no cambio
- Líneas punteadas en los umbrales
- Etiquetas para los 5 genes más significativos

## 🧠 Uso de IA

Durante el desarrollo de este proyecto se utilizó ChatGPT como apoyo para:
- Resolver dudas sobre manejo de archivos y estructuras de datos.
- Corregir errores lógicos (conversión de tipos, asignación de variables en `find_extremes`).
- Sugerir buenas prácticas (`os.path.join`, `annotations.get`, `try/except`).
- Ayudar en la depuración final y en la escritura de pruebas unitarias.

Todas las decisiones de diseño, la escritura del código y los cambios estructurales fueron realizados por el estudiante. La IA actuó como recurso de consulta y guía.

## 📌 Nota importante

- El archivo GFF suministrado (`human_genes.gff`) contiene solo un subconjunto de genes humanos relevantes para la respuesta inmune. Por lo tanto, algunos genes del análisis DESeq2 pueden quedar sin anotación (`"sin anotación"`).
- Los umbrales por defecto (`padj < 0.05` y `|log2FC| >= 1.0`) se pueden modificar según el criterio del usuario.

---

**¡Listo para ejecutar tu análisis de expresión diferencial contra el virus de la Influenza A! 🧬**
```