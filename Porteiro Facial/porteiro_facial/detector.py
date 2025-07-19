import cv2
from deepface import DeepFace
import os
import numpy as np
caminho_banco_de_dados = 'banco_de_dados'
imagem_visitante_path = 'visitante.jpg'
def verificar_rosto(imagem_a_verificar):
  print('Iniciando Reconhecimento Facial Aguarde...')
  try: 
    # Esta é a linha mais importante!
        # Pedimos ao DeepFace para encontrar a pessoa da 'imagem_a_verificar'
        # na nossa pasta 'caminho_banco_dados'.
        # O 'model_name' é o tipo de "cérebro" que o DeepFace vai usar. VGG-Face é um bom padrão.
        resultados = DeepFace.find(img_path=imagem_a_verificar,
                                   db_path=caminho_banco_de_dados,
                                   model_name='VGG-Face',
                                   enforce_detection=True)
        if len(resultados) > 0 and not resultados[0].empty:
             # O resultado é uma lista de DataFrames (tabelas). Pegamos a primeira (a mais provável).
            # A coluna 'identity' contém o caminho para a foto correspondente no banco de dados.
            caminho_foto_encontrada = resultados[0]['idenity'][0]
            nome_arquivo = os.path.basename(caminho_foto_encontrada)
            nome_pessoa, extensao = os.path.splitext(nome_arquivo)
            print(f"Pessoa encontrada: {nome_pessoa}")
            return (True, nome_pessoa, caminho_foto_encontrada)
        else:
            #Se por acaso a lista estiver vazia o sistema ira voltar uma mensage, pessoa nao encontrada
            print('Pessoa não encontrada no sistema')
            return(False,'Desconhecido',None)
  except ValueError as e:
      print(f'ERRO: Não foi possivel reconhecer o rosto na imagem do visitante. {e}')    
      return (False,"Nenhum rosto reconhecido",None)
  def mostrar_resultado(status, nome, caminhho_foto_banco):
      """
      Cria uma janela visual para mostrar se o acesso foi liberado ou negado.
      """
      if status:
          tela_resultado =  np.zeros((400, 600, 3), dtype=np.uint8)
          tela_resultado[:] = (0, 180, 0)
          cv2.putText(tela_resultado, 'Acesso Liberado',) (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
          cv2.putText(tela_resultado, f'Nome: {nome}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
          foto_banco = cv2.imread(caminho_foto_encontrada)
          foto_banco = cv2.resize(foto_banco, (200, 200))
          tela_resultado[150:350, 200:400] = foto_banco
          else:#Se o status for false  (acesso negado)
tela_resultado = np.zeros ((400, 600, 3), dtype=np.uint8)
tela_resultado[:] = (0, 0, 180)
#Escreva msg de erro prr
cv2.putText(tela_resultado, 'Acesso Negado', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
cv2.putText(tela_resultado, nome, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#Mostrar Janela de Resultados
cv2.imshow('Resultado do Porteiro', tela_resultado)
cv2.waitkey(0) #Espere o usuario precionar qualquer tipo de tecla para fechar
cv2.destroyAllWindows() #Feche todas as janelas do OpenCV

if_name_=='_main_':
acesso_liberado, nome, caminho_foto_encontrada = verificar_rosto(imagem_visitante_path)
mostrar_resultado(acesso_liberado, nome_pessoa, foto_banco)
print('Fim da Busca')