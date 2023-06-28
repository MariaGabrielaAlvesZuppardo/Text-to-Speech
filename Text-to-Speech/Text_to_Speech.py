import tkinter as tk
import pyttsx3

def text_to_speech():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Criação da janela principal
window = tk.Tk()
window.title("Conversão de Texto em Fala")

# Criação dos widgets
label = tk.Label(window, text="Digite o texto:")
label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

button = tk.Button(window, text="Converter em Fala", command=text_to_speech)
button.pack()

# Execução da aplicação
window.mainloop()
