def exportar_df_colorido_para_latex(df, caminho_arquivo, idx_vcu_work, idx_vcu):
    """
    Exporta um DataFrame para LaTeX com:
    - primeira coluna como inteiro
    - demais colunas com 4 casas decimais
    - linha idx_vcu_work em vermelho
    - linha idx_vcu em amarelo
    - linha idx_vcu - 1 em azul
    """
    
    def cor_latex(i, x, col_idx):
        if col_idx == 0:
            valor = str(int(x))
        else:
            valor = f"{float(x):.4f}"
        
        if i == idx_vcu_work:
            return r'\textcolor{red}{' + valor + '}'
        elif i == idx_vcu:
            return r'\textcolor{yellow!50!black}{' + valor + '}'
        elif i == idx_vcu - 2:
            return r'\textcolor{blue}{' + valor + '}'
        else:
            return valor

    linhas_latex = [r"\begin{tabular}{%s}" % ("c" * len(df.columns))]
    linhas_latex.append(r"\toprule")
    linhas_latex.append(" & ".join(df.columns) + r" \\")
    linhas_latex.append(r"\midrule")

    for i, row in df.iterrows():
        linha_formatada = [cor_latex(i, val, j) for j, val in enumerate(row)]
        linhas_latex.append(" & ".join(linha_formatada) + r" \\")

    linhas_latex.append(r"\bottomrule")
    linhas_latex.append(r"\end{tabular}")

    latex_final = "\n".join(linhas_latex)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(latex_final)


#####################################################################################################
import pandas as pd

def exportar_dicionario_para_tabular(dicionario,
                                     selected_option,
                                     caminho_arquivo_tex):
    """
    Transforma um dicionário em DataFrame e exporta para LaTeX dentro de um ambiente tabular,
    com nomes de parâmetros mapeados e valores formatados conforme especificações.
    """

    # Se for com fusíveis internos
    match selected_option:
        case "Fusíveis Internos Estrela Dupla":
            mapeamento_keys = {
                "f1": "Frequência (Hz)",
                "power_bank_rated": "Potência Nominal (MVAr)",
                "voltage_bank_rated": "Tensão Nominal (kV)",
                "power_bank_work": "Potência de Trabalho (MVAr)",
                "voltage_bank_work": "Tensão de Trabalho (kV)",
                "S":  "S  - Unidades em Série",
                "Pt": "Pt - Unidades em Paralelo (total)",
                "Pa": "Pa - Unidades em Paralelo da Fase Afetada",
                "P":  "P  - Unidades em Paralelao na String Afetada",
                "G":  "G  - Aterramento (0) / Isolamento (1)",
                "N":  "N  - Elementos em Paralelo das Unidades",
                "Su": "Su - Elementos em Série das Unidades"
            }

            # Formatação dos valores
            valores_formatados = {}
            for chave, valor in dicionario.items():
                if chave in {"Su", "N", "G", "P", "Pa", "Pt", "S"}:
                    valor_formatado = f"{int(round(valor))}"
                elif chave == "f1":
                    valor_formatado = f"{round(valor, 1)}"
                elif chave in {"power_bank_rated", "power_bank_work"}:
                    valor_formatado = f"{round(valor / 1e6, 1)}"
                elif chave in {"voltage_bank_rated", "voltage_bank_work"}:
                    valor_formatado = f"{round(valor / 1e3, 1)}"
                else:
                    valor_formatado = str(valor)
                nome_exibicao = mapeamento_keys.get(chave, chave)
                valores_formatados[nome_exibicao] = valor_formatado

            df = pd.DataFrame(list(valores_formatados.items()), columns=["Parâmetro", "Valor"])
            # Construir conteúdo LaTeX com ambiente tabular
            linhas = [
                r"\begin{tabular}{|l|r|}",
                r"\hline",
                r"\textbf{Parâmetro} & \textbf{Valor} \\ \hline"
            ]

            for _, linha in df.iterrows():
                linhas.append(f"{linha['Parâmetro']} & {linha['Valor']} \\\\  \\hline")

            linhas.append(r"\end{tabular}")

            # Salvar no .tex
            with open(caminho_arquivo_tex, "w", encoding="utf-8") as f:
                f.write("\n".join(linhas))

        case "Fusíveis Externos Estrela Dupla":
            mapeamento_keys = {
                "f1": "Frequência (Hz)",
                "power_bank_rated": "Potência Nominal (MVAr)",
                "voltage_bank_rated": "Tensão Nominal (kV)",
                "power_bank_work": "Potência de Trabalho (MVAr)",
                "voltage_bank_work": "Tensão de Trabalho (kV)",
                "S": "S  - Unidades em Série",
                "Pt": "Pt - Unidades em Paralelo (total)",
                "Pa": "Pa - Unidades em Paralelo da Fase Afetada",
                "G": "G  - Aterramento (0) / Isolamento (1)",
            }

            # Formatação dos valores
            valores_formatados = {}
            for chave, valor in dicionario.items():
                if chave in {"G", "Pa", "Pt", "S"}:
                    valor_formatado = f"{int(round(valor))}"
                elif chave == "f1":
                    valor_formatado = f"{round(valor, 1)}"
                elif chave in {"power_bank_rated", "power_bank_work"}:
                    valor_formatado = f"{round(valor / 1e6, 1)}"
                elif chave in {"voltage_bank_rated", "voltage_bank_work"}:
                    valor_formatado = f"{round(valor / 1e3, 1)}"
                else:
                    valor_formatado = str(valor)

                nome_exibicao = mapeamento_keys.get(chave, chave)
                valores_formatados[nome_exibicao] = valor_formatado

            df = pd.DataFrame(list(valores_formatados.items()), columns=["Parâmetro", "Valor"])
            # Construir conteúdo LaTeX com ambiente tabular
            linhas = [
                r"\begin{tabular}{|l|r|}",
                r"\hline",
                r"\textbf{Parâmetro} & \textbf{Valor} \\ \hline"
            ]

            for _, linha in df.iterrows():
                linhas.append(f"{linha['Parâmetro']} & {linha['Valor']} \\\\  \\hline")

            linhas.append(r"\end{tabular}")

            # Salvar no .tex
            with open(caminho_arquivo_tex, "w", encoding="utf-8") as f:
                f.write("\n".join(linhas))







