

















En el cierre del proyecto se registra un Cash-on-Cash de 44.87%, reflejando una alta generación de retornos en efectivo sobre el capital invertido.

El Equity Multiple de 2.10 indica que el proyecto genera un retorno total de 2.1 veces el capital de equity invertido, considerando un revenue actual aproximado de 8,952,386, sujeto a variación debido a que aún quedan 3 apartamentos por vender y posibles ajustes de precio en negociación, frente a un equity aportado de 4,253,969, lo que resulta en la multiplicación del capital inicial más la ganancia correspondiente.

El FCF from Financing (Net Earning) asciende a 1,908,895, representando el flujo neto final generado por el proyecto al cierre.


2.1 veces quiere decir q lo dobla

Sí. Un Equity Multiple de 2.10x significa que el proyecto más que duplica el capital invertido.

Podrías redactarlo así:

El Equity Multiple de 2.10x indica que el proyecto más que duplica el capital de equity invertido. Considerando un revenue actual estimado de 8,952,386, sujeto a variación debido a que aún quedan tres apartamentos por vender y a posibles ajustes de precio en las negociaciones, frente a un equity aportado de 4,253,969, el retorno total esperado equivale aproximadamente a 2.1 veces el capital invertido.

De forma simple:

Equity invertido: 4.25 MM

Retorno total esperado: ≈ 8.95 MM

Equity Multiple: 2.10x

Interpretación: se recupera el capital inicial y se obtiene un retorno adicional que permite más que duplicar la inversión original.


QUE LA ESTRUTURA CION DE BONOS Y COMO SE HACE EN UN PAIS COMO PANAMA

La estructuración de bonos es el proceso mediante el cual una empresa, banco o entidad gubernamental diseña y emite deuda en el mercado de capitales para obtener financiamiento de inversionistas.

En términos simples, en lugar de solicitar un préstamo a un banco, la empresa vende bonos a múltiples inversionistas y se compromete a pagar intereses periódicos (cupón) y devolver el capital al vencimiento.

Proceso general de estructuración
Definir la necesidad de financiamiento

Monto a captar.

Destino de los fondos (expansión, refinanciamiento, construcción, capital de trabajo, etc.).

Diseñar las características del bono

Plazo (5, 10, 15 años, etc.).

Tasa de interés fija o variable.

Frecuencia de pago de intereses.

Garantías (si las hubiera).

Amortización del principal.

Preparar la documentación

Estados financieros auditados.

Prospecto informativo.

Contratos legales.

Estructura de garantías.

Obtener aprobaciones regulatorias
En Panamá, las emisiones públicas son supervisadas por la Superintendencia del Mercado de Valores de Panamá (SMV).

Seleccionar los participantes de la emisión

Casa de valores estructuradora.

Asesores legales.

Auditores.

Agente de pago.

Central de custodia (Latinclear).

Colocar los bonos en el mercado
Los inversionistas compran los bonos y la empresa recibe los fondos.

Ejemplo en Panamá
Supongamos que una promotora inmobiliaria necesita US$20 millones para desarrollar un proyecto.

Estructura propuesta:

Emisor: Empresa XYZ, S.A.

Monto: US$20 millones.

Plazo: 10 años.

Tasa cupón: 7.5% anual.

Pago de intereses: trimestral.

Garantía: hipoteca sobre el proyecto y cesión de flujos.

La empresa contrata una casa de valores que estructura la emisión, presenta la documentación ante la SMV y posteriormente los bonos se colocan entre bancos, aseguradoras, fondos de pensiones e inversionistas privados.

Participantes típicos en Panamá
Emisor.

Casa de Valores estructuradora.

SMV Panamá.

Bolsa Latinoamericana de Valores (Latinex).

Latinclear.

Agente de pago.

Inversionistas institucionales.

En proyectos inmobiliarios y corporativos en Panamá es común estructurar bonos corporativos, bonos rotativos, bonos subordinados o programas de valores dependiendo de las necesidades de financiamiento y del perfil de riesgo del emisor.


