def render_section(title, key, section_data, scols, selected):
    st.markdown(f'<div class="section-hdr">{title}</div>', unsafe_allow_html=True)

    labels = [r[0] for r in section_data]

    # DataFrame base
    df = pd.DataFrame(
        {"Concepto": labels}
        | {y: [section_data[i][1][j] for i in range(len(section_data))] for j, y in enumerate(scols)}
    )

    edited = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        key=f"editor_{key}_{selected}",
        column_config=col_cfg(scols),
        hide_index=True,
    )

    # 🔥 Asegurar valores numéricos limpios
    edited[scols] = edited[scols].fillna(0).astype(float)

    # 🔥 Convertir a estructura usable
    result = []
    for i in range(len(edited)):
        concept = str(edited.at[i, "Concepto"] or f"Concepto {i+1}")
        vals = [float(edited.at[i, y] or 0) for y in scols]
        result.append((concept, vals))

    # 🔥 SUMAS POR COLUMNA (CORRECTO Y REACTIVO)
    col_sums = edited[scols].sum().to_dict()
    total_val = sum(col_sums.values())

    total_row = pd.DataFrame(
        {
            "Concepto": [f"▶ TOTAL {key}"],
            **{y: [col_sums[y]] for y in scols},
            "TOTAL": [total_val],
        }
    )

    st.dataframe(
        total_row_style(total_row, scols + ["TOTAL"]),
        use_container_width=True,
        hide_index=True,
        column_config={"Concepto": st.column_config.TextColumn("Concepto", width=220)},
    )

    return result
