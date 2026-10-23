# Radar Policial RMC & RMP — Pipeline de Coleta Automática

Este sistema automatiza o monitoramento, extração e filtragem contínua de notícias e documentos oficiais de polícia e investigações criminais nas **Regiões Metropolitanas de Campinas (20 municípios)** e **Piracicaba (24 municípios)**.

## Características do Sistema
- **Intervalo de Atualização:** Execução a cada 1 hora (configurável via `schedule` ou `crontab`).
- **Filtro Geográfico Restrito:** Rejeita qualquer notícia que não cite os municípios das regiões metropolitanas de Campinas ou Piracicaba.
- **Filtro Temático Rigoroso:** Detecta e valida termos de ocorrências policiais, inquéritos, investigações do GAECO, mandados judiciais, perícia técnica e boletins de ocorrência.
- **Fontes Híbridas:** Coleta notícias de veículos jornalísticos regionais e atos em diários oficiais e secretarias de segurança pública.

## Estrutura dos Arquivos
- `config.py`: Lista oficial das 44 cidades da RMC e RMP, palavras-chave de segurança pública e endpoints de feeds.
- `classifier.py`: Funções de processamento de linguagem natural (NLP/Regex) para validação geográfica e temática.
- `crawler.py`: Mecanismo de coleta, deduplicação por hash SHA-256 e gravação no banco de dados.
- `scheduler.py`: Serviço em segundo plano (daemon) para rodar a cada 60 minutos.
- `requirements.txt`: Bibliotecas necessárias.

## Como Executar em Produção
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie o agendador:
   ```bash
   python scheduler.py
   ```
   Ou configure uma linha no `crontab` do servidor Linux:
   ```bash
   0 * * * * cd /caminho/do/projeto && python crawler.py >> crawler.log 2>&1
   ```
