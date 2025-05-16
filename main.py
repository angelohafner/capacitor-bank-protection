import streamlit as st
from exportar_para_latex import exportar_dicionario_para_tabular
from desenho_dos_capacitores_classe import CapacitoresY
import matplotlib.pyplot as plt
import os
import pandas as pd

from botao_de_download_de_relatorio import gerar_pdf_interface

from documento_mestre import (master_internal_fuses, 
                              master_external_fused_double_y, 
                              master_external_fused_single_y,
                              master_internal_fuses_bridge_h)

from input_widgets import (get_capacitor_bank_inputs_for_internal_fused,
                           get_capacitor_bank_inputs_for_external_fused_double_y,
                           get_capacitor_bank_inputs_for_external_fused_single_y,
                           get_capacitor_bank_inputs_for_internal_fused_bridge_h)

st.set_page_config(
    page_title="Desbalanceamento - Banco de Capacitores",
    page_icon="⏸",  # Você pode trocar por outro emoji ou um arquivo .ico/.png
    layout="centered"
)

st.markdown(
    "# Desbalanceamento para um banco de capacitores "
    "[IEEE C37.99](https://standards.ieee.org/ieee/C37.99/5511/)"
)
options = ["Fusíveis Internos Estrela Dupla",
           "Fusíveis Externos Estrela Dupla",
           "Fusíveis Externos Estrela Simples",
           "Fusíveis Internos Ponte H"]
selected_option = st.selectbox("Tipo do Arranjo:", options)
# selected_option = "Fusíveis Internos"

match selected_option:
    case "Fusíveis Internos Estrela Dupla":
        st.image("tex_files/Figure 34 Illustration of an uneven double wye connected bank.png")
        inputs = get_capacitor_bank_inputs_for_internal_fused(selected_option=selected_option)
        exportar_dicionario_para_tabular(dicionario=inputs,
                                         selected_option=selected_option,
                                         caminho_arquivo_tex="tex_files/tabela_parametros_tabular_fusiveis_internos.tex")
        (df_stylized,
         idx_mais_proximo_vcu,  
         idx_mais_proximo_vcu_work) = master_internal_fuses(inputs)
        st.dataframe(data=df_stylized, hide_index=True)
        gerar_pdf_interface(inputs = inputs,
                            template_path = "tex_files/TEMPLATE_Relatorio_Inrush_DAX_FI.tex",
                            nome_base_novo = "banco_capacitores_fusiveis_internos"
                            )

        # fig = CapacitoresY.generate_and_save_capacitor_plot(m=inputs['S'], n=inputs['Pa'], d=2.0, horizontal_spacing=5)
        # st.pyplot(fig)
        


    case "Fusíveis Externos Estrela Dupla":
        st.image("tex_files/Figure 29 Illustration of a double wye-connected capacitor bank.png")
        inputs = get_capacitor_bank_inputs_for_external_fused_double_y(selected_option)
        exportar_dicionario_para_tabular(dicionario=inputs,
                                         selected_option=selected_option,
                                         caminho_arquivo_tex="tex_files/tabela_parametros_tabular_fusiveis_externos-yy.tex")
        (df_stylized, 
         idx_mais_proximo_vcu,  
         idx_mais_proximo_vcu_work) = master_external_fused_double_y(inputs)
        st.dataframe(data=df_stylized, hide_index=True)
        gerar_pdf_interface(inputs = inputs,
                            template_path = "tex_files/TEMPLATE_Relatorio_Inrush_DAX_FE-YY.tex",
                            nome_base_novo="banco_capacitores_fusiveis_externos_yy")

    case "Fusíveis Externos Estrela Simples":
        st.image("tex_files/Figure 28 Illustration of a single wye-connected capacitor bank.png")
        inputs = get_capacitor_bank_inputs_for_external_fused_single_y()
        (df_stylized, 
         idx_mais_proximo_vcu,  
         idx_mais_proximo_vcu_work) = master_external_fused_single_y(**inputs)
        st.dataframe(data=df_stylized, hide_index=True)

    case "Fusíveis Internos Ponte H":
        st.image("tex_files/Figure 36 Illustration of one leg of an H-bridge capacitor bank.png")
        inputs = get_capacitor_bank_inputs_for_internal_fused_bridge_h()
        (df_stylized, 
         idx_mais_proximo_vcu,  
         idx_mais_proximo_vcu_work) = master_internal_fuses_bridge_h(**inputs)
        st.dataframe(data=df_stylized, hide_index=True)


# df_stylized.to_excel(f"capacitor_bank_{selected_option}.xlsx")