#####################################################################################################
import os
import subprocess
import shutil

def gerar_pdf_com_variaveis(dicionario,
                            caminho_template_tex = r'tex_files/TEMPLATE_Relatorio_Inrush_DAX_pt.tex',
                            nome_base_novo = "erro",
                            pasta_saida_pdf = r''):

    # f1 = dicionario["f1"]
    # power_bank_rated = dicionario["power_bank_rated"]
    # voltage_bank_rated = dicionario["voltage_bank_rated"]
    # voltage_bank_work = dicionario["voltage_bank_work"]
    # S = dicionario["S"]
    # Pt = dicionario["Pt"]
    # Pa = dicionario["Pa"]
    # G = dicionario["G"]

     # Read the template
    with open(caminho_template_tex, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Replace variables
    # conteudo = conteudo.replace('{{NNN}}', str(N))
    # conteudo = conteudo.replace('{{SuSuSu}}', str(Su))

    # Work directory and new filenames
    pasta_trabalho    = os.path.dirname(caminho_template_tex)
    caminho_tex_novo  = os.path.join(pasta_trabalho, nome_base_novo+".tex")

    # Save the new .tex
    with open(caminho_tex_novo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    # Ensure the .bib is in the same folder (adjust name if necessário)
    bib_origem = os.path.abspath("bibliografia.bib")
    bib_dest   = os.path.join(pasta_trabalho, "bibliografia.bib")
    if os.path.exists(bib_origem) and not os.path.exists(bib_dest):
        shutil.copy(bib_origem, bib_dest)

    try:
        # Run latexmk to handle XeLaTeX + Biber + passes extras
        result = subprocess.run(
            ["latexmk", "-xelatex", "-interaction=nonstopmode", nome_base_novo],
            cwd=pasta_trabalho,
            capture_output=True, text=True
        )
        import streamlit as st
        st.write(result.stdout, result.stderr)
        # ["latexmk", "-xelatex", "-use-biber", "-interaction=nonstopmode", nome_tex_novo]
        # ["latexmk", "-pdfxe", "-use-biber", "-interaction=nonstopmode", nome_tex_novo]
        # Move the final PDF out, if solicitado
        pdf_gerado = os.path.join(pasta_trabalho, f"{nome_base_novo}.pdf")
        if pasta_saida_pdf:
            os.makedirs(pasta_saida_pdf, exist_ok=True)
            destino = os.path.join(pasta_saida_pdf, f"{nome_base_novo}.pdf")
            shutil.move(pdf_gerado, destino)
            st.write("========================================")
            st.write("========================================")
            st.write("========================================")
            st.write(f"✅ PDF moved to: {destino}")
        else:
            st.write("========================================")
            st.write("========================================")
            st.write("========================================")
            st.write(f"✅ PDF generated at: {pdf_gerado}")

        # Clean up auxiliary files (optional)
        subprocess.run(
            ["latexmk", "-c", nome_base_novo],
            cwd=pasta_trabalho
        )

    except subprocess.CalledProcessError as e:
        print(f"❌ Error during LaTeX build: {e}")