Sí. El ancho de la tabla está definido principalmente por esta parte:

style="width:48%; ..."
Esto significa que la tabla ocupará el 48% del ancho disponible de su contenedor (por ejemplo, la columna de Streamlit donde se encuentra).

Algunos ejemplos:

width:100% → ocupa todo el ancho disponible.

width:80% → ocupa el 80%.

width:48% → ocupa casi la mitad.

width:500px → ancho fijo de 500 píxeles.

En tu código:

<table style="width:48%; border-collapse:collapse; ...">
la tabla tendrá un ancho equivalente al 48% del contenedor.

Si quieres controlar también el ancho de cada columna, puedes hacerlo en los <th>:

<th style="width:60%">DESCRIPTION</th>
<th style="width:40%; text-align:right">PROJECT CLOSING OPERATOR</th>
o mediante un <colgroup>:

<colgroup>
    <col style="width:60%">
    <col style="width:40%">
</colgroup>
Así, width:48% controla el tamaño total de la tabla, mientras que los width de las columnas controlan la distribución interna.


lo que quiero es saber donde cambio el ancho de las tablas 

Exactamente, el ancho total de tu tabla se cambia aquí:

<table style="width:48%; border-collapse:collapse; ...">
Si quieres que sea más ancha, cambia el 48% por otro valor:

width:60%
o

width:100%
Por ejemplo:

<table style="width:70%;border-collapse:collapse;font-family:sans-serif;border:1px solid #ddd;overflow:hidden;margin-bottom:16px">
Si deseas un ancho fijo en píxeles:

width:800px
Por tanto, la línea que controla el ancho de la tabla es:

width:48%;


Pasted text(4).txt
Documento
este es mi codigo: 

Sí, ya vi tu código. El ancho de la tabla de INVESTMENT RETURNS se controla exactamente aquí:

