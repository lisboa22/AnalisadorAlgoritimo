# Analisador de Algoritmos

## Descrição

Este projeto foi desenvolvido como parte da disciplina de **Análise de Algoritmos**. O objetivo da aplicação é fornecer uma ferramenta gráfica para experimentação, análise e comparação de diferentes algoritmos clássicos, permitindo observar seu desempenho prático em relação à complexidade teórica.

Através da interface, o usuário pode selecionar entre diversos tipos de algoritmos, informar o tamanho da entrada e analisar o tempo de execução para cada caso. Além disso, a aplicação gera gráficos que ilustram o comportamento dos algoritmos conforme o tamanho do problema cresce, facilitando a compreensão sobre o impacto da complexidade computacional.

## Funcionalidades

- **Seleção de algoritmos:** Permite escolher entre algoritmos de diferentes paradigmas.
- **Entrada personalizada:** O usuário define o tamanho da entrada (n) para os testes.
- **Análise automática:** Executa o algoritmo selecionado, exibe o resultado, o tempo de execução e a complexidade estimada.
- **Visualização gráfica:** Gera um gráfico da evolução do tempo de execução em função do tamanho da entrada, para facilitar a comparação entre algoritmos.

## Algoritmos Disponíveis

A aplicação contempla os seguintes algoritmos e paradigmas:

1. **Iterativo**
   - Soma simples de números: Complexidade O(n)
2. **Recursivo (Fibonacci)**
   - Implementação recursiva do cálculo de Fibonacci: Complexidade O(2^n)
3. **Dividir para Conquistar (MergeSort)**
   - Algoritmo de ordenação por intercalação: Complexidade O(n log n)
4. **Programação Dinâmica (Fibonacci)**
   - Cálculo de Fibonacci usando abordagem dinâmica: Complexidade O(n)
5. **Guloso (Mochila Fracionária)**
   - Algoritmo para o problema da mochila fracionária: Complexidade O(n log n)
6. **Backtracking (Subconjuntos)**
   - Geração de todos os subconjuntos de um conjunto: Complexidade O(2^n)

## Como funciona

1. O usuário inicia a aplicação e escolhe o algoritmo a ser analisado.
2. Informa o valor de `n`, que representa o tamanho da instância do problema (pode variar conforme o algoritmo).
3. Ao clicar em "Analisar", a aplicação executa o algoritmo, mede o tempo de execução e apresenta:
   - O nome do algoritmo
   - O resultado da execução (parcial, se muito extenso)
   - O tempo de execução
   - A complexidade estimada
4. Um gráfico é gerado mostrando como o tempo de execução cresce com o aumento do tamanho da entrada.

## Tecnologias Utilizadas

- **Python 3**
- **Tkinter**: Interface gráfica
- **Matplotlib**: Geração de gráficos
- **time**: Medição do tempo de execução dos algoritmos

## Estrutura do Código

- **Funções de Algoritmos:** Cada paradigma está implementado em funções separadas, facilitando testes e comparações.
- **Análise de desempenho:** Função dedicada para medir o tempo de execução de cada algoritmo.
- **Complexidade estimada:** Função que retorna a complexidade teórica esperada para cada algoritmo.
- **Interface gráfica:** Classe principal `AnalisadorApp` encapsula toda a lógica da interface, entrada do usuário, execução dos algoritmos e exibição dos resultados e gráficos.

## Uso

1. Instale as dependências necessárias:
   ```bash
   pip install matplotlib
   ```
2. Execute o arquivo principal:
   ```bash
   python <nome_do_arquivo>.py
   ```
3. Use a interface gráfica para explorar diferentes algoritmos e analisar seus desempenhos.

## Observações

- Para algoritmos de complexidade exponencial (Recursivo Fibonacci e Backtracking), recomenda-se cautela ao escolher valores elevados de `n`, pois o tempo de execução pode se tornar impraticável.
- Os gráficos são adaptados automaticamente para evitar execuções excessivamente longas em casos exponenciais.

## Autor

Desenvolvido por **Robson Lisboa Santos** para fins didáticos na matéria de Análise de Algoritmos.

---

Este projeto é uma excelente ferramenta para estudar e comparar o comportamento prático de algoritmos sob diferentes paradigmas, auxiliando no entendimento das implicações da complexidade computacional.
