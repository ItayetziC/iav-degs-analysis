# tests/test_deseq_utils.py

from deseq_utils import classify_gene, find_extremes

def test_classify_upregulated():
    """Un gen con padj=0.01 y lfc=3.5 debe ser upregulated."""
    result = classify_gene(log2fc=3.5, padj=0.01, padj_thr=0.05, lfc_thr=2.0)
    assert result == "upregulated", f"Expected 'upregulated', got '{result}'"

def test_classify_downregulated():
    """Un gen con padj=0.01 y lfc=-2.0 debe ser downregulated."""
    result = classify_gene(log2fc=-2.0, padj=0.01, padj_thr=0.05, lfc_thr=2.0)
    assert result == "downregulated", f"Expected 'downregulated', got '{result}'"

def test_classify_no_change_by_padj():
    """Un gen con padj=0.8 aunque tenga lfc alto debe ser no_change."""
    result = classify_gene(log2fc=3.0, padj=0.8, padj_thr=0.05, lfc_thr=2.0)
    assert result == "no_change", f"Expected 'no_change', got '{result}'"

def test_classify_no_change_by_lfc():
    """Un gen significativo pero con lfc=0.3 debe ser no_change."""
    result = classify_gene(log2fc=0.3, padj=0.01, padj_thr=0.05, lfc_thr=2.0)
    assert result == "no_change", f"Expected 'no_change', got '{result}'"

def test_find_extremes_returns_correct_keys():
    """find_extremes debe retornar dict con las claves most_induced,
    most_repressed y most_significant."""
    genes = [
        {"gene_id": "gene1", "log2FoldChange": 3.0, "padj": 0.01},
        {"gene_id": "gene2", "log2FoldChange": -2.5, "padj": 0.02},
        {"gene_id": "gene3", "log2FoldChange": 1.0, "padj": 0.001},
    ]   
    extremes = find_extremes(genes)
    assert "most_induced" in extremes, "Expected key 'most_induced' in extremes"
    assert "most_repressed" in extremes, "Expected key 'most_repressed' in extremes"
    assert "most_significant" in extremes, "Expected key 'most_significant' in extremes"