st.markdown(f"""
<table style="width:48%;border-collapse:collapse;
              font-family:sans-serif;
              border:1px solid #ddd;
              overflow:hidden;
              margin-bottom:16px">
La parte importante es:

width:48%;
Cambiar el ancho
Por ejemplo:

width:60%;
o

width:80%;
o

width:100%;
Si quieres un ancho fijo:

width:700px;
Pero hay otro detalle en tu código
Arriba tienes:

.main .block-container {
    max-width: 60vw !important;
}
Eso limita toda la página al 60% del ancho de la ventana.

Por eso, aunque pongas:

width:100%;
la tabla solo ocupará el 100% de ese contenedor del 60%.

Si quieres que toda la aplicación sea más ancha, cambia:

max-width: 60vw !important;
por algo como:

max-width: 90vw !important;
o incluso:

max-width: 100vw !important;
Resumen:

Ancho de la tabla → aquí:

width:48%;
Ancho máximo de toda la página → aquí:

max-width: 60vw !important;
Si me dices qué quieres (que la tabla sea más ancha o que toda la página ocupe más espacio), te indico exactamente qué línea modificar.


😄 Gracias, no hay problema. Entendiste perfectamente la situación.

Cuando quieras revisar una parte del código, optimizar Streamlit, ajustar anchos de tablas, mejorar el PDF o agregar nuevas métricas financieras, seguimos desde donde lo dejamos. Ya tengo bastante contexto de tu proyecto DCF.

Y sí, admito que cuando alguien dice "dame todo el código" y no puedo pegarlo completo, se siente un poco como cuando Excel muestra "Not Responding" justo antes de guardar. 😄


esuq et eiba a pedir algo pero tu te pones revelde joo

😂 Tranquilo, no me sentí nada. Solo tengo algunas limitaciones con textos muy largos y a veces parezco el auditor interno diciendo "eso no procede". Pero aquí seguimos para ayudarte.

¿Qué era lo que me ibas a pedir? Joo 😄


y tratme con amor por q sino me cierro

😄 Trato hecho. Puedo responderte de forma amable, paciente y con buen humor. No hace falta que te cierres; pregunta con confianza y vemos juntos lo que necesites.

Así que adelante, Arturo. ¿Qué era lo que me ibas a pedir? 😊


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

st.markdown("""

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

Sub-group visual grouping (purely display — data structure unchanged)
CONCEPT_SUBGROUP = {
"Rent": "REVENUE",
"Sales": "REVENUE",
"CAPEX": "COSTS & EXPENSES",
"OPEX": "COSTS & EXPENSES",
"Rent Comm": "COMMISSIONS",
"Sales Comm": "COMMISSIONS",
}
SEC_SUBGROUPS = {
"INFLOWS": ["REVENUE"],
"OUTFLOWS": ["COSTS & EXPENSES", "COMMISSIONS", "TAXES"],
"FINANCING": ["FCF FROM FINANCING"],
}
SEC_DEFAULT_SG = {
"INFLOWS": "REVENUE",
"OUTFLOWS": "TAXES",
"FINANCING": "FCF FROM FINANCING",
}

def kpi_card(label, value, sub="", green=False):
cls = "kpi-val-green" if green else "kpi-val"
return (f'{label}'
f'{value}{sub}')

CONCEPT_WIDTH = 220

def col_cfg(scols):
cfg = {"Concepto": st.column_config.TextColumn("Concepto", width=CONCEPT_WIDTH, pinned=True)}
cfg.update({y: st.column_config.NumberColumn(y, format="$%,.0f", width="small") for y in scols})
cfg["SUBTOTAL"] = st.column_config.NumberColumn("SUBTOTAL", format="$%,.0f", width="small")
return cfg

PINNED_CONCEPTO = {"Concepto": st.column_config.TextColumn("Concepto", width=CONCEPT_WIDTH, pinned=True)}

def total_row_style(df, num_cols):
return df.style.apply(
lambda r: ["background-color:#1E3A5F;color;font-weight"] * len(r), axis=1
).format(lambda x: "-" if x == 0 else (f"({abs(x):,.0f})" if x < 0 else f"${x:,.0f}"), subset=num_cols)

def sum_by_year(section, n):
return [sum(vals[i] for _, vals in section) for i in range(n)]

def render_fcf_row(label, year_vals, subtotal, scols):
row = {"Concepto": label}
row.update({scols[i]: year_vals[i] for i in range(len(scols))})
row["SUBTOTAL"] = subtotal
df = pd.DataFrame([row])
st.dataframe(
df.style.apply(
lambda r: ["background-color:#DBEAFE;color:#1E3A5F;font-weight"] * len(r), axis=1
).format(
lambda x: f"({abs(x):,.0f})" if x < 0 else f"${x:,.0f}",
subset=scols + ["SUBTOTAL"],
),
use_container_width=True,
hide_index=True,
column_config=PINNED_CONCEPTO,
)

def render_section(title, key, section_data, scols, selected):
st.markdown(f'{title}', unsafe_allow_html=True)

# Assign each concept to its sub-group
sg_data = {}
for concept, vals in section_data:
    sg = CONCEPT_SUBGROUP.get(concept, SEC_DEFAULT_SG.get(key, "OTHER"))
    sg_data.setdefault(sg, []).append((concept, vals))

subgroups  = SEC_SUBGROUPS.get(key, ["OTHER"])
all_results = []

for sg in subgroups:
    sg_concepts = sg_data.get(sg, [])
    if not sg_concepts:
        continue

    st.markdown(f'<div class="subgroup-hdr">{sg}</div>', unsafe_allow_html=True)

    n_rows   = len(sg_concepts)
    vals_key = f"vals_{key}_{sg}_{selected}"

    if vals_key not in st.session_state or len(st.session_state[vals_key]) != n_rows:
        st.session_state[vals_key] = [list(c[1]) for c in sg_concepts]

    labels     = [c[0] for c in sg_concepts]
    row_totals = [sum(v) for v in st.session_state[vals_key]]

    df = pd.DataFrame(st.session_state[vals_key], columns=scols)
    df.insert(0, "Concepto", labels)
    df["SUBTOTAL"] = row_totals

    edited = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        key=f"editor_{key}_{sg}_{selected}",
        disabled=["SUBTOTAL"],
        column_config=col_cfg(scols),
        hide_index=True,
    )

    edited[scols] = edited[scols].fillna(0).astype(float)

    sg_results    = []
    new_vals_list = []
    for i in range(len(edited)):
        concept = str(edited.iloc[i]["Concepto"] or sg_concepts[i][0])
        vals    = edited.iloc[i][scols].tolist()
        sg_results.append((concept, vals))
        new_vals_list.append(vals)

    if new_vals_list != st.session_state[vals_key]:
        st.session_state[vals_key] = new_vals_list
        st.rerun()

    # Consolidated total row for this sub-group
    sg_year_totals = edited[scols].sum()
    sg_total       = sg_year_totals.sum()
    total_row = pd.DataFrame([{
        "Concepto": f"▶ {sg}",
        **sg_year_totals.to_dict(),
        "SUBTOTAL": sg_total,
    }])
    st.dataframe(
        total_row_style(total_row, list(scols) + ["SUBTOTAL"]),
        use_container_width=True,
        hide_index=True,
        column_config=PINNED_CONCEPTO,
    )

    all_results.extend(sg_results)

