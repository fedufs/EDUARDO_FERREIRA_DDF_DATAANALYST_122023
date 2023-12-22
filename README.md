## Item 1 - Sobre Storytelling e Apresentação
- Para o primeiro item, foi sugerido que a arquitetura original fosse sendo substituída de forma progressiva pelo ecossistema da Dadosfera, o qual oferece uma maior quantidade de vantagens para uma empresa de e-commerce.
- A arquitetura original e a arquitetura progressiva sugerida possuem imagens na pasta "Imagens".
- O vídeo de apresentação no YouTube se encontra neste link - https://youtu.be/_Tx26G8VQ-s 

## Item 2 - Sobre a Dadosfera
- Carga do dataset (coletar) - https://app.dadosfera.ai/pt-BR/collect/pipelines/cae0ce53-c61f-4673-91b8-3d979cd0367c
  
![2 1  Eduardo_Ferreira_carga_pipeline](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/0664b56e-4bcb-48c3-9dde-874f70b9f2df)

- Catálogo - https://app.dadosfera.ai/pt-BR/catalog/data-assets/596f49d8-a4b9-4539-aa35-6034f6c4d299

![2 2  Eduardo_Ferreira_carga_catalogo](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/ca1302bb-fdf4-435f-9073-97dc1e000072)

- Visualização da tabela - https://metabase-treinamentos.dadosfera.ai/question/639-tb-3mochw-product-search-scopus-stream

![2 3  Eduardo_Ferreira_tabela](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/64732785-d888-4d91-8c06-5a7bccc6dc54)

## Item 3 - Sobre GenAI e LLMs
- A LLM utilizada foi o Chat GPT Turbo 3.5.
- As features foram geradas e o código 'main.py' estão neste repositório.
- Os arquivos .csv e .xlsx gerados estão neste repositório.
- O arquivo .env com as chaves foi retirado por questões de segurança.
- Para rodar o código 'main.py' na sua máquina, crie um arquivo .env com as suas chaves OPEN_AI_API_KEY = "sua_chave" e OPEN_AI_ORGANIZATION_KEY = "sua_chave".
- Abaixo, um exemplo do resultado no arquivo .csv com as features determinadas ao final.

![3 1  Eduardo_Ferreira_item3_exemplo_gerado_chatGPT](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/f687689c-fb19-44f8-ad21-90c24aa34f33)

## Item 4 - Sobre SQL e Python
- A primeira análise das categorias dos produtos não ficou muito adequada, pois aparentemente o Chat GPT 3.5 Turbo não conseguiu identificar bem as categorias e os materiais dos produtos somente com base no título e no texto fornecidos. Muitos produtos ficaram sem classificação de categoria e de material, o que prejudicaria qualquer análise.
- Na segunda tentativa eu forneci ao prompt 50 categorias e 50 materiais de produtos de e-commerce com base na resposta do próprio Chat GPT 3.5 Turbo. Com base no título, no texto e nas opções fornecidas ao novo prompt, o código retornou informações bem mais precisas para que uma análise pudesse ser feita
- Imagem da tabela .xlsx oriunda do arquivo .csv:

![4 1  Eduardo_Ferreira_item4_tabela_excel](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/36759ebe-9064-496a-afd3-8cd6d09ff876)

- Link da análise das categorias dos produtos, feita em SQL - https://metabase-treinamentos.dadosfera.ai/question/637-analise-das-categorias-de-produtos

- Imagem da análise:

![4 2  Eduardo_Ferreira_item4_analise_categoria_produtos](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/497a19fc-12b8-40a8-870d-2dba9c5b2ca4)

- Posso concluir que a versão do Chat GPT 3.5 Turbo ainda não foi suficiente para devolver uma segmentação precisa de categoria, material e as demais features quando entreguei informação apenas sobre título e texto de cada produto.
- Quando uma lista pré-determinada de categorias e materiais foi entregue no prompt dentro do mesmo código, o modelo se saiu bem melhor na classificação.

## Item 5 - Sobre DataApps
- Como a plataforma não fez o build inicial, não foi possível realizar a tarefa dentro do ambiente da Dadosfera.
- Então, realizei este item 5 na minha máquina local.
- O código se chama "app.py" e para rodá-lo na sua máquina é preciso digitar 'Streamlit run app.py' no terminal.
- Com todas as bibliotecas necessárias instaladas, o app deve aparecer em uma aba do seu browser.
- Análise por categorias:

![5 1  Eduardo_Ferreira_streamlit_analise_categoria_dataframe](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/c374e535-3bd0-455e-b0fa-75a5fbd37774)

![5 2  Eduardo_Ferreira_streamlit_analise_categoria_grafico](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/9750c474-4925-46f9-86c0-cfe4ecc4bad2)

- Análise por similaridade:

![5 3  Eduardo_Ferreira_streamlit_analise_similarity](https://github.com/fedufs/EDUARDO_FERREIRA_DDF_DATAANALYST_122023/assets/56158987/0102393f-dad2-48b4-94a6-66f66a338c63)

