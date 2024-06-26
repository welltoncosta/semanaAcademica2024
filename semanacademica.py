# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nFc7VxV42sYIOnpXpcWaN7aon-UE17Dt
"""

from google.colab.patches import cv2_imshow


import cv2
import sys

# escolha uma imagem pra reconhecer a face
caminhoImagem = "faces.jpg"

caminhoHaar = "haarcascade.xml"

# Criar o haarcascade através do arquivo
faceCascade = cv2.CascadeClassifier(caminhoHaar)

# Ler a imagem
imagem = cv2.imread(caminhoImagem)
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem
faces = faceCascade.detectMultiScale(
    cinza,
    scaleFactor=1.06,
    minNeighbors=5,
    minSize=(30, 30)
    )




# Desenha um retanculo ao redor das faces
for (x, y, w, h) in faces:
                                               #B  G  R
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 0, 255), 7)

#exibe imagem com faces detectadas
cv2_imshow(imagem)
cv2.waitKey(0)


#Exibe o número de faces detectadas
print("{0} faces encontradas!".format(len(faces)))



"""# New Section

# New Section
"""