# Estruturas de Dados - Notas de Estudo

## 📋 Arrays e Strings

### Arrays
- **Acesso:** O(1)
- **Busca:** O(n)
- **Inserção/Remoção:** O(n)
- **Vantagens:** Acesso direto, cache-friendly
- **Desvantagens:** Tamanho fixo, inserção custosa

### Strings
- **Características:** Imutáveis em muitas linguagens
- **Operações comuns:** substring, concatenação, busca
- **Algoritmos:** KMP, Rabin-Karp para pattern matching

## 🔗 Linked Lists

### Singly Linked List
```
[data|next] -> [data|next] -> [data|null]
```
- **Inserção/Remoção:** O(1) se tiver referência
- **Acesso:** O(n)
- **Espaço extra:** O(n) para ponteiros

### Doubly Linked List
```
[prev|data|next] <-> [prev|data|next] <-> [prev|data|null]
```
- **Vantagem:** Navegação bidirecional
- **Desvantagem:** Mais memória

### Técnicas Comuns
- **Two Pointers:** Fast & Slow para detectar ciclos
- **Dummy Node:** Simplifica operações
- **Reversão:** Iterativa vs recursiva

## 🌳 Trees

### Binary Tree
- **Cada nó:** No máximo 2 filhos
- **Traversals:** Inorder, Preorder, Postorder, Level-order
- **Altura:** O(log n) balanceada, O(n) desbalanceada

### Binary Search Tree (BST)
- **Propriedade:** left < root < right
- **Busca/Inserção/Remoção:** O(log n) balanceada
- **Inorder traversal:** Elementos em ordem

### Balanced Trees
- **AVL Tree:** Altura balanceada automaticamente
- **Red-Black Tree:** Balanceamento com cores
- **Garantia:** O(log n) para operações

## 🔥 Heaps

### Min Heap / Max Heap
- **Propriedade:** Pai menor/maior que filhos
- **Inserção:** O(log n)
- **Extração do mínimo/máximo:** O(log n)
- **Peek:** O(1)

### Priority Queue
- **Implementação:** Geralmente com heap
- **Uso:** Algoritmos de grafos, scheduling

## 🗺️ Hash Tables

### Características
- **Acesso/Inserção/Remoção:** O(1) médio
- **Pior caso:** O(n) com muitas colisões
- **Hash Function:** Converte chave em índice

### Tratamento de Colisões
1. **Chaining:** Lista ligada em cada posição
2. **Open Addressing:** Procura próxima posição livre

### Aplicações
- **Sets:** Verificar existência
- **Maps:** Mapeamento chave-valor
- **Frequency counting**

## 📈 Graphs

### Representações
1. **Adjacency Matrix:** O(V²) espaço
2. **Adjacency List:** O(V + E) espaço

### Tipos
- **Directed vs Undirected**
- **Weighted vs Unweighted**
- **Cyclic vs Acyclic (DAG)**

### Algoritmos Fundamentais
- **DFS:** Exploração em profundidade
- **BFS:** Exploração em largura
- **Topological Sort:** Para DAGs
- **Union-Find:** Para componentes conectados

## 🔧 Estruturas Avançadas

### Trie (Prefix Tree)
- **Uso:** Autocompletar, spell checker
- **Busca de prefix:** O(m) onde m é tamanho da string

### Segment Tree
- **Uso:** Range queries e updates
- **Complexidade:** O(log n) para query e update

### Fenwick Tree (Binary Indexed Tree)
- **Uso:** Range sum queries
- **Vantagem:** Menos memória que Segment Tree
