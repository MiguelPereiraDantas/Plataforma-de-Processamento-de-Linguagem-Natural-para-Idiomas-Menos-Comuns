import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy

# Baixando os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

class PLNPlatform:
    def __init__(self, language, spacy_model):
        self.language = language
        self.stop_words = set(stopwords.words(language))
        self.stemmer = PorterStemmer()
        self.nlp = spacy_model

    def tokenize(self, text):
        # Tokenização usando NLTK
        tokens = word_tokenize(text)
        return tokens

    def remove_stopwords(self, tokens):
        # Remoção de stopwords usando NLTK
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
        return filtered_tokens

    def stem(self, tokens):
        # Redução de palavras ao radical usando NLTK
        stemmed_tokens = [self.stemmer.stem(word) for word in tokens]
        return stemmed_tokens

    def lemmatize(self, text):
        # Lematização usando spaCy
        doc = self.nlp(text)
        lemmatized_tokens = [token.lemma_ for token in doc]
        return lemmatized_tokens

# uso da plataforma PLN
if __name__ == "__main__":
    # Carregue o modelo spaCy para o idioma desejado
    nlp_model = spacy.load('fr_core_news_sm')  # Substitua 'spacy.load('fr_core_news_sm')' pelo código do idioma desejado

    # Instancie a plataforma para um idioma específico
    pln_platform = PLNPlatform('french', nlp_model)  # Se quiser Mudar Substitua 'french' pelo código do idioma desejado

    # Exemplo de texto
    input_text = "Ceci est un exemple de traitement du langage naturel dans une langue moins courante."

    # Tokenização
    tokens = pln_platform.tokenize(input_text)
    print("Tokens:", tokens)

    # Remoção de stopwords
    tokens_without_stopwords = pln_platform.remove_stopwords(tokens)
    print("Tokens sem stopwords:", tokens_without_stopwords)

    # Redução ao radical
    stemmed_tokens = pln_platform.stem(tokens)
    print("Tokens reduzidos ao radical:", stemmed_tokens)

    # Lematização
    lemmatized_tokens = pln_platform.lemmatize(input_text)
    print("Tokens lematizados:", lemmatized_tokens)
