import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import keyboard  # Importamos la librería para detectar las teclas

# Variables globales
clicking = False  # Estado de clickeo
interval = 1.0  # Intervalo por defecto entre clics

# Función para realizar los clics automáticos
def auto_click():
    while clicking:
        pyautogui.click()
        time.sleep(interval)

# Función para iniciar/pausar los clics
def start_stop_clicking():
    global clicking
    if clicking:
        clicking = False
        start_button.config(text="Iniciar")
    else:
        clicking = True
        start_button.config(text="Detener")
        threading.Thread(target=auto_click).start()  # Inicia el clic en un hilo separado

# Función para actualizar el intervalo de clics
def update_interval():
    global interval
    try:
        interval = float(interval_entry.get())
        if interval < 0.1:
            raise ValueError("El intervalo debe ser al menos 0.1 segundos.")
    except ValueError as e:
        messagebox.showerror("Error", f"Valor inválido para el intervalo: {e}")

# Función para cerrar el programa
def close_program():
    global clicking
    clicking = False
    root.destroy()

# Función que escucha la tecla de acceso rápido
def hotkey_listener():
    while True:
        if keyboard.is_pressed("F8"):  # Detecta cuando se presiona la tecla F8
            start_stop_clicking()
            time.sleep(0.5)  # Pequeña pausa para evitar múltiples registros de la tecla

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Auto Clicker")

# Etiqueta y campo de entrada para el intervalo de clics
interval_label = tk.Label(root, text="Intervalo entre clics (segundos):")
interval_label.pack(pady=5)

interval_entry = tk.Entry(root)
interval_entry.insert(0, "1.0")  # Valor por defecto
interval_entry.pack(pady=5)

# Botón para actualizar el intervalo
update_button = tk.Button(root, text="Actualizar Intervalo", command=update_interval)
update_button.pack(pady=5)

# Botón para iniciar/detener los clics
start_button = tk.Button(root, text="Iniciar", command=start_stop_clicking)
start_button.pack(pady=10)

# Botón para cerrar el programa
exit_button = tk.Button(root, text="Salir", command=close_program)
exit_button.pack(pady=5)

# Inicia el listener de hotkeys en un hilo separado para no bloquear la interfaz
hotkey_thread = threading.Thread(target=hotkey_listener, daemon=True)
hotkey_thread.start()

# Inicia la aplicación
root.mainloop()

