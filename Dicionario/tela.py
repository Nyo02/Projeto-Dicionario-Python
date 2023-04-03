from tkinter import *
import requests
from PIL import Image, ImageTk
from tkinter import scrolledtext

# procurar palavra ---------------------------------


def buscar_palavra():
    palavra = txt_pesquisa.get()

    # link da api
    api_link = f"https://dicio-api-ten.vercel.app/v2/{palavra}"
    request = requests.get(api_link)
    dados = request.json()
    printar_resultados(dados)


# cores---------------------------------------------
ciano_claro = '#E0FFFF'
verde_claro = '#B0E0E6'

# Telas e Frames -----------------------------------
tela_principal = Tk()
tela_principal.geometry('350x400')
tela_principal.resizable(width=False, height=False)

frame_alto = Frame(tela_principal, bg=ciano_claro, width=350, height=50)
frame_alto.pack()

frame_meio = Frame(tela_principal, bg=verde_claro, width=350, height=100)
frame_meio.pack()

frame_baixo = Frame(tela_principal, bg=ciano_claro, width=350, height=250, padx=10, pady=10)
frame_baixo.pack()

# logo --------------------------------------------
app_imagem = Image.open("dicionario.png")
app_imagem = ImageTk.PhotoImage(app_imagem)

app_logo = Label(frame_alto, image=app_imagem, bg=ciano_claro, width=60, height=60, )
app_logo.place(x=0, y=0)

app_nome = Label(frame_alto, text="DICIONÁRIO", bg=ciano_claro, font='Verdana 22')
app_nome.place(x=100, y=10)

# Barra de pesquisa ---------------------------------
lbl_pesquisa = Label(frame_meio, text="Insira a palavra:", bg=verde_claro)
lbl_pesquisa.place(x=15, y=15)
txt_pesquisa = Entry(frame_meio)
txt_pesquisa.place(x=18, y=40)

# botao pesquisa ------------------------------------
img_procurar = Image.open('lupa.png')
img_procurar = img_procurar.resize((18, 18))
img_procurar = ImageTk.PhotoImage(img_procurar)
btn_pesquisa = Button(frame_meio, command=buscar_palavra, image=img_procurar, height=18, width=40)
btn_pesquisa.place(x=150, y=40)

saida = scrolledtext.ScrolledText(frame_baixo, )
saida.pack(expand=True, fill='both')
saida.configure(font=20)


# resultado -----------------------------------------
def printar_resultados(dados_pesquisa):
    lista_dados = dados_pesquisa[0]
    classe_gramatical = lista_dados['partOfSpeech']
    significado = lista_dados['meanings']
    etimologia = lista_dados['etymology']

    txt_gramatical = f"Classe gramatical:\n {classe_gramatical}"
    txt_significado = f"Significado:\n{significado}"
    txt_etimologia = f"Etimologia:\n{etimologia}"

    saida.delete('1.0', END)
    saida.insert(END, txt_gramatical + "\n\n" + txt_significado + "\n\n" + txt_etimologia)


tela_principal.mainloop()
