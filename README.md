# Detecção de Anomalias em EEG com MNE e NeuroKit2

Este projeto realiza uma análise de sinais eletroencefalográficos (EEG) utilizando a base de dados CHB-MIT. A proposta é visualizar e identificar episódios de crise epiléptica, aplicar filtros nos sinais, e testar um modelo de classificação para detecção automática de anomalias.

## Estrutura do Projeto

O repositório contém os seguintes scripts:

- `analise_neurokit.py`: Aplica um filtro bandpass (0.5–40 Hz) no sinal EEG utilizando a biblioteca NeuroKit2 e plota a comparação entre o sinal original e o filtrado.
- `chb.py`: Realiza a anotação manual de um trecho de crise epiléptica e salva um gráfico com a visualização dos sinais durante a crise.
- `demo.py`: Similar ao `chb.py`, mas com outro paciente e outro episódio de crise.
- `eeg2.py`: Segmenta o EEG em janelas, extrai uma feature simples (média dos canais) e treina um modelo Random Forest para detecção de crise epiléptica.

## Requisitos

Instale as bibliotecas necessárias:

```bash
pip install mne neurokit2 matplotlib numpy pandas scikit-learn
```

## Estrutura de Pastas Recomendada

```bash
project/
│
├── data/
│   └── chb-mit-scalp-eeg-database-1.0.0/
│       └── chb01/
│           └── chb01_03.edf
│       └── chb05/
│           └── chb05_06.edf
│
├── imagens/
│   ├── eeg_canal_filtrado.png
│   ├── eeg_chbmit_30s.png
│   └── eeg_chbmit_seizure.png
│
├── analise_neurokit.py
├── chb.py
├── demo.py
├── eeg2.py
└── README.md
```

## Como Rodar

### Filtragem do Sinal EEG

```bash
python analise_neurokit.py
```

Gera a imagem `eeg_canal_filtrado.png` com comparação entre sinal original e filtrado.

### Visualização de Crises

```bash
python chb.py
```

Salva um gráfico com os canais selecionados durante uma crise epiléptica.

```bash
python demo.py
```

Executa visualização semelhante com outro paciente e episódio.

### Detecção Automática de Crises

```bash
python eeg2.py
```

Treina um modelo de Random Forest com janelas de 5 segundos e exibe um relatório de classificação.

## Base de Dados

Utiliza a base [CHB-MIT Scalp EEG Database](https://physionet.org/content/chbmit/1.0.0/), que contém sinais de EEG de pacientes pediátricos com epilepsia.

## Licença

Este projeto é de uso educacional e científico, respeitando os termos de uso da base CHB-MIT.
