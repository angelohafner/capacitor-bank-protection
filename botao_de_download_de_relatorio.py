import os
import streamlit as st
from exportar_para_latex import gerar_pdf_com_variaveis


def gerar_pdf_interface(
        inputs: dict,
        template_path: str = os.path.join("tex_files", "TEMPLATE_Relatorio_Inrush_DAX_pt.tex"),
        output_dir: str = "tex_files",
        nome_base_novo: str = "erro",
):
    """Render a Streamlit button to generate and download the LaTeX PDF."""
    # Build the expected PDF path
    caminho_pdf = os.path.join(output_dir, nome_base_novo+".pdf")

    # Render button
    if st.button("Gerar PDF"):
        # Show spinner while generating
        with st.spinner("Gerando PDF, por favor aguarde..."):
            gerar_pdf_com_variaveis(
                inputs,
                caminho_template_tex=template_path,
                nome_base_novo = nome_base_novo,
                pasta_saida_pdf=output_dir
            )

        # Check if file was created
        if os.path.exists(caminho_pdf):
            st.success("✅ PDF gerado com sucesso!")
            # Read bytes and create download button
            with open(caminho_pdf, "rb") as f:
                pdf_bytes = f.read()
            st.download_button(
                label="📥 Baixar PDF",
                data=pdf_bytes,
                file_name=nome_base_novo+".pdf",
                mime="application/pdf"
            )
        else:
            st.error("❌ Erro: o arquivo PDF não foi encontrado.")