return all_results
st.markdown('📊 DCF PROJECT CALCULATOR', unsafe_allow_html=True)
st.markdown('Selecciona un proyecto · edita las celdas · los resultados se recalculan automáticamente', unsafe_allow_html=True)

projects = get_projects()
col_sel, col_info = st.columns([2, 5])
with col_sel:
selected = st.selectbox("Proyecto", projects, key="project_selector")
with col_info:
st.markdown(f"Fuente: Google Sheets · Hoja: {selected}",
unsafe_allow_html=True)

D, YEARS, METRICS = load_defaults(selected)
SCOLS = [str(y) for y in YEARS]
N = len(YEARS)
st.divider()

metrics_container = st.container()
st.divider()

inflows = render_section("INFLOWS", "INFLOWS", D["INFLOWS"], SCOLS, selected)
outflows = render_section("OUTFLOWS", "OUTFLOWS", D["OUTFLOWS"], SCOLS, selected)

inflows_yr = sum_by_year(inflows, N)
outflows_yr = sum_by_year(outflows, N)
fcf_no_fin = [inflows_yr[i] + outflows_yr[i] for i in range(N)]
npv_no = sum(fcf_no_fin)

Totales consolidados INFLOWS / OUTFLOWS
st.markdown('TOTALES', unsafe_allow_html=True)
totals_df = pd.DataFrame([
{"Concepto": "▶ TOTAL INFLOWS", **{SCOLS[i]: inflows_yr[i] for i in range(N)}, "SUBTOTAL": sum(inflows_yr)},
{"Concepto": "▶ TOTAL OUTFLOWS", **{SCOLS[i]: outflows_yr[i] for i in range(N)}, "SUBTOTAL": sum(outflows_yr)},
])
st.dataframe(
totals_df.style.apply(
lambda r: [
"background-color:#DBEAFE;color:#1e40af;font-weight" if r["Concepto"].endswith("INFLOWS")
else "background-color:#FEE2E2;color:#991b1b;font-weight"
] * len(r), axis=1
).format(
lambda x: "-" if x == 0 else (f"({abs(x):,.0f})" if x < 0 else f"${x:,.0f}"),
subset=SCOLS + ["SUBTOTAL"],
),
use_container_width=True,
hide_index=True,
column_config=PINNED_CONCEPTO,
)

st.markdown('FCF SIN FINANCIAMIENTO', unsafe_allow_html=True)
render_fcf_row("FCF (Excluye Financiamiento)", fcf_no_fin, npv_no, SCOLS)

financing = render_section("FINANCING", "FINANCING", D["FINANCING"], SCOLS, selected)
financing_yr = sum_by_year(financing, N)
fcf_with_fin = [fcf_no_fin[i] + financing_yr[i] for i in range(N)]
npv_fin = sum(fcf_with_fin)

