# my api key

import openai

chave_api = "Your API Key"

openai.api_key = chave_api

def enviar_mensagem( mensagem , lista_de_mensagens : list = [] ):
    
    
    lista_de_mensagens.append(
        {"role" : "user" , "content" : mensagem }
    )
    
    resposta = openai.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages = [
            {
                "role": "assistent",
                "content" : lista_de_mensagens  
            }
        ]    
    )
    
    return resposta["choices"][0]["message"]
    
    
lista_mensagens : list = []
while True :
    texto = input("Escreva aqui sua mensagem:")
    
    if texto == "sair":
        break
    else: 
        resposta = enviar_mensagem( mensagem = texto , lista_de_mensagens = lista_mensagens )
        lista_mensagens.append(resposta)
        print("ChatBot: ", resposta["content"])