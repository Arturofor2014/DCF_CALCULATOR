def render_section(title, key, section_data, scols, selected):
    st.markdown(f'<div class="section-hdr">{title}</div>', unsafe_allow_html=True)

    # 🔥 Labels
    labels = [r[0] for r in section_data]
    n_rows = len(labels)

    # 🔥 Construir matriz de valores de forma segura
    data_matrix = []
    for i in range(n_rows):
        data_matrix.append(section_data[i][1])

    df = pd.DataFrame(data_matrix, columns=scols)
    df.insert(0, "Concepto", labels)

    # 🔥 Editor
    edited = st.data_editor(
        df,
        use_container_width=True,
        num_rows="fixed",
        key=f"editor_{key}_{selected}",
        column_config=col_cfg(scols),
        hide_index=True,
    )

    # 🔥 Asegurar números
    edited[scols] = edited[scols].fillna(0).astype(float)

    # 🔥 reconstruir estructura original
    result = []
    for i in range(len(edited)):
        concept = edited.iloc[i]["Concepto"]
        vals = edited.iloc[i][scols].tolist()
        result.append((concept, vals))

    # 🔥 SUMAS REALES (CORRECTO)
    col_sums = edited[scols].sum()
    total_val = col_sums.sum()

    total_row = pd.DataFrame(
        [{
            "Concepto": f"▶ TOTAL {key}",
            **col_sums.to_dict(),
            "TOTAL": total_val
        }]
    )

    st.dataframe(
        total_row_style(total_row, scols + ["TOTAL"]),
        use_container_width=True,
        hide_index=True,
        column_config={"Concepto": st.column_config.TextColumn("Concepto", width=220)},
    )

    return result
