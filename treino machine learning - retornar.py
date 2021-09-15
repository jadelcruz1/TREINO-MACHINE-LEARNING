#import wget
#import pandas as pd

from sklearn.svm import LinearSVC
uri = "https://www.in.gov.br/en/web/dou/-/edital-concurso-prf-n-11-de-27-de-maio-de-2021-322821323"

candidato1 = ['J']
candidato2 = ['A']
candidato3 = ['R']



X  = [candidato1, candidato2, candidato3]
y = [aprovados, reprovado]

#modelo = LineaSVC()
#modelo.fit(x,y).