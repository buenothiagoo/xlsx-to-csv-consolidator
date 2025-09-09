# xlsx-to-csv-consolidator

Um script simples em Python para automatizar a consolidação de múltiplos arquivos `.xlsx` localizados em diferentes pastas em um único arquivo `.csv`.

## Como Funciona

Este projeto é uma solução prática para um desafio comum: unificar dados que estão distribuídos em vários diretórios. O script percorre uma lista de pastas, processa cada arquivo Excel (.xlsx) encontrado e consolida os dados em um único DataFrame. Além disso, ele adiciona uma nova coluna no arquivo final, identificando a pasta de origem de cada linha de dados.

O resultado final é um arquivo `.csv` limpo e consolidado, pronto para ser usado em análises, dashboards ou relatórios.

## Destaques

* **Consolidação de dados:** Processa múltiplos arquivos `.xlsx` de diferentes pastas.
* **Identificação da origem:** Adiciona automaticamente o nome da pasta de origem como uma nova coluna.
* **Fácil de configurar:** As pastas de entrada e saída podem ser facilmente ajustadas no código.
* **Pronto para análise:** O arquivo de saída é formatado em `.csv`, um formato amplamente utilizado para análise de dados.

## Requisitos

Para rodar este script, você precisa ter o Python instalado e as seguintes bibliotecas:

* `pandas`
* `os`
* `re`

Você pode instalá-las usando `pip`:
```bash
pip install pandas openpyxl
```
*(openpyxl é necessário para ler arquivos .xlsx)*

## Estrutura de pastas

Para que o script funcione corretamente, organize seus arquivos da seguinte forma:

```
├──  consolidator.py
├──  dados_entrada/
│    ├──  pasta_1/
│    │    ├── arquivo1.xlsx
│    │    └── arquivo2.xlsx
│    └──  pasta_2/
│         ├── arquivo3.xlsx
│         └── arquivo4.xlsx
└──  dados_saida/
```

## Como usar

1. Clone este repositório ou faça o download do `consolidator.py`.
2. Ajuste os caminhos: Edite as variáveis `pastas_a_processar`, `caminho_base_entrada`, `caminho_base_saida` e `nome_arquivo_saida` no final do script (`if __name__ == "__main__":`).
3. Execute o script a partir do terminal:
```bash
python seu_script.py
```
4. O arquivo `.csv` consolidado será salvo na pasta `dados_saida`.
