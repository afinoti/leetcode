# Algoritmos - Notas de Estudo

## 🔍 Algoritmos de Busca

### Binary Search
- **Complexidade:** O(log n)
- **Uso:** Arrays ordenados
- **Padrão:** Dividir pela metade repetidamente

### Linear Search
- **Complexidade:** O(n)
- **Uso:** Arrays não ordenados
- **Padrão:** Verificar elemento por elemento

## 🔄 Algoritmos de Ordenação

### Quick Sort
- **Complexidade:** O(n log n) médio, O(n²) pior caso
- **Estabilidade:** Não estável
- **Espaço:** O(log n)

### Merge Sort
- **Complexidade:** O(n log n)
- **Estabilidade:** Estável
- **Espaço:** O(n)

### Heap Sort
- **Complexidade:** O(n log n)
- **Estabilidade:** Não estável
- **Espaço:** O(1)

## 📊 Algoritmos em Grafos

### DFS (Depth-First Search)
- **Complexidade:** O(V + E)
- **Uso:** Detecção de ciclos, componentes conectados
- **Implementação:** Recursiva ou pilha

### BFS (Breadth-First Search)
- **Complexidade:** O(V + E)
- **Uso:** Menor caminho (grafo não ponderado)
- **Implementação:** Fila

### Dijkstra
- **Complexidade:** O((V + E) log V)
- **Uso:** Menor caminho em grafo ponderado
- **Limitação:** Não funciona com pesos negativos

## 🧮 Programação Dinâmica

### Características
- Subproblemas sobrepostos
- Subestrutura ótima
- Memoização vs Tabulação

### Padrões Comuns
1. **0/1 Knapsack**
2. **Unbounded Knapsack**
3. **Longest Common Subsequence**
4. **Palindrome Partitioning**
5. **Edit Distance**

## 🔄 Algoritmos de Backtracking

### Características
- Exploração exaustiva
- Poda de caminhos inválidos
- Retrocesso quando necessário

### Problemas Típicos
- N-Queens
- Sudoku Solver
- Combination Sum
- Word Search

## 🎯 Algoritmos Gulosos (Greedy)

### Características
- Escolha localmente ótima
- Nem sempre garante solução global ótima
- Eficiente quando aplicável

### Exemplos
- Activity Selection
- Fractional Knapsack
- Huffman Coding
