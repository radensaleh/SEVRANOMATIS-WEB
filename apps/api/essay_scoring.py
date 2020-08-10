import string
import pandas as pd
from nltk import ngrams
from nltk.tokenize import RegexpTokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.metrics.pairwise import cosine_similarity


def pre_processing(doc):  # NLP Text Pre-processing
    # Regular Expression - Menghapus karakter angka dan tanda baca
    tokenizer = RegexpTokenizer(r'\w+')
    texts = []

    # Stemmer - Menghilangkan infleksi/kata imbuhan ke dalam bentuk dasar
    stFactory = StemmerFactory()
    st = stFactory.create_stemmer()

    # Stopword - Menghilangkan kata umum yang tidak memiliki makna
    swFactory = StopWordRemoverFactory()
    sw = swFactory.create_stop_word_remover()

    for i in doc:
        raw = i.lower()  # Merubah kata menjadi huruf kecil
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if i in sw.remove(i)]
        stemmed_tokens = [st.stem(i) for i in stopped_tokens]

        texts.append(stemmed_tokens)

    # Detokenize
    detok = []
    for row in texts:
        sq = ''
        for word in row:
            sq = sq + ' ' + word
        detok.append(sq)

    texts = detok
    return texts[0]


def ngram_term(doc):  # N-Gram Document Matriks
    vec = CountVectorizer(ngram_range=(1, 1))
    x = vec.fit_transform(doc).toarray()
    df = pd.DataFrame(x, columns=vec.get_feature_names(),
                      index=['key', 'answer'])
    print(df)
    return x


def lsa(doc):  # Latent Semantic Analysis
    lsa = TruncatedSVD(n_components=2, algorithm='randomized')
    dtm_lsa = lsa.fit_transform(doc)
    dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)
    return dtm_lsa


def scoring(key, answer):
    # Pre-processing Document
    doc = [pre_processing(key), pre_processing(answer)]

    n = ngram_term(doc)
    l = lsa(n)

    cs = cosine_similarity(l, l)

    s = []
    for i in cs:
        s.append(i[0])

    # nilai = []
    # for z in s:
    #     nilai.append(z*100)
        #print(z*100)

    return s[1]*100
    #print(l)
