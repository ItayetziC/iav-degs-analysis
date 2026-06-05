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
        description="Análisis de genes diferencialmente expresados en células infectadas con IAV"
    )
# Define los argumentos de línea de comandos con descripciones claras y valores por defecto
    parser.add_argument("--input", required=True, help="Ruta al archivo TSV de resultados DESeq2")
    parser.add_argument("--gff", required=True, help="Ruta al archivo GFF3 de anotaciones")
    parser.add_argument("--padj-threshold", type=float, default=0.05, help="Umbral de significancia (padj < umbral)")
    parser.add_argument("--lfc-threshold", type=float, default=1.0, help="Umbral absoluto de log2FoldChange")
    parser.add_argument("--output-dir", default="results/", help="Directorio para archivos de salida")

    return parser.parse_args()

def write_genes(genes: list, category: str, output_dir: str, annotations: dict):
    """
    Guarda una lista de genes en un archivo TSV.

    Parameters
    ----------
    genes : list
        Lista de genes a guardar.
    category : str
        Categoría de los genes (upregulated o downregulated).
    output_dir : str
        Directorio donde se guardará el archivo.
    annotations : dict
        Diccionario de anotaciones para agregar descripciones a los genes.
    """
# Construye la ruta completa del archivo usando el separador de rutas del sistema operativo
# y el nombre dinámico según la categoría (upregulated o downregulated    
    output_path = os.path.join(output_dir, f"{category}_genes.tsv")
    with open(output_path, "w") as f:
        
        f.write("gene_id\tlog2FoldChange\tpadj\tdescription\n")
# Escribe cada gen en el archivo, agregando la descripción desde el diccionario de anotaciones        
        for gene in genes:
            gene_id = gene["gene_id"]
            log2fc = gene["log2FoldChange"]
            padj = gene["padj"]
# Buscar descripción en el diccionario, si no existe usar "sin anotación"
            desc = annotations.get(gene_id, "sin anotacion")
            f.write(f"{gene_id}\t{log2fc:.4f}\t{padj:.6f}\t{desc}\n")

def write_summary_report(up_genes, down_genes, no_change_count, total_genes, annotations,
                         output_dir, input_file, gff_file, padj_thr, lfc_thr, extremes):
    """
    Genera el archivo summary_report.txt con el resumen del análisis.
    """
# Crea el directorio de salida si no existe    
    os.makedirs(output_dir, exist_ok=True)
# Construye la ruta completa del archivo de resumen 
    output_path = os.path.join(output_dir, "summary_report.txt")
    
    with open(output_path, "w") as f:
# Escribir cabecera
        f.write("=== ANALISIS DE GENES DIFERENCIALMENTE EXPRESADOS ===\n")
        f.write(f"Archivo DESeq2: {input_file}\n")
        f.write(f"Archivo GFF   : {gff_file}\n")
        f.write(f"Umbral padj   : {padj_thr}\n")
        f.write(f"Umbral |log2FC|: {lfc_thr}\n\n")
        
# Conteos de genes y porcentajes respecto al total
        up_count = len(up_genes)
        down_count = len(down_genes)
        f.write("--- RESULTADOS ---\n")
        f.write(f"Total genes analizados: {total_genes}\n")
        f.write(f"Upregulated   : {up_count} ({up_count/total_genes*100:.1f}%)\n")
        f.write(f"Downregulated : {down_count} ({down_count/total_genes*100:.1f}%)\n")
        f.write(f"No change     : {no_change_count} ({no_change_count/total_genes*100:.1f}%)\n\n")
        
        # Genes extremos (más inducido, más reprimido, más significativo) 
        f.write("--- GENES EXTREMOS (entre significativos) ---\n")
        f.write(f"Mas inducido  : {extremes['upregulated']['gene_id']}  log2FC = {extremes['upregulated']['log2FoldChange']:.4f}  padj = {extremes['upregulated']['padj']:.6f}\n")
        f.write(f"Mas reprimido : {extremes['downregulated']['gene_id']}  log2FC = {extremes['downregulated']['log2FoldChange']:.4f}  padj = {extremes['downregulated']['padj']:.6f}\n")
        f.write(f"Mas confiable : {extremes['most_significant']['gene_id']}  padj   = {extremes['most_significant']['padj']:.6f}\n\n")
        
        # Lista de genes upregulated con descripción
        f.write("--- GENES UPREGULATED ---\n")
        f.write("gene_id\tlog2FoldChange\tpadj\tdescription\n")
        for gene in up_genes:
            desc = annotations.get(gene["gene_id"], "sin anotacion")
            f.write(f"{gene['gene_id']}\t{gene['log2FoldChange']:.4f}\t{gene['padj']:.6f}\t{desc}\n")
        
        f.write("\n--- GENES DOWNREGULATED ---\n")
        f.write("gene_id\tlog2FoldChange\tpadj\tdescription\n")
        for gene in down_genes:
            desc = annotations.get(gene["gene_id"], "sin anotacion")
            f.write(f"{gene['gene_id']}\t{gene['log2FoldChange']:.4f}\t{gene['padj']:.6f}\t{desc}\n")

