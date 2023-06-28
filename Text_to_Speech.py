import tkinter as tk
import pyttsx3

def text_to_speech():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def clear_text():
    text_entry.delete(0, tk.END)

# Criação da janela principal
window = tk.Tk()
window.title("Conversão de Texto em Fala")

# Criação dos widgets
label = tk.Label(window, text="Digite o texto:")
label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

button_frame = tk.Frame(window)
button_frame.pack()

convert_button = tk.Button(button_frame, text="Converter em Fala", command=text_to_speech)
convert_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Limpar Texto", command=clear_text)
clear_button.pack(side=tk.LEFT)

# Execução da aplicação
window.mainloop()