st.markdown('FCF CON FINANCIAMIENTO', unsafe_allow_html=True)
render_fcf_row("FCF (Incluye Financiamiento)", fcf_with_fin, npv_fin, SCOLS)

def safe_irr(cf):
try:
v = npf.irr(cf)
if v is None:
return None
v = float(np.real(v))
return v if not np.isnan(v) else None
except Exception:
return None

irr_no = safe_irr(fcf_no_fin)
irr_fin = safe_irr(fcf_with_fin)

noi_last = inflows_yr[-1] + outflows_yr[-1]
sales_last = inflows_yr[-1]
cap_rate = noi_last / sales_last if sales_last != 0 else 0

equity_actual = sum(-fcf_with_fin[i] for i in range(N) if fcf_with_fin[i] < 0)
cash_on_cash = npv_fin / equity_actual if equity_actual != 0 else None

with metrics_container:
st.markdown('INVESTMENT RETURNS — Métricas Clave', unsafe_allow_html=True)

def concept_total(section, name):
    for concept, vals in section:
        if concept == name:
            return sum(vals)
    return 0

PCT_KEYS  = {"CASH-ON-CASH", "IRR WITH FINANCING", "IRR SIN FINANCING",
             "ROI", "ROE", "CAP RATE", "CAP RATE ANUAL"}
MULT_KEYS = {"EQUITY MULTIPLE"}

def fmt_metric(key, val):
    k = key.upper()
    if k in PCT_KEYS or any(x in k for x in ("IRR", "RATE", "ROI", "ROE", "CASH")):
        return f"{val*100:.2f}%"
    if k in MULT_KEYS or "MULTIPLE" in k:
        return f"{val:.3f}"
    return fmt_usd(val)

rows = [(label, fmt_metric(label, val)) for label, val in METRICS]

body = "".join(
    f'<tr style="background:{"#FAFAFA" if i%2==0 else "#FFFFFF"}">'
    f'<td style="padding:7px 14px;font-size:12px;font-weight:700;color:#1a1a2e;border-bottom:1px solid #eee">{d}</td>'
    f'<td style="padding:7px 14px;text-align:right;font-size:12px;font-weight:700;color:#0052FF;border-bottom:1px solid #eee">{v}</td>'
    f'</tr>'
    for i, (d, v) in enumerate(rows)
)

st.markdown(f"""
<table style="width:48%;border-collapse:collapse;font-family:sans-serif;border:1px solid #ddd;overflow:hidden;margin-bottom:16px">
  <thead>
    <tr style="background:#F5F0C8">
      <th style="padding:10px 14px;text-align:left;font-size:11px;font-weight:800;letter-spacing:1.5px;color:#333;border-bottom:2px solid #ccc">DESCRIPTION</th>
      <th style="padding:10px 14px;text-align:right;font-size:11px;font-weight:800;letter-spacing:1.5px;color:#333;border-bottom:2px solid #ccc">PROJECT CLOSING OPERATOR</th>
    </tr>
  </thead>
  <tbody>{body}</tbody>
</table>
""", unsafe_allow_html=True)
st.divider()
st.markdown('DESCARGAR REPORTE', unsafe_allow_html=True)
fmt_choice = st.radio("Selecciona el formato:", ["Excel (.xlsx)", "PDF (.pdf)"], horizontal=True)