def main():
    args = parse_args()
    if not os.path.exists(args.input): 
        print(f"Error: el archivo de entrada '{args.input}' no existe")
        sys.exit(1)
    if not os.path.exists(args.gff):
        print(f"Error: El archivo GFF '{args.gff}' no existe.")
        sys.exit(1)
# Crea directorio de salida si no existe
    os.makedirs(args.output_dir, exist_ok=True)    
    genes = read_tsv(args.input)
    annotations = read_gff(args.gff)
    up_genes = []
    down_genes = [] 
    no_change_count = 0

    for gene in genes:
        category = classify_gene(gene["log2FoldChange"], gene["padj"], args.padj_threshold, args.lfc_threshold)
        if category == "upregulated":
            up_genes.append(gene)
        elif category == "downregulated":
            down_genes.append(gene)
        else:
            no_change_count += 1
    
    total_genes = len(genes)
    significant_genes = up_genes + down_genes
    if significant_genes:
        extremes = find_extremes(significant_genes)
    else:
        extremes = None  



    write_genes(up_genes, "upregulated", args.output_dir, annotations)  
    write_genes(down_genes, "downregulated", args.output_dir, annotations)
    write_summary_report(up_genes, down_genes, no_change_count, total_genes, annotations,
                         args.output_dir, args.input, args.gff, args.padj_threshold, args.lfc_threshold, extremes)
    
    print("=================================================")
    print("  Análisis DESeq2: IAV vs Mock")
    print(f"  Archivo: {args.input}")
    print(f"  GFF    : {args.gff}")
    print(f"  padj   : {args.padj_threshold}   |   |log2FC|: {args.lfc_threshold}")
    print("=================================================")
    print(f"Genes cargados del TSV  : {total_genes}")
    print(f"Genes cargados del GFF  : {len(annotations)}")
    print()
    print("--- Clasificación ---")
    up_count = len(up_genes)
    down_count = len(down_genes)
    print(f"  upregulated  : {up_count:3d}  ({up_count/total_genes*100:5.1f}%)")
    print(f"  downregulated: {down_count:3d}  ({down_count/total_genes*100:5.1f}%)")
    print(f"  no_change    : {no_change_count:3d}  ({no_change_count/total_genes*100:5.1f}%)")
    print()
    print("--- Genes extremos (significativos) ---")
    # Asegurarse de que extremes tenga valores válidos (puede ser que no haya significativos)
    if up_count + down_count > 0 and extremes is not None:
        print(f"  Más inducido  : {extremes['upregulated']['gene_id']:8s}   log2FC = {extremes['upregulated']['log2FoldChange']:.4f}  padj = {extremes['upregulated']['padj']:.6f}")
        print(f"  Más reprimido : {extremes['downregulated']['gene_id']:8s}   log2FC = {extremes['downregulated']['log2FoldChange']:.4f}  padj = {extremes['downregulated']['padj']:.6f}")
        print(f"  Más confiable : {extremes['most_significant']['gene_id']:8s}   padj   = {extremes['most_significant']['padj']:.6f}")
            
    else:
        print("  No se encontraron genes diferencialmente expresados con los umbrales dados.")

    print(f"Archivos guardados en: {args.output_dir}/")

if __name__ == "__main__":
    main()