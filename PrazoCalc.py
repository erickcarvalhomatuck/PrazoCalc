import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

# Banco de dados de prazos por área do direito
prazos_por_area = {
    'Direito Civil': {
        'Contestação': 15,
        'Embargos de declaração': 5,
        'Apelação': 15
    },
    'Direito Penal': {
        'Resposta à acusação': 10,
        'Apelação': 5,
        'Habeas corpus': 0  # Imediato, sem prazo específico
    },
    'Direito Trabalhista': {
        'Defesa (contestação)': 10,
        'Apelação': 8,
        'Recurso de revista': 8
    },
    'Direito Tributário': {
        'Impugnação à cobrança': 30,
        'Recurso administrativo': 30,
        'Defesa em processos administrativos fiscais': 30
    },
    'Direito Empresarial': {
        'Defesa em ação de falência': 10,
        'Contestação em ação de cobrança': 15,
        'Defesa em recuperação judicial': 15
    }
}

# Função para adicionar dias, ajustando fim de semana
def adicionar_dias_e_ajustar_fim_de_semana(data_entrada, dias):
    try:
        data_formatada = datetime.strptime(data_entrada, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Use o formato: dd/mm/aaaa")
        return None, None

    nova_data = data_formatada + timedelta(days=dias)
    
    if nova_data.weekday() == 5:  # Sábado
        nova_data -= timedelta(days=1)
    elif nova_data.weekday() == 6:  # Domingo
        nova_data -= timedelta(days=2)
    
    dia_da_semana = nova_data.strftime("%A")
    return nova_data.strftime('%d/%m/%Y'), dia_da_semana

# Função para cálculo da data
def calcular_data():
    area_selecionada = area_var.get()
    opcao_selecionada = opcao_var.get()
    data_entrada = entry.get()

    if not data_entrada:
        messagebox.showerror("Erro", "Por favor, insira uma data.")
        return

    dias = prazos_por_area.get(area_selecionada, {}).get(opcao_selecionada, 0)
    
    nova_data, dia_da_semana = adicionar_dias_e_ajustar_fim_de_semana(data_entrada, dias)
    
    if nova_data:
        resultado.config(text=f"O prazo é: {nova_data}\nDia da semana: {dia_da_semana}")

# Função para mostrar opções da área selecionada
def mostrar_opcoes():
    for widget in opcao_frame.winfo_children():
        widget.destroy()
        
    opcoes = prazos_por_area.get(area_var.get(), {})
    
    for opcao in opcoes:
        rb = ttk.Radiobutton(opcao_frame, text=opcao, variable=opcao_var, value=opcao)
        rb.pack(side=tk.TOP, pady=5)

# Função para exibir a mensagem ao passar o mouse
def mostrar_mensagem(event):
    mensagem_label.config(text="Como usar:\n1. Selecione a área jurídica desejada\n"
                               "2. Insira a data que o andamento foi expedido\n"
                               "3. Selecione que tipo de andamento você deseja calcular prazo\n"
                               "4. Aperte o 'Calcular' e você tem até esse dia para dar um parecer.\n"
                               "Não deixe seus prazos para última hora se você pode fazer hoje.")

def esconder_mensagem(event):
    mensagem_label.config(text="")

# Configuração da interface
root = tk.Tk()
root.title("Calculadora de Prazos Jurídicos")
root.geometry('360x640')  # Tamanho padrão de celular
root.resizable(False, False)  # Impede redimensionamento

# Carrega o ícone
try:
    icone = tk.PhotoImage(file='icone.png')
    root.iconphoto(False, icone)
except Exception as e:
    print("Ícone não encontrado.")

# Configuração de estilos
style = ttk.Style()
style.configure('TLabel', background='#f7f7f7', foreground='#333', font=('Helvetica', 11))
style.configure('TEntry', fieldbackground='#fff', foreground='#000', font=('Helvetica', 12))
style.configure('TRadiobutton', background='#f7f7f7', foreground='#333', font=('Helvetica', 11))

# Frame para seleção da área do direito
area_frame = ttk.Frame(root)
area_frame.pack(pady=20)

ttk.Label(area_frame, text="Selecione a área do direito:", font=('Helvetica', 14, 'bold')).pack(pady=5)
area_var = tk.StringVar(value='Direito Civil')
for area in prazos_por_area.keys():
    ttk.Radiobutton(area_frame, text=area, variable=area_var, value=area, command=mostrar_opcoes).pack(anchor='w')

# Frame para entrada de data
data_frame = ttk.Frame(root)
data_frame.pack(pady=20)

ttk.Label(data_frame, text="Data de entrada (dd/mm/aaaa):", font=('Helvetica', 12)).pack(pady=5)
entry = ttk.Entry(data_frame, width=20)
entry.pack()

# Frame para seleção de opção
opcao_frame = ttk.Frame(root)
opcao_frame.pack(pady=20)
opcao_var = tk.StringVar()
mostrar_opcoes()

# Frame para botão de cálculo
calcular_frame = ttk.Frame(root)
calcular_frame.pack(pady=20)

# Botão com a cor de fundo personalizada
calcular_button = tk.Button(calcular_frame, text="Calcular", command=calcular_data, bg='#017472', fg='white', font=('Helvetica', 12, 'bold'))
calcular_button.pack(padx=10, pady=10)

# Frame para exibir o resultado
resultado_frame = ttk.Frame(root)
resultado_frame.pack(pady=20)
resultado = ttk.Label(resultado_frame, text="", font=('Helvetica', 12, 'bold'))
resultado.pack()

# Símbolo para exibir a mensagem de uso
simbolo_label = ttk.Label(root, text="❓", font=('Helvetica', 16, 'bold'), foreground="#017472")
simbolo_label.place(x=320, y=10)  # Posiciona o símbolo no canto superior direito
simbolo_label.bind("<Enter>", mostrar_mensagem)
simbolo_label.bind("<Leave>", esconder_mensagem)

# Label para mostrar a mensagem
mensagem_label = ttk.Label(root, text="", font=('Helvetica', 10), background='#f7f7f7', foreground='#333')
mensagem_label.pack(pady=5)

root.mainloop()
