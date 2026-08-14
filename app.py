import streamlit as st
import pandas as pd
import numpy as np
import numpy_financial as npf
import openpyxl
import requests
import io
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="DCF Project Calculator", layout="wide", page_icon="📊")

# ===== MÁRGENES / PADDING DE LA APP (edita estos valores) =====
PAGE_MAX_WIDTH    = "90vw"   # ancho máximo del contenido (acepta vw, px, %, etc.)
PAGE_PADDING_TOP  = "1.5rem" # espacio arriba, antes del título
PAGE_PADDING_LEFT  = "1rem"  # margen izquierdo del contenido
PAGE_PADDING_RIGHT = "1rem"  # margen derecho del contenido

# ===== ANCHO DE ETIQUETAS DE TÍTULO =====
# Las tablas ocupan el 100% del ancho disponible (use_container_width), así que
# los títulos usan el mismo 100% para quedar alineados con ellas.
SECTION_HDR_WIDTH  = "100%"  # ancho de los títulos de sección (INFLOWS, OUTFLOWS, TOTALES, etc.)
SUBGROUP_HDR_WIDTH = "100%"  # ancho de las etiquetas de subgrupo (REVENUE, COSTS & EXPENSES, etc.)

st.markdown(f"""
<style>
section[data-testid="stSidebar"] {{ display: none; }}
.main .block-container {{
    padding-top: {PAGE_PADDING_TOP};
    max-width: {PAGE_MAX_WIDTH} !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: {PAGE_PADDING_LEFT};
    padding-right: {PAGE_PADDING_RIGHT};
}}
.kpi-card {{
    background: #ffffff; border-radius: 10px; padding: 14px 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10); text-align: center;
    margin-bottom: 12px; min-height: 110px;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
}}
.kpi-label {{ font-size: 10px; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 0.5px; line-height: 1.4; }}
.kpi-val   {{ font-size: 20px; font-weight: 900; color: #0052FF; margin: 6px 0 3px; }}
.kpi-sub   {{ font-size: 10px; color: #999; }}
.kpi-val-green {{ font-size: 20px; font-weight: 900; color: #00875A; margin: 6px 0 3px; }}
.section-hdr {{
    font-size: 13px; font-weight: 800; color: #0052FF;
    letter-spacing: 2px; text-transform: uppercase;
    border-left: 4px solid #0052FF; padding-left: 10px; margin: 20px 0 6px;
    width: {SECTION_HDR_WIDTH}; box-sizing: border-box;
}}
.subgroup-hdr {{
    background: #F5F0C8; padding: 5px 12px 5px 16px;
    font-size: 11px; font-weight: 800; letter-spacing: 1.2px;
    color: #5D4E0D; border-left: 4px solid #C8A800;
    margin: 6px 0 1px 0;
    width: {SUBGROUP_HDR_WIDTH}; box-sizing: border-box;
}}
.page-title {{ font-size: 26px; font-weight: 900; color: #0052FF; letter-spacing: 1px; }}
.page-sub   {{ font-size: 13px; color: #888; margin-top: -4px; }}
</style>
""", unsafe_allow_html=True)

# ===== ANCHOS DE TABLAS (edita estos valores) =====
TABLES_USE_FIXED_WIDTH = False   # True = usar anchos fijos definidos abajo, False = ocupar todo el ancho disponible
CONCEPT_COL_WIDTH = 220         # ancho columna "Concepto" en px (tablas INFLOWS/OUTFLOWS/FINANCING/TOTALES/FCF)
YEAR_COL_WIDTH    = 100         # ancho de cada columna de año y SUBTOTAL en px (mismas tablas)

METRICS_TABLE_WIDTH = "48%"     # ancho de la tabla de métricas (acepta "%" o "px", ej. "600px")

