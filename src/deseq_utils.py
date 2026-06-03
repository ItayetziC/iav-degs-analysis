"""
Funciones auxiliares para analizar genes diferencialmente expresados.

Este módulo contiene funciones para leer archivos TSV de DESeq2,
leer anotaciones GFF3, clasificar genes e identificar genes extremos.
"""
import csv
import sys

def read_tsv(filepath: str) -> list[dict]:
    """
    Lee un archivo TSV con resultados de DESeq2.
    Parameters
    ----------
    filepath : str
        Ruta al archivo TSV.
    Returns
    -------
    list[dict]
        Lista de genes, donde cada gen es un diccionario.
    """
    genes = []
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for gene in reader:
                # Convertir las columnas numéricas a float
                try:
                    gene["baseMean"] = float(gene["baseMean"])
                    gene["log2FoldChange"] = float(gene["log2FoldChange"])
                    gene["lfcSE"] = float(gene["lfcSE"])
                    gene["stat"] = float(gene["stat"])
                    gene["pvalue"] = float(gene["pvalue"])
                    gene["padj"] = float(gene["padj"])
                except ValueError as e:
                    print(f"Error de conversión en línea {reader.line_num}: {e}")
                    print(f"Contenido problemático: {gene}")
                    sys.exit(1)
                # gene_id se deja como string
                genes.append(gene)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filepath}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado al leer '{filepath}': {e}")
        sys.exit(1)
    return genes

def read_gff(filepath: str) -> dict:
    """
    Lee un archivo GFF3 y extrae la descripción de cada gen.
    Parameters
    ----------
    filepath : str
        Ruta al archivo GFF3.
    Returns
    -------
    dict
        Diccionario con formato {gene_id: description}.
    """
    anotaciones = {}
    try:
        with open(filepath, "r") as f:
            for line in f:
                if not line or line.startswith("#"):
                    continue
                columns = line.strip().split("\t")
                if len(columns) < 9:
                    continue
                attributes = columns[8]
                # extraer Name y description
                name = None
                description = None
                for attr in attributes.split(";"):
                    if attr.startswith("Name="):
                        name = attr.split('=', 1)[1]
                    elif attr.startswith("description="):
                        description = attr.split('=', 1)[1]
                if name:
                    anotaciones[name] = description if description else "sin anotación"
    except FileNotFoundError: 
        print(f"Error: No se encontró el archivo '{filepath}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado al leer '{filepath}': {e}")
        sys.exit(1)
    return anotaciones

def classify_gene(
    log2fc: float,
    padj: float,
    padj_thr: float,
    lfc_thr: float
) -> str:
    """
    Clasifica un gen como upregulated, downregulated o no_change.

    Parameters
    ----------
    log2fc : float
        Log2 fold change del gen.
    padj : float
        Valor p ajustado.
    padj_thr : float
        Umbral máximo de padj para considerar significativo.
    lfc_thr : float
        Umbral mínimo de cambio en log2FoldChange.

    Returns
    -------
    str
        Una de: 'upregulated', 'downregulated', 'no_change'.
    """
    if padj < padj_thr and log2fc >= lfc_thr:
        return "upregulated"

    if padj < padj_thr and log2fc <= -lfc_thr:
        return "downregulated"

    return "no_change"

def find_extremes(genes): 
    if not genes:
        return "Lista de genes vacía"
    upregulated = genes[0]
    downregulated = genes[0]
    representative = genes[0]
    for gene in genes: 
        if gene["log2FoldChange"] > upregulated["log2FoldChange"]:
            upregulated["log2FoldChange"] = gene
        if(gene["log2FoldChange"] < downregulated["log2FoldChange"]): 
            downregulated["log2FoldChange"] = gene
        if(gene["padj"] < representative["padj"]):
            representative["padj"] = gene
    return{
        "most_induced": (upregulated["gene_id"], upregulated["log2FoldChange"], upregulated["padj"]),
        "most_repressed": (downregulated["gene_id"], downregulated["log2FoldChange"], downregulated["padj"]),
        "most_representative": (representative["gene_id"], representative["log2FoldChange"], representative["padj"])
    }