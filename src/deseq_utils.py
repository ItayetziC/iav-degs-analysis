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
def read_tsv(filepath: str) -> list[dict]:
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




















    with open(filepath, "r") as f:
        for line in f:
            if line.startswith("#") :
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
                    name = attr[5:]
                elif attr.startswith("description="):
                    description = attr[12:]
            if name and description:
                annotations[name] = description

    return annotations

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


def find_extremes(genes: list[dict]) -> dict:
    """
    Encuentra los genes extremos entre los genes significativos.

    Parameters
    ----------
    genes : list[dict]
        Lista de genes significativos.

    Returns
    -------
    dict
        Diccionario con los genes más inducido, más reprimido
        y más significativo.
    """
    extremes = {
        "most_induced": None,
        "most_repressed": None,
        "most_significant": None,
    }

    for gene in genes:
        if extremes["most_induced"] is None or gene["log2FoldChange"] > extremes["most_induced"]["log2FoldChange"]:
            extremes["most_induced"] = gene

        if extremes["most_repressed"] is None or gene["log2FoldChange"] < extremes["most_repressed"]["log2FoldChange"]:
            extremes["most_repressed"] = gene

        if extremes["most_significant"] is None or gene["padj"] < extremes["most_significant"]["padj"]:
            extremes["most_significant"] = gene

    return extremes