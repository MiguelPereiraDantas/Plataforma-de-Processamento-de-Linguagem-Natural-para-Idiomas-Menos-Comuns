# Plataforma de Processamento de Linguagem Natural para Idiomas Menos Comuns

Este é um projeto de plataforma de processamento de linguagem natural (PLN) que lida com idiomas menos comuns. Ele oferece funcionalidades básicas, como tokenização, remoção de stopwords, redução ao radical (stemming) e lematização, além de reconhecimento de entidades e análise de sentimentos.

## Pré-requisitos

Certifique-se de ter Python instalado. Você pode instalar as dependências usando:

```bash
pip install -r requirements.txt
```
## Uso
1. Baixe os recursos necessários do NLTK:

```bash
python -m nltk.downloader punkt stopwords
```

2. Baixe o modelo spaCy para o idioma desejado. Substitua 'spacy.load('fr_core_news_sm')' pelo código do idioma desejado.

```bash
python -m spacy download xx
```
3. Execute o script principal:
```bash
python app.py
```
4. Insira o texto quando solicitado e observe os resultados.
## Funcionalidades
- Tokenização
- Remoção de stopwords
- Redução ao radical (stemming)
- Lematização
- Reconhecimento de entidades
- Análise de sentimentos
## Contribuição
Sinta-se à vontade para contribuir com melhorias, correções ou adição de novas funcionalidades. Abra uma issue para discutir mudanças significativas antes de enviar um pull request.

## Licença
Este projeto é licenciado sob a MIT License.