import flet as ft

def main(page:ft.Page):
    #page.theme = "dark"
    def handle_click(e):
        page.add(ft.Text("Cliquei aqui"))

    ola = ft.Text('Olá, Mundo!', size=50, color="green", bgcolor='white')
    botao = ft.ElevatedButton (text="clique aqui", on_click=handle_click)
    page.add(ola, botao)
    
ft.app(target=main)
