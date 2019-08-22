# ibmcloud-redis

Este repositório contém pedaços de código para facilitar o uso do Redis na IBM Cloud. Ele automatiza a leitura e extração do JSON gerado pela IBM Cloud com as credenciais do serviço, prontas para serem usadas com a biblioteca Python oficial do Redis.

## Como utilizar:

- Crie uma instância do [Redis na IBM Cloud](https://cloud.ibm.com/catalog/services/databases-for-redis)
- Na página Web do serviço instanciado na IBM Cloud, clique na aba `service credentials`.
- Crie uma nova credencial se necessário, e copie todo o conteúdo do JSON gerado.
- Cole o conteúdo do JSON no arquivo `iredis_credentials.json`.
- Já é possível executar o código do arquivo `iredis.py`!