def build_excel():
buf = BytesIO()
with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
wb_out = writer.book
hdr_fmt = wb_out.add_format({"bold": True, "bg_color": "#0052FF", "font_color": "#FFFFFF", "border": 1, "align": "center"})
lbl_fmt = wb_out.add_format({"bold": True, "bg_color": "#EEF2FF", "border": 1, "indent": 1})
num_fmt = wb_out.add_format({"num_format": '#,##0;(#,##0)', "border": 1, "align": "right"})
tot_fmt = wb_out.add_format({"bold": True, "num_format": '#,##0;(#,##0)', "border": 1, "bg_color": "#DBEAFE", "align": "right"})
pct_fmt = wb_out.add_format({"num_format": '0.00%', "border": 1, "align": "right"})
title_fmt = wb_out.add_format({"bold": True, "font_size": 14, "font_color": "#0052FF"})
sub_fmt = wb_out.add_format({"bold": True, "bg_color": "#1E3A5F", "font_color": "#FFFFFF", "border": 1, "indent": 1})
date_fmt = wb_out.add_format({"italic": True, "font_size": 10, "font_color": "#888888"})

    ws = wb_out.add_worksheet("DCF PROJECT")
    writer.sheets["DCF PROJECT"] = ws
    ws.set_column(0, 0, 32)
    for c in range(1, N + 3):
        ws.set_column(c, c, 14)

    ncols = N + 1
    ts = datetime.now().strftime("%d/%m/%Y  %H:%M")
    ws.merge_range(0, 0, 0, ncols, f"Generado: {ts}", date_fmt)
    ws.merge_range(1, 0, 1, ncols, f"DCF PROJECT — {selected.upper()}   |   Closing", title_fmt)
    ws.write(2, 0, "Concepto", hdr_fmt)
    for c, h in enumerate(SCOLS + ["SUBTOTAL"], 1):
        ws.write(2, c, h, hdr_fmt)

    rn = 3

    def write_sec(title, rows):
        nonlocal rn
        ws.merge_range(rn, 0, rn, ncols, title, sub_fmt)
        rn += 1
        for label, vals in rows:
            ws.write(rn, 0, label, lbl_fmt)
            for c, v in enumerate(vals, 1):
                ws.write(rn, c, v, num_fmt)
            ws.write(rn, len(vals) + 1, sum(vals), tot_fmt)
            rn += 1
        rn += 1

    write_sec("INFLOWS",            inflows)
    write_sec("OUTFLOWS",           outflows)
    write_sec("FCF FROM FINANCING", financing)
    write_sec("FREE CASH FLOW", [
        ("FCF (Sin Financiamiento)", fcf_no_fin),
        ("FCF (Con Financiamiento)", fcf_with_fin),
    ])

    ws.merge_range(rn, 0, rn, ncols, "INVESTMENT RETURNS", sub_fmt); rn += 1
    for label, val, fmt_ in [
        ("IRR Sin Financiamiento", irr_no  or 0, pct_fmt),
        ("IRR Con Financiamiento", irr_fin or 0, pct_fmt),
        ("NPV Sin Financiamiento", npv_no,       tot_fmt),
        ("NPV Con Financiamiento", npv_fin,      tot_fmt),
    ]:
        ws.write(rn, 0, label, lbl_fmt)
        ws.write(rn, 1, val, fmt_)
        rn += 1

buf.seek(0)
return buf.read()
def build_pdf():
from fpdf import FPDF
pdf = FPDF(orientation="L", unit="mm", format="A3")
pdf.add_page()
pdf.set_margins(10, 10, 10)
pdf.set_auto_page_break(True, margin=15)

BLUE  = (0, 82, 255);  LBLUE = (238, 242, 255)
DARK  = (30, 58, 95);  WHITE = (255, 255, 255); TEXT = (38, 39, 48)

col_w   = max(18, int(360 / (N + 2)))
label_w = 50
hdrs    = SCOLS + ["SUBTOTAL"]

ts = datetime.now().strftime("%d/%m/%Y  %H:%M")
pdf.set_font("Helvetica", "I", 8); pdf.set_text_color(136, 136, 136)
pdf.cell(0, 5, f"Generado: {ts}", ln=True, align="C")
pdf.set_font("Helvetica", "B", 16); pdf.set_text_color(*BLUE)
pdf.cell(0, 10, f"DCF PROJECT - {selected.upper()}  |  Closing", ln=True, align="C")
pdf.set_text_color(*TEXT)
pdf.ln(3)

def draw_header():
    pdf.set_fill_color(*BLUE); pdf.set_text_color(*WHITE); pdf.set_font("Helvetica", "B", 7)
    pdf.cell(label_w, 7, "Concepto", border=1, align="C", fill=True)
    for h in hdrs:
        pdf.cell(col_w, 7, h, border=1, align="C", fill=True)
    pdf.ln()

