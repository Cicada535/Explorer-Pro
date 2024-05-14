# Python 3.10.0
# pip install --update tkinter

# Говнокод ON
from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from io import StringIO
import subprocess
# Говнокод OFF

# Создаём окно
root = Tk()
root.geometry('860x560')
root.configure(background="gray11")
root.title('Explorer Pro')

# Добавляем иконку
root.iconphoto(False, PhotoImage(file="Exploer-Pro\Explorer-Pro.png"))

# Создаём текстовое поле для кода
code_editor = tk.Text(root, background="gray11", foreground="white", insertbackground="white")
code_editor.pack(fill=tk.BOTH, expand=True)

# Добавляем подсветку синтаксиса
code_editor.tag_configure("keyword", foreground="blue")
code_editor.tag_configure("string", foreground="red")
code_editor.tag_configure("comment", foreground="green")
code_editor.tag_configure("number", foreground="magenta")

# Определяем стили для тёмной темы
dark_theme = {
    "background": "gray11",
    "foreground": "white",
    "insertbackground": "white",
    "selectbackground": "gray15",
    "inactiveselectbackground": "gray18"
}

# Применяем тёмную тему
for key, value in dark_theme.items():
    code_editor.configure(*{key: value})

# Определяем функцию для запуска кода
def run_code():
    # Получаем код из текстового поля
    code = code_editor.get("1.0", "end")

    # Создаем процесс для запуска кода
    process = subprocess.Popen(["python", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Запускаем код и получаем вывод
    output, error = process.communicate(code.encode())

    # Выводим результат в консоль
    print(output.decode())

# Создаём кнопку для запуска кода
run_button = ttk.Button(root, text="Запустить", command=run_code)
run_button.pack()

# Запускаем окно редактора кода
root.mainloop()
