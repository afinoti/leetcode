# Padrões de Problemas - Notas de Estudo

## 🎯 Two Pointers

### Conceito
Usar dois ponteiros para percorrer estrutura de dados, geralmente em direções opostas ou velocidades diferentes.

### Quando Usar
- Array/string ordenados
- Buscar pares que satisfazem condição
- Detectar ciclos em linked lists

### Problemas Típicos
- Two Sum (array ordenado)
- Three Sum
- Container With Most Water
- Valid Palindrome
- Linked List Cycle

### Template
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition_met:
            return result
        elif need_larger_sum:
            left += 1
        else:
            right -= 1
```

## 🪟 Sliding Window

### Conceito
Manter uma "janela" de elementos contíguos e deslizar pela estrutura.

### Tipos
1. **Fixed Size Window**
2. **Variable Size Window**

### Quando Usar
- Subarray/substring contíguo
- Problemas de otimização (min/max)
- Análise de sequências

### Problemas Típicos
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Sliding Window Maximum

### Template (Variable Size)
```python
def sliding_window(arr):
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # Expand window
        
        while condition_violated:
            # Shrink window
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

## 🐰🐢 Fast & Slow Pointers

### Conceito
Dois ponteiros se movendo em velocidades diferentes (um rápido, um lento).

### Quando Usar
- Detectar ciclos
- Encontrar meio de linked list
- Problemas que envolvem estruturas cíclicas

### Problemas Típicos
- Linked List Cycle
- Find Middle of Linked List
- Happy Number
- Palindrome Linked List

### Template
```python
def fast_slow_pointers(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True  # Cycle detected
    
    return False
```

## 🔄 Merge Intervals

### Conceito
Lidar com intervalos sobrepostos, mesclando ou manipulando-os.

### Quando Usar
- Problemas com intervalos de tempo
- Scheduling
- Range operations

### Problemas Típicos
- Merge Intervals
- Insert Interval
- Meeting Rooms
- Employee Free Time

### Template
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:  # Overlap
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged
```

## 🌊 Cyclic Sort

### Conceito
Posicionar elementos nos seus índices corretos para arrays com números de 1 a n.

### Quando Usar
- Array com números em range específico
- Encontrar números faltantes/duplicados
- Problemas de permutação

### Problemas Típicos
- Find Missing Number
- Find Duplicate Number
- Find All Missing Numbers
- First Missing Positive

### Template
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
```

## 🌳 Tree DFS

### Conceito
Exploração em profundidade de árvores usando recursão ou pilha.

### Tipos
1. **Preorder:** Root → Left → Right
2. **Inorder:** Left → Root → Right
3. **Postorder:** Left → Right → Root

### Problemas Típicos
- Binary Tree Paths
- Path Sum
- Maximum Depth
- Diameter of Binary Tree

### Template (Recursivo)
```python
def tree_dfs(root):
    if not root:
        return
    
    # Process current node
    
    tree_dfs(root.left)   # Visit left subtree
    tree_dfs(root.right)  # Visit right subtree
```

## 🌊 Tree BFS

### Conceito
Exploração em largura usando fila, processando nível por nível.

### Quando Usar
- Level-order traversal
- Encontrar nível específico
- Menor caminho em árvore

### Problemas Típicos
- Level Order Traversal
- Zigzag Level Order
- Minimum Depth
- Connect Level Order Siblings

### Template
```python
def tree_bfs(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 📊 Topological Sort

### Conceito
Ordenação linear de vértices em grafo direcionado acíclico (DAG).

### Implementações
1. **Kahn's Algorithm:** Usando grau de entrada
2. **DFS-based:** Usando ordem de finalização

### Problemas Típicos
- Course Schedule
- Alien Dictionary
- Task Scheduling
- Build Order

### Template (Kahn's Algorithm)
```python
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    
    # Calculate in-degrees
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []
```