st.markdown("""
<style>
div[data-testid="stDataFrame"],
div[data-testid="stDataFrame"] > div,
.stDataFrameGlideDataEditor {
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def _download_xlsx():
    FILE_ID = st.secrets["FILE_ID"]
    r = requests.get(f"https://docs.google.com/spreadsheets/d/{FILE_ID}/export?format=xlsx")
    return r.content

@st.cache_data
def get_projects():
    wb = openpyxl.load_workbook(io.BytesIO(_download_xlsx()), read_only=True)
    return [s for s in wb.sheetnames if s not in ("INSTRUCCIONES", "PLANTILLA")]

@st.cache_data
def load_defaults(project_name: str):
    wb = openpyxl.load_workbook(io.BytesIO(_download_xlsx()), data_only=True)
    ws = wb[project_name]

    header = next(ws.iter_rows(min_row=2, max_row=2, values_only=True))
    years = []
    for v in header[2:]:
        try:
            y = int(v)
            if 1900 < y < 2200:
                years.append(y)
        except (TypeError, ValueError):
            pass
    years = years[:10]  # limitar a un horizonte de 10 años
    n = len(years)

    KNOWN = {"INFLOWS", "OUTFLOWS", "FINANCING"}
    sections = {"INFLOWS": [], "OUTFLOWS": [], "FINANCING": []}
    current = None

    def _f(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0

    for row in ws.iter_rows(min_row=3, max_row=39, values_only=True):
        sec     = str(row[0]).strip() if row[0] else ""
        concept = str(row[1]).strip() if row[1] else ""

        if sec in KNOWN:
            current = sec
            if concept:
                vals = [_f(v) for v in row[2:2 + n]]
                sections[current].append((concept, vals))
            continue

        if current and concept:
            vals = [_f(v) for v in row[2:2 + n]]
            sections[current].append((concept, vals))

    DEFAULTS = {
        "INFLOWS":   ["Rent", "Sales"],
        "OUTFLOWS":  ["CAPEX", "OPEX", "Rent Comm", "Sales Comm"],
        "FINANCING": ["Debt Draw", "Debt Repay"],
    }

    for sec, default_concepts in DEFAULTS.items():
        loaded = {r[0]: r[1] for r in sections[sec]}
        ordered = []
        for c in default_concepts:
            ordered.append((c, loaded.get(c, [0.0] * n)))
        for c, v in sections[sec]:
            if c not in default_concepts:
                ordered.append((c, v))
        sections[sec] = ordered

    # Leer métricas desde fila 40 en adelante (col A = label, col B = valor)
    metrics = []
    reading = False
    for row in ws.iter_rows(min_row=40, max_col=2, values_only=True):
        a, b = row[0], row[1]
        if str(a).strip().lower() == "description":
            reading = True
            continue
        if reading and a and b is not None:
            try:
                metrics.append((str(a).strip(), float(b)))
            except (TypeError, ValueError):
                pass

    return sections, years, metrics

def fmt_usd(v):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "—"
    return f"(${abs(v):,.0f})" if v < 0 else f"${v:,.0f}"

def _pdf_safe(s):
    # Helvetica (fuente core del PDF) solo soporta Latin-1; cualquier
    # carácter fuera de ese rango (tipografía "inteligente" pegada desde
    # Word/Excel, emojis, etc.) hace que fpdf lance una excepción y la
    # descarga falle en silencio. Lo sustituimos en vez de reventar.
    return str(s).encode("latin-1", "replace").decode("latin-1")

# Sub-group visual grouping (purely display — data structure unchanged)
CONCEPT_SUBGROUP = {
    "Rent":       "REVENUE",
    "Sales":      "REVENUE",
    "CAPEX":      "COSTS & EXPENSES",
    "OPEX":       "COSTS & EXPENSES",
    "Rent Comm":  "COMMISSIONS",
    "Sales Comm": "COMMISSIONS",
}
SEC_SUBGROUPS = {
    "INFLOWS":   ["REVENUE"],
    "OUTFLOWS":  ["COSTS & EXPENSES", "COMMISSIONS", "TAXES"],
    "FINANCING": ["FCF FROM FINANCING"],
}
SEC_DEFAULT_SG = {
    "INFLOWS":   "REVENUE",
    "OUTFLOWS":  "TAXES",
    "FINANCING": "FCF FROM FINANCING",
}
