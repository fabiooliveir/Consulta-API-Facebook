## Consultas na API do Facebook

Este projeto apresenta exemplos de consultas na API do Facebook utilizando Python. Cada arquivo neste repositório representa um tipo de consulta diferente. Abaixo estão os detalhes de cada consulta:

### Consulta de Estatísticas de Anúncios

O arquivo `get_ads_insights.py` demonstra como realizar uma consulta para obter estatísticas de anúncios, como impressões, gastos e ações. Para executar este arquivo, é necessário configurar as variáveis de ambiente no arquivo `.env` com as credenciais necessárias (ACCESS_TOKEN, AD_ACCOUNT_ID, APP_SECRET, APP_ID).

### Consulta de Dados de Leads

O arquivo `get_lead_data.py` mostra como fazer uma consulta para obter dados de leads de formulários do Facebook. Este arquivo utiliza a função `get_access_token()` para obter o token de acesso necessário e, em seguida, faz uma chamada à API para obter os dados de leads. Os dados são então extraídos e exibidos em um DataFrame do Pandas.

Para executar qualquer um dos arquivos, é necessário instalar as dependências listadas no arquivo `requirements.txt` e configurar as variáveis de ambiente no arquivo `.env`.