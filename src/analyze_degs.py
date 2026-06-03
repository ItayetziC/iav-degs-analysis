import os
import sys
import argparse

from deseq_utils import read_tsv, read_gff, classify_gene, find_extremes


def parse_args():
    """
    Define y obtiene los argumentos de línea de comandos.

    Returns
    -------
    argparse.Namespace
        Argumentos ingresados por el usuario.
    """
    parser = argparse.ArgumentParser(
        description="Análisis de genes diferencialmente expresados"
    )

    parser.add_argument("--input", required=True, help="Ruta al archivo TSV de resultados DESeq2")
    parser.add_argument("--gff", required=True, help="Ruta al archivo GFF3 de anotaciones")
    parser.add_argument("--padj-threshold", type=float, default=0.05, help="Umbral de significancia (padj < umbral)")
    parser.add_argument("--lfc-threshold", type=float, default=1.0, help="Umbral absoluto de log2FoldChange")
    parser.add_argument("--output-dir", default="results/", help="Directorio para archivos de salida")

    return parser.parse_args()

def write_genes(genes, category, output_dir): 
    args = parse_args()
    if not os.path.exists(args.input): 
        print(f"Error: el archivo de entrada '{args.input}' no existe")
        sys.exit(1)
    if not os.path.exists(args.gff):
        print(f"Error: El archivo GFF '{args.gff}' no existe.")
        sys.exit(1)
# Crea directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)    
    for gene in genes: 
        


def main():
    args = parse_args()
    genes = read_tsv(genes)


















    try:
        genes = read_tsv(args.input)
        annotations = read_gff(args.gff)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        sys.exit(1)

    upregulated = []
    downregulated = []
    no_change = []

    for gene in genes:
        category = classify_gene(
            gene["log2FoldChange"],
            gene["padj"],
            args.padj_threshold,
            args.lfc_threshold
        )

        gene["category"] = category

        if category == "upregulated":
            gene["description"] = annotations.get(
                gene["gene_id"],
                "sin anotación"
            )
            upregulated.append(gene)

        elif category == "downregulated":
            gene["description"] = annotations.get(
                gene["gene_id"],
                "sin anotación"
            )
            downregulated.append(gene)

        else:
            no_change.append(gene)

    significant_genes = upregulated + downregulated
    extremes = find_extremes(significant_genes)

    os.makedirs(args.output_dir, exist_ok=True)

    # Aquí después agregas:
    # guardar upregulated_genes.tsv
    # guardar downregulated_genes.tsv
    # guardar summary_report.txt
    # imprimir resumen en pantalla


if __name__ == "__main__":
    main()