import tkinter as tk
from tkinter import ttk, messagebox
import time
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def exemplo_iterativo(n):
    total = 0
    for i in range(n):
        total += i
    return total

def exemplo_recursivo(n):
    if n <= 1:
        return n
    return exemplo_recursivo(n-1) + exemplo_recursivo(n-2)

def dividir_para_conquistar(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = dividir_para_conquistar(arr[:meio])
    direita = dividir_para_conquistar(arr[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

def programacao_dinamica(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def guloso_mochila(valores, pesos, capacidade):
    proporcao = sorted([(v/p, v, p) for v, p in zip(valores, pesos)], reverse=True)
    total = 0
    for frac, v, p in proporcao:
        if capacidade >= p:
            capacidade -= p
            total += v
        else:
            total += frac * capacidade
            break
    return total

def backtracking_subconjuntos(nums):
    resultado = []
    def backtrack(caminho, inicio):
        resultado.append(caminho[:])
        for i in range(inicio, len(nums)):
            caminho.append(nums[i])
            backtrack(caminho, i + 1)
            caminho.pop()
    backtrack([], 0)
    return resultado

# --- Analisador ---

def analisar_tempo_execucao(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def estimar_complexidade(func_name):
    complexidades = {
        "Iterativo": "O(n)",
        "Recursivo (Fibonacci)": "O(2^n)",
        "Dividir para Conquistar (MergeSort)": "O(n log n)",
        "Programação Dinâmica (Fibonacci)": "O(n)",
        "Guloso (Mochila Fracionária)": "O(n log n)",
        "Backtracking (Subconjuntos)": "O(2^n)"
    }
    return complexidades.get(func_name, "Desconhecida")

# --- Interface Gráfica ---

class AnalisadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Algoritmos")
        self.root.geometry("750x750")

        # Adiciona o protocolo para fechar o programa corretamente
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_programa)

        self.label = ttk.Label(root, text="Robson Lisboa Santos")
        self.label.pack(pady=4)
        self.label = ttk.Label(root, text="Escolha o algoritmo:")
        self.label.pack(pady=10)

        self.combo = ttk.Combobox(root, values=[
            "Iterativo",
            "Recursivo (Fibonacci)",
            "Dividir para Conquistar (MergeSort)",
            "Programação Dinâmica (Fibonacci)",
            "Guloso (Mochila Fracionária)",
            "Backtracking (Subconjuntos)"
        ])
        self.combo.pack()

        self.label_n = ttk.Label(root, text="Digite o valor de n:")
        self.label_n.pack(pady=5)

        self.entrada_n = ttk.Entry(root)
        self.entrada_n.pack()

        self.botao_analisar = ttk.Button(root, text="Analisar", command=self.executar_algoritmo)
        self.botao_analisar.pack(pady=10)

        self.resultado_texto = tk.Text(root, height=9, width=90)
        self.resultado_texto.pack(pady=10)
        
        self.grafico_frame = ttk.Frame(root)
        self.grafico_frame.pack(pady=10)
        self.canvas = None

    def fechar_programa(self):
        self.root.destroy()
        self.root.quit()

    def executar_algoritmo(self):
        nome_algoritmo = self.combo.get()
        try:
            n = int(self.entrada_n.get())
            if n < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro positivo para n.")
            return

        if nome_algoritmo == "Iterativo":
            resultado, tempo = analisar_tempo_execucao(exemplo_iterativo, n)
        elif nome_algoritmo == "Recursivo (Fibonacci)":
            resultado, tempo = analisar_tempo_execucao(exemplo_recursivo, n)
        elif nome_algoritmo == "Dividir para Conquistar (MergeSort)":
            arr = list(range(n, 0, -1))
            resultado, tempo = analisar_tempo_execucao(dividir_para_conquistar, arr)
        elif nome_algoritmo == "Programação Dinâmica (Fibonacci)":
            resultado, tempo = analisar_tempo_execucao(programacao_dinamica, n)
        elif nome_algoritmo == "Guloso (Mochila Fracionária)":
            valores = list(range(n, 0, -1))
            pesos = [i+1 for i in range(n)]
            capacidade = sum(pesos) // 2
            resultado, tempo = analisar_tempo_execucao(guloso_mochila, valores, pesos, capacidade)
        elif nome_algoritmo == "Backtracking (Subconjuntos)":
            arr = list(range(n))
            resultado, tempo = analisar_tempo_execucao(backtracking_subconjuntos, arr)
        else:
            messagebox.showwarning("Aviso", "Selecione um algoritmo válido.")
            return

        complexidade = estimar_complexidade(nome_algoritmo)

        self.resultado_texto.delete("1.0", tk.END)
        self.resultado_texto.insert(tk.END, f"Algoritmo: {nome_algoritmo}\n")
        self.resultado_texto.insert(tk.END, f"Resultado: {str(resultado)[:300]}...\n")
        self.resultado_texto.insert(tk.END, f"Tempo de execução: {tempo:.6f} segundos\n")
        self.resultado_texto.insert(tk.END, f"Complexidade Estimada: {complexidade}\n")
        
        self.exibir_grafico(nome_algoritmo)

    def exibir_grafico(self, nome_algoritmo):
        tamanhos = [i for i in range(1, 15)]
        tempos = []

        for n in tamanhos:
            if nome_algoritmo == "Iterativo":
                _, t = analisar_tempo_execucao(exemplo_iterativo, n*1000)
            elif nome_algoritmo == "Recursivo (Fibonacci)":
                if n > 30:
                    break
                _, t = analisar_tempo_execucao(exemplo_recursivo, n)
            elif nome_algoritmo == "Dividir para Conquistar (MergeSort)":
                arr = list(range(n*500, 0, -1))
                _, t = analisar_tempo_execucao(dividir_para_conquistar, arr)
            elif nome_algoritmo == "Programação Dinâmica (Fibonacci)":
                _, t = analisar_tempo_execucao(programacao_dinamica, n*500)
            elif nome_algoritmo == "Guloso (Mochila Fracionária)":
                valores = list(range(n*200, 0, -1))
                pesos = [i+1 for i in range(n*200)]
                capacidade = sum(pesos) // 2
                _, t = analisar_tempo_execucao(guloso_mochila, valores, pesos, capacidade)
            elif nome_algoritmo == "Backtracking (Subconjuntos)":
                if n > 20:
                    break
                arr = list(range(n))
                _, t = analisar_tempo_execucao(backtracking_subconjuntos, arr)
            tempos.append(t)
        
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(tamanhos[:len(tempos)], tempos, marker="o")
        ax.set_title(f"Desempenho - {nome_algoritmo}")
        ax.set_xlabel("Tamanho de entrada (n)")
        ax.set_ylabel("Tempo (segundos)")

        self.canvas = FigureCanvasTkAgg(fig, master=self.grafico_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# --- Execução ---

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalisadorApp(root)
    root.mainloop()