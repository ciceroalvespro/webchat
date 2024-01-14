# 1 -- Importando o flet
import flet as ft

# 2 -- Criando a função principal
def main(pagina):
    # Criando os elementos da pagina
    titulo = ft.Text('Bem vindo ao Hashzap')
    
    chat = ft.Column()
    
    nome_usuario = ft.TextField(label='Digite seu nome')
    
    # Websoquet tunel de informações
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes)) 
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
         # colocar o nome do usuario na mensagem
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        #chat.controls.append(ft.Text(texto_campo_mensagem)) 
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.pubsub.send_all(texto_campo_mensagem)
        # Atualizar a pagina
        pagina.update()
        
    campo_mensagem = ft.TextField(label='Escreva seu nome', on_submit=enviar_mensagem) 
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        # fecha o popup
        popup.open = False
        # tirar o botao iniciar chat
        pagina.remove(botao_iniciar)
        # espaço do chat
        pagina.add(chat)
        # crie o campo de mensagem # crie o botao de enviar 
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
            )
        pagina.add(linha_mensagem)
        # Atualizar a pagina
        texto = f'{nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(texto)
        pagina.update()
     # Criando o popup
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text('Bem vindo ao Hashapp'),
        content=nome_usuario,
        actions= [ft.ElevatedButton('Entrar', on_click=entrar_chat)]
        )
        
     # Função iniciar chat do botão
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        # atualizar a pagina
        pagina.update()
        
      # Botão iniciar
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    # Adicionando os elementos criados á pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# 3 -- Passando a funcao principal para o app
ft.app(main, view=ft.WEB_BROWSER)
#ft.app(main)

