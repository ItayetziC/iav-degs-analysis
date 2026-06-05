# Diagrama del flujo del proyecto
```mermaid
flowchart TD
    A[Inicio] --> B[Parsear argumentos: --input, --gff, umbrales, --output-dir]
    B --> C{¿Archivos existen?}
    C -- No --> D[Mostrar error y salir]
    C -- Sí --> E[Crear directorio de salida]
    E --> F[Leer TSV con read_tsv → lista de genes]
    E --> G[Leer GFF con read_gff → dict anotaciones]
    F --> H[Clasificar cada gen con classify_gene]
    H --> I[Separar en up_genes, down_genes, contar no_change]
    I --> J[Calcular total_genes]
    J --> K[Identificar genes extremos con find_extremes]
    K --> L[Escribir TSV: upregulated_genes.tsv y downregulated_genes.tsv]
    L --> M[Generar summary_report.txt con write_summary_report]
    M --> N[Imprimir resumen en pantalla]
```

# ── Uso de IA ───────────────────────────────────────────────
# Herramienta : Deepseek
# Prompt usado: "crea un diagrama de flujo tipo Mermaid con el pipeline del proyecto"
# Qué generó  : generó el diagrama de flujo del proyecto
# Qué modifiqué: reducí y reestructuré flujo
# ────────────────────────────────────────────────────────────