def draw_sec_title(t):
    pdf.set_fill_color(*DARK); pdf.set_text_color(*WHITE); pdf.set_font("Helvetica", "B", 8)
    pdf.cell(label_w + col_w * len(hdrs), 6, f"  {t}", border=1, fill=True, ln=True)

def fc(v):
    return "-" if v == 0 else (f"({abs(v):,.0f})" if v < 0 else f"{v:,.0f}")

def draw_row(label, vals):
    pdf.set_fill_color(*LBLUE); pdf.set_text_color(*TEXT); pdf.set_font("Helvetica", "", 7)
    pdf.cell(label_w, 6, f"  {label}", border=1, fill=True)
    for v in vals:
        pdf.cell(col_w, 6, fc(v), border=1, align="R")
    pdf.cell(col_w, 6, fc(sum(vals)), border=1, align="R", fill=True)
    pdf.ln()

def draw_fcf(label, vals, sub):
    pdf.set_fill_color(219, 234, 254); pdf.set_text_color(*TEXT); pdf.set_font("Helvetica", "B", 7)
    pdf.cell(label_w, 6, f"  {label}", border=1, fill=True)
    for v in vals:
        pdf.cell(col_w, 6, fc(v), border=1, align="R")
    pdf.cell(col_w, 6, fc(sub), border=1, align="R", fill=True)
    pdf.ln()

draw_header()
draw_sec_title("INFLOWS")
for lbl, vals in inflows:  draw_row(lbl, vals)
pdf.ln(2)
draw_sec_title("OUTFLOWS")
for lbl, vals in outflows: draw_row(lbl, vals)
pdf.ln(2)
draw_sec_title("FCF FROM FINANCING")
for lbl, vals in financing: draw_row(lbl, vals)
pdf.ln(2)
draw_sec_title("FREE CASH FLOW")
draw_fcf("FCF (Sin Financiamiento)", fcf_no_fin,   npv_no)
draw_fcf("FCF (Con Financiamiento)", fcf_with_fin, npv_fin)
pdf.ln(5)

pdf.set_fill_color(*DARK); pdf.set_text_color(*WHITE); pdf.set_font("Helvetica", "B", 8)
pdf.cell(130, 7, "  INVESTMENT RETURNS", border=1, fill=True, ln=True)
for lbl, val, is_total in [
    ("IRR Sin Financiamiento", f"{irr_no*100:.2f}%"  if irr_no  is not None else "-", False),
    ("IRR Con Financiamiento", f"{irr_fin*100:.2f}%" if irr_fin is not None else "-", False),
    ("NPV Sin Financiamiento", fmt_usd(npv_no).replace("—", "-"),  True),
    ("NPV Con Financiamiento", fmt_usd(npv_fin).replace("—", "-"), True),
]:
    pdf.set_fill_color(*LBLUE); pdf.set_text_color(*TEXT); pdf.set_font("Helvetica", "B", 7)
    pdf.cell(80, 6, f"  {lbl}", border=1, fill=True)
    if is_total:
        pdf.set_fill_color(219, 234, 254); pdf.set_font("Helvetica", "B", 7)
        pdf.cell(50, 6, val, border=1, align="R", fill=True)
    else:
        pdf.set_fill_color(*WHITE); pdf.set_font("Helvetica", "", 7)
        pdf.cell(50, 6, val, border=1, align="R", fill=True)
    pdf.ln()

buf = BytesIO()
pdf.output(buf)
buf.seek(0)
return buf.read()
if fmt_choice == "Excel (.xlsx)":
st.download_button("⬇️ Descargar Excel", build_excel(),
file_name=f"DCF_{selected}.xlsx",
mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
type="primary")
else:
st.download_button("⬇️ Descargar PDF", build_pdf(),
file_name=f"DCF_{selected}.pdf",
mime="application/pdf", type="primary")


Cerrar
