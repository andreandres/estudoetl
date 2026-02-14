🚀 Pipeline ETL com Python e Pandas
Este projeto é um estudo prático de Engenharia de Dados que implementa um processo de ETL (Extração, Transformação e Carga) consumindo dados da API pública DummyJSON. O objetivo é demonstrar a automação na coleta de dados brutos e a sua posterior conversão para formatos estruturados.

🏗️ Estrutura do Pipeline
O projeto foi dividido nas seguintes etapas lógicas:

Extração (extract_data): Realiza requisições GET para os endpoints da API, tratando possíveis erros de conexão.

Carga Inicial (load_data & loop_load_data): Salva os dados brutos em formato .json dentro da pasta data/, simulando uma camada de Data Lake (Raw/Bronze).

Transformação (transform_data_json_to_csv): Utiliza a biblioteca Pandas para ler os arquivos JSON, processá-los em um DataFrame e exportá-los como arquivos .csv na pasta curated/ (camada de dados limpos/Silver).

🛠️ Tecnologias e Bibliotecas
Python 3.x.

Requests: Para consumo da API REST.

Pandas: Para manipulação e transformação de dados estruturados.

JSON: Para manipulação de arquivos de dados semi-estruturados.
