# 🎯 FAANG Master Guide: SPEC → PLAN → TASKS

**Objetivo:** Não memorizar soluções. Entender como **reconhecer padrões** e **escolher a melhor abordagem** para cada problema.

---

## 📋 Framework SPEC → PLAN → TASKS

```
┌─────────────────────────────────────────────────────────┐
│ SPEC: O QUÊ? (Definir o problema)                      │
│ • Contrato Input/Output                                 │
│ • Edge cases e restrições                               │
│ • Propriedades matemáticas (monotonicidade?)            │
│ • Força bruta naive (sempre comece aqui!)               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PLAN: COMO? (Escolher a técnica)                        │
│ • Reconhecer padrão (BFS? DP? Greedy? Binary Search?)   │
│ • Comparar trade-offs (Time vs Space vs Legibilidade)   │
│ • Justificar escolha (por quê THIS padrão?)             │
│ • Pseudocódigo e diagrama                               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ TASKS: CÓDIGO (Implementar + Validar)                   │
│ • Código limpo e comentado                              │
│ • Testes (edge cases, casos normais ...)            │
│ • Análise de complexidade (Time + Space)                │
│ • Débug (printf-debugging, trace mental)                │
└─────────────────────────────────────────────────────────┘
```

---

## 🔍 SPEC: Checklist Detalhado

### 1️⃣ **Contrato Input/Output**

| Aspecto | Pergunta | Exemplo |
|---------|----------|---------|
| **Tipos de entrada** | List? Dict? Tree? Graph? String? | `nums: List[int]`, `intervals: List[List[int]]` |
| **Ranges/Constraints** | Qual é o tamanho máximo? Valores podem ser negativos? | `1 <= n <= 10^4`, `1 <= nums[i] <= 10^9` |
| **Tipo de saída** | int? bool? List? Estrutura customizada? | `int` (count), `bool` (viável?), `List[int]` (indices) |
| **Ordem da saída** | Importa? Pode ser qualquer ordem? | Sorted? Em qual ordem? |

### 2️⃣ **Edge Cases Críticos**

Sempre teste esses casos:

```python
# Tamanho
[], [1], [1, 2]           # Vazio, singleton, pair

# Valores duplicados
[1, 1, 1], [1, 2, 1]     # Todos iguais, repetições

# Extremos
[-10^9, 0, 10^9]         # Min, zero, max

# Casos especiais do domínio
# Strings: "", strings com espaços, caracteres especiais
# Arrays: Arrays já ordenados, inversamente ordenados
# Grafos: Grafo desconexo, nó isolado, ciclos
```

### 3️⃣ **Propriedades Matemáticas**

Pergunta-chave: **Qual propriedade do problema ajuda a resolver?**

| Propriedade | Implicação | Padrão Sugerido |
|-------------|-----------|-----------------|
| **Monotonicidade** | Se `f(k)` funciona, `f(k+1)` funciona? | Binary Search |
| **Subestrutura ótima** | Solução ótima = combina soluções ótimas dos subproblemas? | DP |
| **Indecisão simples** | Preciso explorar TODAS as possibilidades? | Backtracking, DFS |
| **Greedy choice** | Escolher o melhor LOCAL sempre leva ao ótimo GLOBAL? | Greedy |
| **Estrutura linear** | Array/String processados da esquerda para direita? | Sliding Window, DP 1D |
| **Grafo/Árvore** | Vizinhanças, níveis, caminos? | BFS, DFS, DSU, Topological Sort |

---

## 🎓 PLAN: Matriz de Trade-offs

### Quando usar cada técnica?

```
┌─────────────────────────┬──────────┬──────────┬──────────────────┐
│ Técnica                 │ Time     │ Space    │ Quando usar      │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ FORCE BRUTE             │ O(n!)    │ O(1)     │ Sempre comece    │
│ (tenta tudo)            │ O(2^n)   │          │ aqui! n < 20     │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ BACKTRACKING + PRUNING  │ O(n!)    │ O(n)     │ Combinações,     │
│ (força bruta smart)     │ O(2^n)   │ recursão │ Permutações,     │
│                         │ (melhor) │ stack    │ Sudoku           │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ DYNAMIC PROGRAMMING     │ O(n²)    │ O(n²)    │ Subestrutura     │
│ (memoization/tabulation)│ O(n³)    │ O(n)     │ ótima, repetição │
│                         │ (dep)    │ (rolling)│ de subproblemas  │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ DFS (graph/tree)        │ O(V+E)   │ O(V)     │ Explorar         │
│                         │ ou O(n)  │ recursão │ profundidade,    │
│                         │          │ stack    │ Connected comps  │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ BFS (graph/tree)        │ O(V+E)   │ O(V)     │ Menor caminho,   │
│                         │ ou O(n)  │ queue    │ Nível a nível    │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
| BINARY SEARCH           │ O(log n) │ O(1)     │ Função monotônica |
│ (on answer/value)       │          │          │ (não é sobre      |
│                         │          │          │ ordenação!)       |
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ GREEDY                  │ O(n)     │ O(1)     │ Greedy choice    │
│                         │ O(n log n)│ O(n)    │ provável ótima   │
│                         │          │ (sort)   │                  │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ SLIDING WINDOW          │ O(n)     │ O(k)     │ Subarrays/       │
│                         │          │ (hash)   │ substrings       │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ HASH MAP / SET          │ O(n) avg │ O(n)     │ Lookup rápido,   │
│                         │ O(n²) bad│          │ Frequência       │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ HEAP / PRIORITY QUEUE   │ O(n log n)│ O(n)   │ Top K, Mediana   │
│                         │          │          │ Merge K          │
├─────────────────────────┼──────────┼──────────┼──────────────────┤
│ MONOTONIC STACK         │ O(n)     │ O(n)     │ Próximo elemento │
│ (Deque/Stack simples)   │          │ stack    │ MAIOR/MENOR,     │
│                         │          │          │ Daily Temps      │
└─────────────────────────┴──────────┴──────────┴──────────────────┘
```

### Exemplos de Trade-offs

#### ✅ **Problema: Find Minimum in Rotated Sorted Array**

| Abordagem | Time | Space | Viável? | Razão |
|-----------|------|-------|---------|-------|
| Linear scan | O(n) | O(1) | ✅ Sim | Sempre funciona, mas lento |
| Binary Search | O(log n) | O(1) | ✅✅ MELHOR | Array está **sorted** → propriedade monotônica |
| DP | O(n) | O(n) | ❌ Não | Sem subestrutura ótima |

**Conclusão:** Use Binary Search porque o array é sorted → monotonicidade.

---

#### ✅ **Problema: N-Queens**

| Abordagem | Time | Space | Viável? | Razão |
|-----------|------|-------|---------|-------|
| Brute force (try all) | O(n!·n²) | O(n²) | ❌ Horrível | Timeout para n > 8 |
| Backtracking + pruning | O(n!) | O(n) | ✅✅ MELHOR | Prune ramos inviáveis early |
| DP | ❌ Não aplicável | - | ❌ Não | Sem subestrutura ótima |

**Conclusão:** Use Backtracking porque precisamos explorar TODAS as combinações + poder fazer pruning.

---

#### ✅ **Problema: Coin Change (mínimo moedas para valor X)**

| Abordagem | Time | Space | Viável? | Razão |
|-----------|------|-------|---------|-------|
| Greedy (maior moeda first) | O(n) | O(1) | ❌ Não | Não sempre ótimo (ex: [1,3,4], value=6) |
| DFS (try all coins) | O(k^n) | O(n) | ❌ Exponencial | Sem otimização |
| DP (memoization) | O(n·k) | O(n) | ✅✅ MELHOR | Subestrutura ótima: min(coin1..k) + min(rest) |

**Conclusão:** Use DP porque temos subestrutura ótima + repetição de subproblemas.

---

## 🚀 Decision Tree: Como Escolher?

```
NOVO PROBLEMA
     ↓
[1] É um problema de GRAFO/ÁRVORE?
     YES → BFS (shortest path) ou DFS (conectividade)?
           → Topological sort? → Dijkstra?
     NO → [2]
     
[2] Preciso ENCONTRAR TODAS as soluções (combinações/permutações)?
     YES → BACKTRACKING + PRUNING (N-Queens, Sudoku)
     NO → [3]
     
[3] É um problema de OTIMIZAÇÃO (min/max)?
     YES → [4a]
     NO → [5]
     
[4a] A função objetivo é MONOTÔNICA?
      YES → BINARY SEARCH ON ANSWER (Koko Bananas)
           ⚠️ IMPORTANTE: Monotonicidade de FUNÇÃO (curva sempre sobe/desce)
                         NÃO confundir com MONOTONIC STACK (estrutura de dados)!
                         
                         Monotonic Stack é para problemas como:
                         - Nearest Greater/Smaller Element
                         - Daily Temperatures
                         - Trapping Rain Water
                         
                         Use Monotonic Stack quando precisa encontrar padrões
                         de vizinhança em arrays (não é otimização com busca)
      
      NO → [4b]
      
[4b] Tem SUBESTRUTURA ÓTIMA (solução ótima = opt(subproblemas))?
      YES → DYNAMIC PROGRAMMING (Coin Change, LIS, House Robber)
      NO → GREEDY (Jump Game, Interval Scheduling)
           ⚠️ Greedy nem sempre funciona! Prove ou valide com testes.
           
[5] É um SUBSTRING/SUBARRAY problem?
     YES → SLIDING WINDOW (Fixed/Variable size)
           ou TWO POINTERS (contraste entre elementos)
     NO → [6]
     
[6] Frequência, rank, top K?
     YES → HEAP / HASH MAP (K Frequent, Kth Largest)
     NO → [7]
     
[7] Array/String simples?
     YES → TWO POINTERS, SORT + GREEDY, ou HASH MAP
     NO → Check outras propriedades (linked list? matrix?)
```

---

## 🎯 Padrões de Reconhecimento

### 1. **Quando reconhecer DP?**

```
GATILHOS DP:
✅ "mínimo", "máximo" (otimização)
✅ "contar", "número de formas" (combinatória)
✅ "é possível?", "viável?" (decisão)
✅ Overlapping subproblems (fibonacci, coin change)
✅ Subestrutura ótima (a resposta usa respostas menores)

Frases que triggerem DP:
- "Minimum steps to..."
- "Maximum product of..."
- "Number of ways to..."
- "Can we achieve...?"
- "Is it possible...?"
```

**Exemplo:** "Mínimo número de moedas para fazer X"
→ Subestrutura: `min_coins(X) = 1 + min(min_coins(X - coin) for each coin)`

---

### 2. **Quando reconhecer Backtracking?**

```
GATILHOS BACKTRACKING:
✅ "todas as combinações" / "todas as permutações"
✅ "encontrar todas as soluções"
✅ "escolher/descartar elementos"
✅ Decisões independentes em cada nível

Frases que triggerem Backtracking:
- "Find ALL combinations/permutations"
- "Generate all valid..."
- "Solve the puzzle" (Sudoku, N-Queens)
- "All possible ways to..."
```

**Exemplo:** "Todas as permutações de uma string"
→ Escolha: cada posição pode ter qualquer caractere ainda não usado.

---

### 2️⃣ **O que é Monotonicidade? (Conceito Essencial)**

Monotonicidade é a propriedade de uma **FUNÇÃO**, não dos dados!

#### 📐 Definição Matemática

```
Função MONOTÔNICA (crescente ou decrescente) significa que:

CRESCENTE MONÓTONA:
  Se x₁ < x₂, então f(x₁) ≤ f(x₂) (ou < para estritamente crescente)
  Exemplo: f(x) = x, f(x) = 2x + 1, f(x) = √x
  
DECRESCENTE MONÓTONA:
  Se x₁ < x₂, então f(x₁) ≥ f(x₂) (ou > para estritamente decrescente)
  Exemplo: f(x) = -x, f(x) = 1/x, f(x) = -2x + 5
```

#### 🎯 Regra Simples

```
✅ MONOTÔNICA: Sempre vai na MESMA DIREÇÃO
   • Sempre cresce: f(1) < f(2) < f(3) < f(4) ...
   • Sempre decresce: f(1) > f(2) > f(3) > f(4) ...
   • Nunca muda de direção!

❌ NÃO MONOTÔNICA: Muda de direção
   • Cresce e depois decresce: f(1) < f(2) < f(3) > f(4) ❌
   • Decresce e depois cresce: f(1) > f(2) > f(3) < f(4) ❌
```

#### 🔍 Exemplos Visuais

```
CRESCENTE MONÓTONA (f(x) = x²):
y
  |                  ●  
  |              ●
  |          ●
  |      ●
  |  ●
  └─────────────→ x
  
  Padrão: Sempre SOBE (ou fica igual)
  Logo: f(1) < f(2) < f(3) < f(4)

───────────────────────────────────

DECRESCENTE MONÓTONA (f(x) = -x):
y
  |  ●
  |      ●
  |          ●
  |              ●
  |                  ●
  └─────────────→ x
  
  Padrão: Sempre DESCE (ou fica igual)
  Logo: f(1) > f(2) > f(3) > f(4)

───────────────────────────────────

NÃO MONOTÔNICA (f(x) = x² - 4x):
y
  |  ●
  |      ●
  |          ●
  |      ●
  |  ●
  └─────────────→ x
  
  Padrão: Desce, depois SOBE
  Logo: ❌ NÃO é monotônica! (muda de direção)
```

#### 💡 Aplicação: Por que Binary Search precisa de Monotonicidade?

```
PROBLEMA: Procurar um valor em um espaço grande [1, 10^9]

Com MONOTONICIDADE (f sempre cresce ou sempre decresce):
  Se estou no meio e f(mid) > target:
    → Posso ignorar METADE do espaço com segurança!
    → Porque sei que não vai mudar de direção
  
  Logo: O(log n) é garantido! ✅

Sem MONOTONICIDADE (f sobe e desce):
  Se estou no meio e f(mid) > target:
    → Não sei se ignorar esquerda ou direita!
    → A resposta pode estar em QUALQUER LUGAR
  
  Logo: Preciso de força bruta O(n) ❌
```

#### 🔗 Exemplo: Koko Eating Bananas (MONOTÔNICA DECRESCENTE)

```
Pilhas: [3, 6, 7, 11]
Horas disponíveis: 8

Função: hours_needed(k) = sum(ceil(pile / k))

Valores:
  k=1  → hours_needed(1)  = 4 + 6 + 7 + 11 = 28
  k=2  → hours_needed(2)  = 2 + 3 + 4 + 6  = 15
  k=3  → hours_needed(3)  = 2 + 2 + 3 + 4  = 11
  k=4  → hours_needed(4)  = 1 + 2 + 2 + 3  = 8  ← resposta!
  k=5  → hours_needed(5)  = 1 + 2 + 2 + 3  = 8
  k=6  → hours_needed(6)  = 1 + 1 + 2 + 2  = 6
  k=7  → hours_needed(7)  = 1 + 1 + 1 + 2  = 5

Propriedade: 28 > 15 > 11 > 8 ≥ 8 > 6 > 5
             SEMPRE DECRESCENTE (ou igual)
             
✅ É MONOTÔNICA! Logo Binary Search funciona.
```

#### ❌ Contraexemplo: NÃO MONOTÔNICA

```
Função: f(x) = x² - 8x + 12 (parábola)

Valores:
  x=0 → f(0) = 12
  x=1 → f(1) = 5
  x=2 → f(2) = 0
  x=3 → f(3) = -3
  x=4 → f(4) = -4  ← mínimo
  x=5 → f(5) = -3
  x=6 → f(6) = 0
  x=7 → f(7) = 5

Propriedade: 12 > 5 > 0 > -3 > -4 < -3 < 0 < 5
             Desce depois SOBE!
             
❌ NÃO é MONOTÔNICA! Binary Search NÃO funciona diretamente.
   (Precisaria de técnica especial para encontrar o mínimo)
```

---

### 3. **Quando reconhecer Binary Search?**

```
GATILHOS BINARY SEARCH:
✅ Função é MONOTÔNICA: f(x) = [F, F, ..., F, T, T, ..., T] ou [T, T, ..., T, F, F]
✅ "Mínimo X tal que..." ou "Máximo X tal que..."
✅ Array sorted OU espaço de busca bem definido
✅ Constraints: n até 10^18 (log n é viável, linear não)

⚠️ IMPORTANTE: Monotonicidade NÃO é ordenação!
   • Monotonicidade = propriedade da FUNÇÃO (input ↑ → output ↑ ou ↓)
   • Ordenação = estado dos DADOS (array em ordem crescente)
   • Exemplo Koko: [3,6,7,11] NÃO é sorted, mas horas_needed(k) é monotônica

Frases que triggerem Binary Search:
- "Minimum/Maximum [X] such that [condition]"
- "Can we do it in [X] time/capacity?"
- "First/Last position of..."
```

**Exemplo:** "Mínimo velocidade para comer todas as bananas" (Koko)
→ Monotonicidade: se velocidade V funciona, V+1 também funciona.

---

### 4️⃣ **Quando reconhecer Monotonic Stack? (NÃO confundir com Binary Search!)**

```
⚠️ ALERTA CONFUSÃO:
   Muitas pessoas confundem "Monotônica" (Binary Search) 
   com "Monotonic Stack" (estrutura de dados)
   
   SÃO COISAS COMPLETAMENTE DIFERENTES!
```

#### Monotonic Stack: O que é?

```
Monotonic Stack é uma ESTRUTURA DE DADOS (não é uma propriedade de função!)
Mantém elementos em ordem CRESCENTE ou DECRESCENTE
Usando: Deque ou Stack com pop() estratégico

Exemplo:
  Input:  [73, 74, 75, 71, 69, 72, 76, 73]
  Problema: Daily Temperatures - próxima temperatura MAIOR
  
  Stack (monotonic decreasing):
    [73]           → Stack vazio, push
    [73, 74]       → 74 > 73, pop 73, encontra resposta! push 74
    [73, 74, 75]   → 75 > 74, pop 74, push 75
    [73, 74, 75, 71] → 71 < 75, push (sem pop)
    ...
```

#### GATILHOS Monotonic Stack:

```
✅ "Próximo elemento MAIOR/MENOR"
✅ "Elemento anterior MAIOR/MENOR"
✅ "Número de dias até temperatura maior"
✅ "Elemento com maior valor à direita/esquerda"
✅ "Remover k dígitos para fazer número menor"
✅ "Largest Rectangle in Histogram"
✅ "Trapping Rain Water"

Padrão: Precisa encontrar padrões de vizinhança/relação entre elementos
        Não é otimização com busca (então NÃO é Binary Search)
        
Complexidade: O(n) - cada elemento entra/sai da stack UMA VEZ
```

#### Comparação: Monotônica vs Monotonic Stack

```
┌──────────────────────────────┬──────────────────────┬──────────────────────┐
│ Aspecto                      │ MONOTÔNICA (Binary)  │ MONOTONIC STACK      │
├──────────────────────────────┼──────────────────────┼──────────────────────┤
│ O que é                      │ Propriedade de função│ Estrutura de dados   │
│ Pergunta típica              │ "Mínimo X tal que"   │ "Próximo X MAIOR"    │
│ Estrutura                    │ Espaço de busca      │ Stack/Deque          │
│ Algoritmo                    │ Binary Search        │ Linear scan com pop()│
│ Complexidade                 │ O(log n) + O(n)      │ O(n)                 │
│ Exemplo                      │ Koko Bananas         │ Daily Temperatures   │
│ Usa comparação mid com cond? │ SIM                  │ NÃO                  │
│ Precisa manter ordem?        │ NÃO (função vale)    │ SIM (stack ordem)    │
└──────────────────────────────┴──────────────────────┴──────────────────────┘
```

#### Exemplo: Monotonic Stack

```python
# Daily Temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
# Output: Dias até próxima temperatura MAIOR

def dailyTemperatures(temps):
    result = [0] * len(temps)
    stack = []  # Vai guardar ÍNDICES, mantendo temperaturas em ordem DECRESCENTE
    
    for i, temp in enumerate(temps):
        # Enquanto stack não vazio E temperatura atual > topo do stack
        while stack and temp > temps[stack[-1]]:
            j = stack.pop()
            result[j] = i - j  # Encontrou! A diferença é a resposta
        
        stack.append(i)
    
    return result

# Trace:
# temps = [73, 74, 75, 71, 69, 72, 76, 73]
# 
# i=0, temp=73: stack=[] → push(0) → stack=[0]
# i=1, temp=74: 74 > 73? SIM! pop(0), result[0]=1-0=1, push(1) → stack=[1]
# i=2, temp=75: 75 > 74? SIM! pop(1), result[1]=2-1=1, push(2) → stack=[2]
# i=3, temp=71: 71 > 75? NÃO → push(3) → stack=[2,3]
# i=4, temp=69: 69 > 71? NÃO → push(4) → stack=[2,3,4]
# i=5, temp=72: 72 > 69? SIM! pop(4), result[4]=5-4=1
#               72 > 71? SIM! pop(3), result[3]=5-3=2
#               72 > 75? NÃO → push(5) → stack=[2,5]
# i=6, temp=76: 76 > 72? SIM! pop(5), result[5]=6-5=1
#               76 > 75? SIM! pop(2), result[2]=6-2=4, push(6) → stack=[6]
# i=7, temp=73: 73 > 76? NÃO → push(7) → stack=[6,7]
#
# result = [1, 1, 4, 2, 1, 1, 0, 0]
```

---

### 5. **Quando reconhecer Greedy?**

```
GATILHOS GREEDY:
✅ Problema de otimização (min/max)
✅ Escolha LOCAL ótima leva a ótimo GLOBAL
✅ Não há subestrutura ótima ou é óbvio

AVISO: Greedy nem sempre funciona!
❌ Coin Change com [1, 3, 4] e valor 6:
   Greedy: 4 + 1 + 1 = 3 moedas ❌
   Ótima: 3 + 3 = 2 moedas ✅

Validação Greedy:
1. Prove que escolha local é ótima (prova matemática)
2. OU teste exaustivamente com pequenos exemplos
3. OU use DP se não tiver certeza
```

---

## 📊 Exemplos do Repositório

### Jump Game (Greedy)

**SPEC:**
- Input: `nums: List[int]` (alcance máximo de cada posição)
- Output: `bool` (consegue chegar ao final?)
- Edge: `[]`, `[0]`, `[2,3,1,1,4]`
- Propriedade: Subestrutura ótima? SIM (pode alcançar i ⟺ pode alcançar j < i e j+nums[j] >= i)

**PLAN:**
- Força bruta: DFS all paths → O(2^n) ❌
- DP: `dp[i] = True se conseguir alcançar i`  → O(n²) ✅
- Greedy: `max_reach` track → O(n) ✅✅ **MELHOR**

**CÓDIGO:**
```python
def canJump(nums: List[int]) -> bool:
    """Greedy: acompanha máximo alcance."""
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False  # Não consegue alcançar posição i
        max_reach = max(max_reach, i + nums[i])
    return True

# Tests
assert canJump([2, 3, 1, 1, 4]) == True   # Consegue
assert canJump([3, 2, 1, 0, 4]) == False  # Cai no 0
assert canJump([0]) == True               # Já no final
assert canJump([2, 0, 0]) == True         # Pode alcançar
print("✓ Jump Game I Passed")
```

Escolha: **Greedy** porque propriedade especial: monotonicidade no alcance.

---

### Jump Game II (BFS - Nível a Nível)

**SPEC:**
- Input: `nums: List[int]` (alcance máximo de cada posição)
- Output: `int` (número MÍNIMO de jumps para chegar ao final)
- Restrição: Sempre consegue chegar (dados garantem)
- Propriedade: **Níveis** (cada jump é 1 nível)

**PLAN:**
- Força bruta: DFS explorando todos os jumps → O(2^n) ❌
- DP: `dp[i] = min jumps para alcançar i` → O(n²) ✅
- BFS: Processa nível a nível, contabiliza jumps → O(n) ✅✅ **MELHOR**

**Intuição BFS:**
```
Cada iteração processa 1 nível de BFS
Quando termina de processar um nível, jumps += 1
```

**CÓDIGO:**
```python
def jump(nums: List[int]) -> int:
    """BFS nível a nível: cada nível = 1 jump."""
    jumps = 0
    current_end = 0      # Fim do nível atual
    farthest = 0         # Máximo alcançado
    
    for i in range(len(nums) - 1):  # Não precisa processar último
        farthest = max(farthest, i + nums[i])
        
        # Terminou este nível? (i == current_end)
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps

# Tests
assert jump([2, 3, 1, 1, 4]) == 2     # [0,1,4] = 2 jumps
assert jump([2, 3, 0, 1, 4]) == 2     # [0,1,4] = 2 jumps  
assert jump([1, 1, 1, 0]) == 3        # [0,1,2,3] = 3 jumps
assert jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2  # [0, ...] = 2
print("✓ Jump Game II Passed")
```

**Trade-off:**
- DP O(n²) é correto mas redundo
- BFS O(n) é natural: simula os jumps como níveis do grafo

---

### Jump Game III (DFS/BFS com Ciclos)

**SPEC:**
- Input: `arr: List[int]` (array), `start: int` (posição inicial)
- Output: `bool` (consegue alcançar 0?)
- Restrição: **Pode pular PARA FRENTE E PARA TRÁS** (pode ter ciclos!)
- Edge: `[4,2,3,0,3,1,2]`, start=5

**PLAN:**
- DFS sem visited: Ciclo infinito! ❌
- DFS com visited: Marca visitados, evita ciclos → O(n) ✅✅ **MELHOR**
- BFS com visited: Similar, também funciona

**CÓDIGO - DFS Version:**
```python
def canReach(arr: List[int], start: int) -> bool:
    """DFS com visited set: evita ciclos infinitos."""
    visited = set()
    
    def dfs(i):
        # Validação
        if i < 0 or i >= len(arr) or i in visited:
            return False
        
        # Chegou no 0!
        if arr[i] == 0:
            return True
        
        # Marca como visitado (ANTES de explorar filhos)
        visited.add(i)
        
        # Pode pular FRENTE E TRÁS
        return dfs(i + arr[i]) or dfs(i - arr[i])
    
    return dfs(start)

# Tests
assert canReach([4, 2, 3, 0, 3, 1, 2], 5) == True   # 5→1→4→3→0
assert canReach([3, 0, 2, 1, 2], 2) == False        # Não consegue
assert canReach([0], 0) == True                      # Já no 0
assert canReach([1, 0], 1) == True                   # 1→0
print("✓ Jump Game III (DFS) Passed")
```

**CÓDIGO - BFS Version:**
```python
from collections import deque

def canReach_BFS(arr: List[int], start: int) -> bool:
    """BFS com visited set: nível a nível."""
    visited = set([start])
    queue = deque([start])
    
    while queue:
        i = queue.popleft()
        
        if arr[i] == 0:
            return True
        
        # Explore vizinhos (frente e trás)
        for next_i in [i + arr[i], i - arr[i]]:
            if 0 <= next_i < len(arr) and next_i not in visited:
                visited.add(next_i)
                queue.append(next_i)
    
    return False

# Tests (mesmos)
assert canReach_BFS([4, 2, 3, 0, 3, 1, 2], 5) == True
print("✓ Jump Game III (BFS) Passed")
```

**Comparação Jump Game I/II/III:**
| Problema | Direção | Ciclos? | Padrão | Complexidade |
|----------|---------|---------|--------|--------------|
| Jump I | Frente | Não | Greedy | O(n) |
| Jump II | Frente | Não | BFS | O(n) |
| Jump III | Frente + Trás | SIM | DFS/BFS+visited | O(n) |



---

### Koko Eating Bananas (Binary Search)

**SPEC:**
- Input: `piles: List[int]`, `h: int`
- Output: `int` (mínimo velocidade)
- Propriedade: **Monotonicidade** ✅ (se k funciona, k+1 funciona)

**PLAN:**
- Search space: `[1, max(piles)]`
- Binary Search encontra primeiro k onde `hours_needed(k) <= h`

**Trade-off:**
- Brute force: `for k in range(1, max(piles))` → O(n · max) ❌
- Binary search → O(n · log(max)) ✅✅ **MELHOR**

**⚠️ IMPORTANTE: Leia a seção "TASKS" abaixo para entender COMPLETAMENTE!**

---

### N-Queens (Backtracking)

**SPEC:**
- Input: `n: int` (tamanho do tabuleiro)
- Output: `List[List[str]]` (todas as soluções)
- Precisa: TODAS as soluções ✅

**PLAN:**
- Força bruta: Tentar todas as colocações de N rainhas → O(N!) ❌ (sem pruning)
- Backtracking: Prunar posições inválidas → O(N!) ✅✅ (com pruning)

**Trade-off:**
- DP não aplica (sem subestrutura ótima)
- BFS/DFS não usa bem (problema combinatório)
- **Backtracking** é natural

**CÓDIGO:**
```python
def solveNQueens(n: int) -> List[List[str]]:
    """Backtracking: coloca rainhas linha por linha com pruning."""
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()
    # diag1: i - j (mesma anti-diagonal)
    # diag2: i + j (mesma diagonal)
    
    def backtrack(row):
        # Terminou: colocou n rainhas
        if row == n:
            result.append([''.join(line) for line in board])
            return
        
        # Tenta colocar rainha em cada coluna desta linha
        for col in range(n):
            # Validação: não tem rainha nesta:
            # - coluna
            # - diagonal (i - j)
            # - anti-diagonal (i + j)
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Poda: posição inválida
            
            # Coloca rainha
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            # Recursão: próxima linha
            backtrack(row + 1)
            
            # BACKTRACK: desfaz colocação
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0)
    return result

# Tests
result_4 = solveNQueens(4)
assert len(result_4) == 2          # 4-Queens tem 2 soluções
assert all(len(sol) == 4 for sol in result_4)

result_1 = solveNQueens(1)
assert len(result_1) == 1          # 1-Queens tem 1 solução
assert result_1[0][0] == "Q"

print("✓ N-Queens Passed")
```

**Complexidade:**
- Time: O(N!) - no pior caso explora todas as permutações
         Mas com pruning, muito mais rápido na prática
- Space: O(N) - recursion stack depth + sets

---

### Container With Most Water (Two Pointers)

**SPEC:**
- Input: `heights: List[int]` (altura de cada barra vertical)
- Output: `int` (máxima área de água)
- Edge: `[]`, `[1, 1]`, alturas podem ser 0
- Propriedade: **Greedy + contraste** (duas pontas convergem)

**PLAN:**
- Força bruta: Todos os pares (i, j) → O(n²) ❌
- Two Pointers: Começa nas extremidades, move o menor → O(n) ✅✅ **MELHOR**

**Intuição Greedy:**
```
Área = min(height[left], height[right]) × (right - left)

Se move o MAIOR → distância diminui, altura não aumenta muito
Se move o MENOR → chance de encontrar altura maior (área cresce)
```

**CÓDIGO:**
```python
def maxArea(heights: List[int]) -> int:
    """Two Pointers: começa nas extremidades, move o menor."""
    left, right = 0, len(heights) - 1
    max_area = 0
    
    while left < right:
        # Calcula área atual
        width = right - left
        current_area = min(heights[left], heights[right]) * width
        max_area = max(max_area, current_area)
        
        # Move o ponteiro da barra MENOR
        # (esperança: encontrar barra maior)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Tests
assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49   # Entre índices 1 e 8
assert maxArea([1, 1]) == 1                          # Mínimo
assert maxArea([4, 3, 2, 1, 4]) == 16                # Extremidades
assert maxArea([2, 3, 4, 5, 18, 17, 6]) == 17        # Meio
print("✓ Container With Most Water Passed")
```

**Trade-off:**
- Força bruta O(n²) é correto mas lento
- Two Pointers O(n) explora greedy: mover o menor sempre é ótimo para próxima iteração

**Complexidade:**
- Time: O(n) - dois ponteiros passam uma vez
- Space: O(1) - apenas variáveis

---

### Longest Repeating Character Replacement (Sliding Window)

**SPEC:**
- Input: `s: str`, `k: int` (máximo de replacements)
- Output: `int` (máximo length de substring com mesmo caractere)
- Propriedade: **Janela variável** (expandir/contrair)

**PLAN:**
- Força bruta: Todas as substrings, contar replacements → O(n³) ❌
- Sliding Window: Manter janela onde (len - max_freq) <= k → O(n) ✅✅ **MELHOR**

**Lógica:**
```
window_len = right - left + 1
chars_to_replace = window_len - max_frequency_in_window

Se chars_to_replace <= k:  janela válida, expanda
Senão:                     contraia (move left)
```

**CÓDIGO:**
```python
def characterReplacement(s: str, k: int) -> int:
    """Sliding Window: mantém janela com até k replacements."""
    from collections import Counter
    
    left = 0
    char_count = Counter()
    max_freq = 0
    max_length = 0
    
    for right in range(len(s)):
        # Expande janela
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])
        
        # Valida janela
        window_len = right - left + 1
        chars_to_replace = window_len - max_freq
        
        # Se precisa trocar mais de k caracteres, contrai
        if chars_to_replace > k:
            char_count[s[left]] -= 1
            left += 1
        
        # Atualiza resposta
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Tests
assert characterReplacement("ABAB", 2) == 4      # Troca 2 B's → "AAAA"
assert characterReplacement("ABBB", 2) == 4      # Troca 2 A's → "BBBB"
assert characterReplacement("AABAB", 1) == 3     # "AAA" ou "BBB"
assert characterReplacement("A", 0) == 1         # Sem replacements
print("✓ Longest Repeating Character Replacement Passed")
```

**Trade-off:**
- DP com memoization O(n·26) é correto mas overkill
- Sliding Window O(n) com hash map é natural e elegante

**Complexidade:**
- Time: O(n) - cada caractere processado uma vez
- Space: O(26) = O(1) - no máximo 26 letras

---

### Word Search / Trie (DFS Backtracking)

**SPEC:**
- Input: `board: List[List[str]]`, `word: str`
- Output: `bool` (palavra existe no tabuleiro?)
- Restrição: Pode se mover up/down/left/right, cada célula usa apenas 1x
- Propriedade: **Grafo com backtracking** (explora caminhos, marca visitado)

**PLAN:**
- BFS/DFS com visited set: Marca célula visitada durante busca
- Backtracking: Unmark ao retornar (permite reexploração em outros caminhos)

**Lógica DFS:**
```python
def dfs(i, j, idx):
    # Base: encontrou toda a palavra
    if idx == len(word):
        return True
    
    # Validação
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return False
    if board[i][j] != word[idx] or (i, j) in visited:
        return False
    
    # Backtrack
    visited.add((i, j))
    
    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
        if dfs(i+di, j+dj, idx+1):
            return True
    
    visited.remove((i, j))  # ← CRUCIAL: remove ao retornar
    return False
```

**CÓDIGO:**
```python
def exist(board: List[List[str]], word: str) -> bool:
    """DFS com backtracking: marca visitado, depois desmarcar."""
    if not board or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    visited = set()
    
    def dfs(i, j, idx):
        # Terminou a palavra?
        if idx == len(word):
            return True
        
        # Validação de limites
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        
        # Validação de caractere e visitado
        if board[i][j] != word[idx] or (i, j) in visited:
            return False
        
        # MARCA COMO VISITADO
        visited.add((i, j))
        
        # Explora 4 direções
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            if dfs(i + di, j + dj, idx + 1):
                # ENCONTROU! Pode retornar sem limpar
                return True
        
        # BACKTRACK: remove do visitado para outras explorações
        visited.remove((i, j))
        return False
    
    # Tenta começar de cada posição
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    
    return False

# Tests
board1 = [["O", "A", "A"], ["A", "A", "A"], ["A", "A", "O"]]
assert exist(board1, "AAA") == True           # Múltiplos caminhos

board2 = [["A", "B"], ["A", "A"]]
assert exist(board2, "AAB") == True           # Frente e trás

board3 = [["A", "B"], ["C", "D"]]
assert exist(board3, "ABCD") == False         # Não existe

board4 = [["A"]]
assert exist(board4, "A") == True             # Célula única

print("✓ Word Search Passed")
```

**Trade-off:**
- BFS puro não funciona (precisa rastrear caminho + backtrack)
- DFS com backtracking é natural para esse tipo de exploração

**Complexidade:**
- Time: O(n·m·4^L) onde n=rows, m=cols, L=len(word)
         4^L porque cada célula pode explorar 4 direções no pior caso
- Space: O(L) - recursion stack (backtracking depth)

---

### Union-Find / DSU (Disjoint Set Union)

**SPEC:**
- Input: `edges: List[List[int]]`, `n: int` (nós)
- Output: `int` (número de componentes conectadas) ou `bool` (tem ciclo?)
- Propriedade: **Componentes do grafo não-dirigido**

**PLAN:**
- DFS/BFS clássico: Mark visited → O(V + E) ✅✅ (simples)
- Union-Find (DSU): Merge componentes durante construção → O(V + E·α(V)) ✅✅ (elegante)

**Quando usar DSU?**
```
✅ Múltiplas queries de conectividade
✅ Detectar ciclos
✅ Mínimum Spanning Tree (Kruskal)
✅ Grafo dinâmico (adiciona arestas incrementalmente)

❌ Precisa do caminho exato → use DFS/BFS
❌ Grafo direcionado com ordem específica → use Topological Sort
```

**CÓDIGO:**
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Encontra raiz com path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Une dois componentes. Retorna False se já estavam unidos (ciclo!)."""
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return False  # Já no mesmo componente (ciclo detectado!)
        
        # Union by rank: árvore menor aponta para maior
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True  # Nova conexão


def countComponents(n: int, edges: List[List[int]]) -> int:
    """Conta componentes conectadas usando DSU."""
    dsu = DSU(n)
    
    for u, v in edges:
        dsu.union(u, v)
    
    # Conta quantas raízes únicas existem
    return len(set(dsu.find(i) for i in range(n)))


def hasRedundantConnection(edges: List[List[int]]) -> List[int]:
    """Detecta ciclo (aresta redundante) em grafo não-dirigido."""
    dsu = DSU(len(edges) + 1)
    
    for u, v in edges:
        # Se não conseguir unir, é porque já estavam conectados (ciclo!)
        if not dsu.union(u, v):
            return [u, v]
    
    return []

# Tests
# Exemplo 1: 3 componentes conectadas
edges1 = [[0, 1], [1, 2], [4, 5]]
assert countComponents(6, edges1) == 3  # {0,1,2}, {3}, {4,5}

# Exemplo 2: Detecta ciclo
edges2 = [[1, 2], [1, 3], [2, 3]]
assert hasRedundantConnection(edges2) == [2, 3]  # Ciclo: 1-2-3-1

# Exemplo 3: Sem ciclo
edges3 = [[1, 2], [2, 3], [3, 4]]
assert hasRedundantConnection(edges3) == []

print("✓ Union-Find / DSU Passed")
```

**Trade-off:**
- DFS: Mais intuitivo, mais simples para 1-2 queries
- DSU: Melhor para múltiplas queries, mais elegante em Union-Find específico

**Complexidade:**
- find(): O(α(n)) ≈ O(1) com path compression
- union(): O(α(n)) ≈ O(1) com union by rank
- Total: O(E·α(n)) ≈ O(E)

---

## 🛠️ Checklist de Implementação (TASKS)

Antes de começar a código:

```
ESTRUTURA:
□ Função assinada com tipos (Python 3.9+)
□ Docstring com descrição, exemplo, complexidade
□ Função auxiliar se necessário (helper function)

CÓDIGO:
□ Variáveis com nomes descritivos
□ Comentários explicando LÓGICA, não óbvio
□ Edge cases tratados ([], None, etc)
□ Sem magic numbers (use constantes nomeadas)

VALIDAÇÃO:
□ Casos normais testados
□ Edge cases testados
□ Stress test (grande entrada)
□ Tracear manualmente um exemplo

COMPLEXIDADE:
□ Time complexity declarado
□ Space complexity declarado
□ Explicação de por que é essa complexidade
```

### Template TASKS

```python
from typing import List

def solve_problem(nums: List[int]) -> int:
    """
    Descrição clara do que faz.
    
    Args:
        nums: Lista de inteiros, 1 <= n <= 10^4
        
    Returns:
        int: Resultado da operação
        
    Time:  O(n log n) - sorting + binary search
    Space: O(1) - only constant extra space
    
    Examples:
        >>> solve_problem([3, 6, 7, 11])
        4
    """
    # SPEC check: validate input
    if not nums:
        return 0
    
    # PLAN: implement chosen pattern
    result = 0
    # ... main logic ...
    
    # TASKS: return and validate
    return result

# ─── Tests ───────────────────────────────────────
if __name__ == "__main__":
    # Normal cases
    assert solve_problem([3, 6, 7, 11]) == 4
    
    # Edge cases
    assert solve_problem([]) == 0
    assert solve_problem([1]) == 1
    
    # Stress (large input)
    assert solve_problem(list(range(1000))) >= 0
    
    print("All tests passed ✓")
```

---

## 📚 Referências Rápidas

### Complexidade Assintótica

```
O(1)        ← Constant (best)
O(log n)    ← Logarithmic (binary search)
O(n)        ← Linear (simple loop)
O(n log n)  ← Linearithmic (sorting, merge)
O(n²)       ← Quadratic (nested loops, DP 2D)
O(n³)       ← Cubic (rare, avoid)
O(2^n)      ← Exponential (backtracking, brute force)
O(n!)       ← Factorial (permutations, very bad)
```

### Space Complexity

```
O(1)        ← Constant, no extra space
O(log n)    ← Recursion stack depth
O(n)        ← Array/Hash storage
O(n²)       ← 2D DP table
```

---

## 🎓 Resumo: Não Decore, Escolha!

```
┌─────────────────────────────────────────────────────────┐
│ REGRA DE OURO PARA NÃO DECORAR:                         │
│                                                          │
│ 1. SPEC: Entenda TODAS as constraints do problema       │
│ 2. PLAN: Reconheça qual PROPRIEDADE o problema tem      │
│ 3. TASKS: Implemente a solução que EXPLORA essa prop.   │
│                                                          │
│ Exemplo: Problema tem subestrutura ótima?               │
│          → DP é natural (não decoração)                 │
│                                                          │
│ Exemplo: Array é sorted?                                │
│          → Binary Search é natural (não decoração)      │
└─────────────────────────────────────────────────────────┘
```

---

## 🔗 Exemplo Completo: Koko Eating Bananas

### SPEC

**Problema:** Koko adora bananas. Há `n` pilhas. Cada pilha `i` tem `piles[i]` bananas. Ela tem `h` horas. A cada hora, ela escolhe UMA pilha e come `k` bananas daquela pilha. Se a pilha tiver menos de `k`, ela come tudo. Qual o **mínimo `k`** para comer todas as bananas em `h` horas?

- **Input:** `piles: List[int]` (bananas por pilha), `h: int` (horas disponíveis)
- **Output:** `int` (mínima velocidade em bananas/hora)
- **Edge:** `[]`, `[1]`, `[10^9]`, `h = 1` (precisa comer tudo em 1 hora!)
- **Propriedade CRÍTICA:** **Monotonicidade** ✅ se consegue com `k=5`, consegue com `k=6` também!

### PLAN

#### 🎯 Reconhecer o Padrão

```
1. Preciso OTIMIZAR (encontrar mínimo)
2. A função objetivo é MONOTÔNICA?
   
   hours_needed(k=1)  = 4+6+7+11 = 28 horas  ← lento
   hours_needed(k=2)  = 2+3+4+6  = 15 horas  ← mais rápido
   hours_needed(k=3)  = 2+2+3+4  = 11 horas  ← ainda melhor
   hours_needed(k=4)  = 1+2+2+3  = 8 horas   ← ótimo! (k=4)
   hours_needed(k=5)  = 1+2+2+3  = 8 horas   ← mesmo que k=4
   
   Padrão: CONFORME k AUMENTA → hours_needed(k) DIMINUI ✓
           (Função é DECRESCENTE = MONOTÔNICA!)
   
3. Logo: Binary Search consegue encontrar o mínimo k!
```

#### 📊 Por quê `ceil(pile / k)` é correto?

```
Pilha com 11 bananas, velocidade k:

k=1: 11 horas (1 banana/hora × 11 bananas)
k=2: ceil(11/2) = ceil(5.5) = 6 horas
     (Hora 1-5: 2 ban/hora = 10 bananas)
     (Hora 6: 1 banana restante, ainda conta 1 hora!)
k=3: ceil(11/3) = ceil(3.67) = 4 horas
     (Hora 1-3: 3 ban/hora = 9 bananas)
     (Hora 4: 2 bananas restantes, ainda conta 1 hora!)
k=4: ceil(11/4) = ceil(2.75) = 3 horas
     
⚠️ NUNCA FAÇA: 11 / 4 = 2.75 horas (ERRADO!)
   A gente precisa ARREDONDAR PARA CIMA porque:
   - Se sobrar nem que seja 1 banana, precisa de 1 hora inteira!
```

#### ✅ Fórmula `ceil(a/b)` em Python

```python
# ❌ ERRADO - Float impreciso para números grandes
import math
horas = math.ceil(11 / 4)  # Funciona, mas perde precisão em 10^9

# ✅ CERTO - Integer division sem float
horas = (11 + 4 - 1) // 4  # = 14 // 4 = 3
horas = (pile + k - 1) // k  # Fórmula universal!

# Prova: Por que (a + b - 1) // b funciona?
# Caso 1: a % b == 0 (divisão exata)
#   (12 + 3 - 1) // 3 = 14 // 3 = 4 ✓ (correto: 12 / 3 = 4)
#
# Caso 2: a % b != 0 (tem resto)
#   (11 + 3 - 1) // 3 = 13 // 3 = 4 ✓ (correto: ceil(11/3) = 4)
```

#### 🔍 Template: Binary Search on Answer

```
Objetivo: Encontrar MÍNIMO k onde hours_needed(k) <= h

min_speed = 1           ← velocidade mínima possível
max_speed = max(piles)  ← velocidade máxima (come uma pilha por hora)

Buscar a resposta como se fosse um número em um range!
[1, 2, 3, 4, 5, 6, ..., max_piles]
             ↑ resposta está aqui em algum lugar
```

### TASKS

```python
from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    Encontra mínima velocidade para comer todas as bananas em h horas.
    
    Estratégia: Binary Search na velocidade (1 até max(piles))
    
    Args:
        piles: Lista de inteiros, n pilhas
        h: Inteiro, horas disponíveis
    
    Returns:
        int: Mínima velocidade em bananas/hora
    
    Time:  O(n · log(max(piles)))
           - log(max) iterações de binary search
           - n para calcular horas_needed a cada iteração
    
    Space: O(1)
    
    Example:
        >>> minEatingSpeed([3, 6, 7, 11], 8)
        4  # Com velocidade 4: 1+2+2+3 = 8 horas (perfeit!)
    """
    
    def hours_needed(speed: int) -> int:
        """
        Calcula TOTAL de horas necessárias para comer todas as pilhas
        com uma velocidade k.
        
        Para cada pilha, calcula: ceil(pile / speed) = (pile + speed - 1) // speed
        """
        total_hours = 0
        for pile in piles:
            # Horas para essa pilha: arredonda para CIMA
            # (pile + speed - 1) // speed é equivalente a ceil(pile / speed)
            hours_for_this_pile = (pile + speed - 1) // speed
            total_hours += hours_for_this_pile
        return total_hours
    
    # ─── Binary Search ───────────────────────────────
    left = 1                  # Velocidade MÍNIMA
    right = max(piles)        # Velocidade MÁXIMA
    
    # Invariante: resposta está em [left, right]
    while left < right:
        mid = (left + right) // 2
        
        # Pergunta: Com velocidade mid, consigo terminar em h horas?
        if hours_needed(mid) <= h:
            # SIM! Então posso tentar MAIS DEVAGAR
            # A resposta está em [left, mid]
            right = mid
        else:
            # NÃO! Preciso comer MAIS RÁPIDO
            # A resposta está em [mid+1, right]
            left = mid + 1
    
    # Agora left == right e ambos apontam para a resposta!
    return left


# ─── TESTS ───────────────────────────────────────────
if __name__ == "__main__":
    # Exemplo da descrição
    print("Test 1: piles=[3,6,7,11], h=8")
    result = minEatingSpeed([3, 6, 7, 11], 8)
    print(f"  Velocidade mínima: {result}")
    print(f"  Horas needed: {(3 + result - 1) // result + (6 + result - 1) // result + (7 + result - 1) // result + (11 + result - 1) // result}")
    assert result == 4, "Esperava 4!"
    
    # Edge: apenas 1 pilha
    print("\nTest 2: piles=[1000000000], h=2")
    result = minEatingSpeed([1000000000], 2)
    print(f"  Velocidade mínima: {result}")
    assert result == 500000000, f"Esperava 500000000, got {result}!"
    
    # Edge: velocidade máxima necessária
    print("\nTest 3: piles=[1,1,1,1], h=4")
    result = minEatingSpeed([1, 1, 1, 1], 4)
    print(f"  Velocidade mínima: {result}")
    assert result == 1, "Esperava 1!"
    
    # Edge: uma hora, comer tudo em 1 hora
    print("\nTest 4: piles=[312884132], h=968709470")
    result = minEatingSpeed([312884132], 968709470)
    print(f"  Velocidade mínima: {result}")
    assert result == 1, "Esperava 1!"
    
    print("\n✓ Todos os testes passaram!")
```

#### 🧮 Visualização Passo a Passo

```
Entrada: piles = [3, 6, 7, 11], h = 8

Binary Search Loop:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Iteração 1:
  left=1, right=11
  mid = (1+11)//2 = 6
  hours_needed(6) = ceil(3/6) + ceil(6/6) + ceil(7/6) + ceil(11/6)
                  = 1 + 1 + 2 + 2 = 6 <= 8? SIM!
  → Podemos ir mais devagar: right = 6

Iteração 2:
  left=1, right=6
  mid = (1+6)//2 = 3
  hours_needed(3) = ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
                  = 1 + 2 + 3 + 4 = 10 <= 8? NÃO!
  → Precisa ser mais rápido: left = 4

Iteração 3:
  left=4, right=6
  mid = (4+6)//2 = 5
  hours_needed(5) = ceil(3/5) + ceil(6/5) + ceil(7/5) + ceil(11/5)
                  = 1 + 2 + 2 + 3 = 8 <= 8? SIM!
  → Podemos ir mais devagar: right = 5

Iteração 4:
  left=4, right=5
  mid = (4+5)//2 = 4
  hours_needed(4) = ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4)
                  = 1 + 2 + 2 + 3 = 8 <= 8? SIM!
  → Podemos ir mais devagar: right = 4

Iteração 5:
  left=4, right=4
  left == right → PARE!

Resposta: 4 ✓
```

#### 📈 Gráfico da Monotonicidade

```
Hours Needed vs Speed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Horas ↑
  28  |●  (k=1: lento)
  25  |
  20  | ●   (k=2: mais rápido)
  15  |
  10  |  ●   (k=3)
   8  |   ● ●●● (k=4,5,6: resposta k=4)
      |        ●●●● (k=7+: ainda mais rápido, mas k=4 é mínimo!)
      └─────────────────────────────→ k (velocidade)
        1  2  3  4  5  6  7  8
        
Propriedade: SEMPRE DECRESCENTE (monotônico!)
Logo: Binary Search funciona! ✓
```

---

### Daily Temperatures (Monotonic Stack)

**SPEC:**
- Input: `temperatures: List[int]` (temperaturas diárias)
- Output: `List[int]` (dias até próxima temperatura MAIOR)
- Edge: `[1]`, `[1,1,1,1]` (sem próxima maior), `[30,40,50,60]` (já crescente)
- Propriedade: **Vizinhança/Padrão** (próximo elemento maior)

**PLAN:**
- Força bruta: Para cada dia, procura adiante → O(n²) ❌
- Monotonic Stack: Mantém stack de índices em ordem decrescente → O(n) ✅✅ **MELHOR**

**Intuição:**
```
Quando temperatura AUMENTA, sabemos a resposta para dias anteriores!

Exemplo: [73, 74, 75, 71, 69, 72, 76, 73]

dia 0 (73): Stack vazio, empilha
dia 1 (74): 74 > 73? SIM! Pop 73, resposta[0] = 1-0 = 1
            Empilha 74
dia 2 (75): 75 > 74? SIM! Pop 74, resposta[1] = 2-1 = 1
            Empilha 75
dia 5 (72): 72 > 71? SIM! Pop 71, resposta[3] = 5-3 = 2
            72 > 75? NÃO, empilha 72
dia 6 (76): 76 > 72? SIM! Pop 72, resposta[5] = 6-5 = 1
            76 > 75? SIM! Pop 75, resposta[2] = 6-2 = 4
            Empilha 76

Resultado: [1, 1, 4, 2, 1, 1, 0, 0] ✓
```

**CÓDIGO:**
```python
def dailyTemperatures(temps: List[int]) -> List[int]:
    """Monotonic Stack (decrescente): mantém índices de temperaturas."""
    n = len(temps)
    result = [0] * n
    stack = []  # Guarda ÍNDICES, mantendo temperaturas em ordem DECRESCENTE
    
    for i, temp in enumerate(temps):
        # Enquanto temperatura atual > topo do stack
        while stack and temp > temps[stack[-1]]:
            j = stack.pop()
            result[j] = i - j  # Encontrou a resposta!
        
        # Empilha índice atual
        stack.append(i)
    
    return result

# Tests
assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]
assert dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]) == [8, 1, 5, 3, 8, 4, 3, 2, 0, 0]

print("✓ Daily Temperatures Passed")
```

**Trade-off:**
- Força bruta O(n²) é correto mas lento
- Monotonic Stack O(n) é elegante: cada elemento entra/sai da stack UMA VEZ

**Complexidade:**
- Time: O(n) - cada índice entra e sai UMA VEZ
- Space: O(n) - stack pode ter até n elementos no pior caso

---

### Kahn's Algorithm (Topological Sort)

**SPEC:**
- Input: `edges: List[List[int]]`, `n: int` (DAG - Directed Acyclic Graph)
- Output: `List[int]` (ordem topológica) ou detectar ciclo
- Propriedade: **Dependências** - se há ciclo, retorna []
- Exemplo: Course Prerequisites, Task Scheduling

**PLAN:**
- DFS com stack: Explorar profundidade → O(V+E) ✅
- Kahn's BFS: In-degree + queue → O(V+E) ✅✅ **MELHOR para detectar ciclos**

**Intuição:**
```
1. Calcula in-degree (quantas arestas entram) de cada nó
2. Começa com nós que têm in-degree = 0 (sem dependências)
3. Processa nó: adiciona à resposta, reduz in-degree dos vizinhos
4. Se conseguir processar V nós → topológica válida
   Se não → ciclo detectado!
```

**CÓDIGO:**
```python
def canFinish(n: int, edges: List[List[int]]) -> bool:
    """Kahn: detecta ciclo em DAG."""
    # Construir grafo e in-degree
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for course, prereq in edges:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Fila com nós que têm in-degree = 0
    queue = [i for i in range(n) if in_degree[i] == 0]
    count = 0
    
    while queue:
        course = queue.pop(0)
        count += 1
        
        # Reduz in-degree dos vizinhos
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # Se processou todos os cursos, não tem ciclo
    return count == n


def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    """Kahn: retorna ordem topológica ou [] se tem ciclo."""
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = [i for i in range(n) if in_degree[i] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Se não processou todos, tem ciclo
    return result if len(result) == n else []

# Tests
# DAG válido: 0 → 1 → 2
assert canFinish(3, [[1, 0], [2, 1]]) == True

# Ciclo: 0 → 1 → 0
assert canFinish(2, [[1, 0], [0, 1]]) == False

# Sem arestas
assert canFinish(3, []) == True

# Topological sort
result = topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
assert len(result) == 4  # Todos processados

print("✓ Kahn's Algorithm / Topological Sort Passed")
```

**Complexidade:**
- Time: O(V + E) - visita cada nó e aresta uma vez
- Space: O(V + E) - grafo + queue

---

### Dijkstra's Algorithm (Shortest Path)

**SPEC:**
- Input: `graph: List[List[Tuple]]` (grafo com pesos), `start: int`
- Output: `List[int]` (distância mínima de cada nó até start)
- Propriedade: **Grafos ponderados** - sem pesos negativos!
- Padrão: Network Delay Time, Path With Minimum Effort

**PLAN:**
- BFS simples: Não funciona com pesos ❌
- Dijkstra: Greedy com Priority Queue → O((V+E) log V) ✅✅ **MELHOR**

**Intuição:**
```
1. Começa no nó start com distância 0
2. Sempre processa o nó com MENOR distância ainda não visitado
3. Atualiza distâncias dos vizinhos: dist[neighbor] = min(dist[neighbor], dist[current] + weight)
4. Marca como visitado e continua
```

**CÓDIGO:**
```python
import heapq
from typing import List, Tuple

def dijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    """Dijkstra com Priority Queue: menor distância primeiro."""
    # Construir grafo
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Se não-dirigido
    
    # Inicializa distâncias
    dist = [float('inf')] * n
    dist[start] = 0
    visited = set()
    
    # Priority queue: (distância, nó)
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Já visitado
        if u in visited:
            continue
        
        visited.add(u)
        
        # Relaxa arestas
        for v, weight in graph[u]:
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    return dist


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    """Dijkstra: tempo para todos os nós receberem sinal."""
    # Grafo: u → v com weight
    graph = [[] for _ in range(n + 1)]
    for u, v, time in times:
        graph[u].append((v, time))
    
    # Dijkstra do nó k
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    visited = set()
    pq = [(0, k)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        
        visited.add(u)
        
        for v, weight in graph[u]:
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    # Distância máxima (tempo para todos receberem)
    max_time = max(dist[1:n+1])
    return max_time if max_time != float('inf') else -1

# Tests
# Exemplo: Sinal de 1 para 3 nós, k=1
# Edges: 1→2 (1), 1→3 (4), 2→3 (2)
# Path: 1→3 diretamente (4) ou 1→2→3 (3)
assert networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 1) == 4

# Caminho direto
assert networkDelayTime([[1, 2, 1]], 2, 1) == 1

# Múltiplos caminhos
assert networkDelayTime([[1, 2, 1], [1, 3, 4], [2, 3, 2]], 3, 1) == 4

print("✓ Dijkstra's Algorithm Passed")
```

**Complexidade:**
- Time: O((V + E) log V) com Priority Queue
- Space: O(V + E) - grafo + estruturas

---

### Merge Intervals (Interval Pattern)

**SPEC:**
- Input: `intervals: List[List[int]]` (não-ordenados, sobrepostos)
- Output: `List[List[int]]` (intervalos mesclados)
- Propriedade: **Ordenação + Varredura** (sort depois merge)
- Exemplo: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

**PLAN:**
- Força bruta: Comparar todos com todos → O(n²) ❌
- Sort + Merge: Ordena por start, depois varre uma vez → O(n log n) ✅✅ **MELHOR**

**Intuição:**
```
1. Sort intervalos por start
2. Varre: se current.start <= last.end → merge (end = max(end))
   Senão → novo intervalo
```

**CÓDIGO:**
```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    """Merge intervals: sort + varredura."""
    if not intervals:
        return []
    
    # Sort por start (Python sorts por primeiro elemento por padrão)
    intervals.sort()
    
    result = [intervals[0]]
    
    for current in intervals[1:]:
        last = result[-1]
        
        # Sobrepõe? Merge
        if current[0] <= last[1]:
            result[-1] = [last[0], max(last[1], current[1])]
        else:
            # Novo intervalo
            result.append(current)
    
    return result

# Tests
assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
assert merge([[1, 5]]) == [[1, 5]]
assert merge([]) == []
assert merge([[1, 3], [4, 6]]) == [[1, 3], [4, 6]]

print("✓ Merge Intervals Passed")
```

**Complexidade:**
- Time: O(n log n) - sorting é dominante
- Space: O(1) - não conta output

---

### Insert Interval (Interval Pattern Avançado)

**SPEC:**
- Input: `intervals: List[List[int]]` (já ordenados!), `newInterval: List[int]`
- Output: `List[List[int]]` (intervals + newInterval mesclado)
- Propriedade: **Já ordenado** - deve permanecer ordenado
- Tricky: Não pode fazer sort novamente!

**PLAN:**
- Merge simples (sort): O(n log n) ❌ (não eficiente)
- 3-pass: Before + Merge + After → O(n) ✅✅ **MELHOR**

**Intuição:**
```
Pass 1: Adiciona todos intervalos que terminam ANTES do new start
Pass 2: Mescla TODOS que sobrepõem
Pass 3: Adiciona todos que começam DEPOIS do new end
```

**CÓDIGO:**
```python

def insert_clean(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """Insert interval: versão mais limpa."""
    result = []
    new_start, new_end = newInterval
    
    # Adiciona intervals que terminam antes do novo
    i = 0
    while i < len(intervals) and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1
    
    # Mescla todos que sobrepõem
    while i < len(intervals) and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    
    result.append([new_start, new_end])
    
    # Adiciona rest que não sobrepõe
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

# Tests
assert insert_clean([[1, 5]], [2, 3]) == [[1, 5]]  # Dentro
assert insert_clean([[1, 5]], [2, 7]) == [[1, 7]]  # Sobrepõe direita
assert insert_clean([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]  # Antes
assert insert_clean([[1, 2], [3, 5], [6, 7]], [5, 6]) == [[1, 2], [3, 7]]
assert insert_clean([], [5, 7]) == [[5, 7]]  # Vazio

print("✓ Insert Interval Passed")
```

**Complexidade:**
- Time: O(n) - uma ou duas varridas
- Space: O(1) - não conta output

---

### Meeting Rooms II (Interval Pattern com Heap)

**SPEC:**
- Input: `intervals: List[List[int]]` (horários de reuniões)
- Output: `int` (mínimo salas necessárias)
- Padrão: **Evento + Varredura** (início e fim de reunião)
- Tricky: Pode reusar sala se uma termina quando outra começa

**PLAN:**
- Força bruta: Comparar todos com todos → O(n²) ❌
- Sort + Min Heap: Ordena starts, usa heap para tracks fins → O(n log n) ✅✅ **MELHOR**

**Intuição:**
```
1. Sort tudo: [start, "begin"], [end, "end"]
2. Varre: 
   - Início → adiciona sala (heap++)
   - Fim → libera sala (heap--)
3. Máximo tamanho da heap = salas necessárias
```

**CÓDIGO:**
```python
def minMeetingRooms(intervals: List[List[int]]) -> int:
    """Min rooms: sort + min heap para track de saídas."""
    if not intervals:
        return 0
    
    # Cria lista de eventos: (tempo, tipo)
    # tipo: 0 = saída (deve processar primeiro), 1 = entrada
    events = []
    for start, end in intervals:
        events.append((start, 1))  # Início
        events.append((end, 0))    # Fim
    
    # Sort: por tempo, depois por tipo (saída antes de entrada no mesmo tempo)
    events.sort()
    
    rooms_needed = 0
    rooms_in_use = 0
    
    for time, event_type in events:
        if event_type == 1:  # Reunião começa
            rooms_in_use += 1
            rooms_needed = max(rooms_needed, rooms_in_use)
        else:  # Reunião termina
            rooms_in_use -= 1
    
    return rooms_needed


def minMeetingRooms_heap(intervals: List[List[int]]) -> int:
    """Min rooms: heap versão com min-heap de saídas."""
    if not intervals:
        return 0
    
    # Sort por start
    intervals.sort()
    
    # Min-heap: guardar fins das reuniões
    end_times = []
    heapq.heappush(end_times, intervals[0][1])
    
    for start, end in intervals[1:]:
        # Se a reunião anterior terminou, reusar sala
        if end_times[0] <= start:
            heapq.heappop(end_times)
        
        heapq.heappush(end_times, end)
    
    return len(end_times)

# Tests
assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2  # 0-30 + 5-10
assert minMeetingRooms([[7, 10], [2, 4]]) == 1  # Sem overlap
assert minMeetingRooms([[1, 5], [1, 6], [1, 7]]) == 3  # Todas simultâneas
assert minMeetingRooms([]) == 0  # Vazio

print("✓ Meeting Rooms II Passed")
```

**Complexidade:**
- Time: O(n log n) - sorting + heap ops
- Space: O(n) - heap pode ter até n elementos



## 🌐 Padrões Diversos: Referência Rápida

Além dos exemplos detalhados acima, aqui estão outros padrões IMPORTANTES:

### Trie + DFS (String Patterns)

```
GATILHOS: "Prefix", "Word dictionary", "autocomplete"
Exemplo: Implement Trie, Word Search II

Padrão: Build Trie → DFS com backtracking
Complexidade: O(n·m·k) onde n=dict size, m=word len, k=branching
```

### Topological Sort (DAG - Directed Acyclic Graph)

```
GATILHOS: "Dependências", "Task scheduling", "Course prerequisites"
Exemplo: Course Schedule, Task Sequencing

Padrão: Kahn's algorithm (BFS) ou DFS com visited
Complexidade: O(V + E)
```

### Segment Tree / Fenwick Tree (Range Queries)

```
GATILHOS: "Range sum", "Point update", "Mínimo/máximo em range"
Exemplo: Range Sum Query, Count of Smaller Numbers After Self

Padrão: Build tree → Query + Update
Complexidade: O(log n) por operação
```

### Two Pointers (String/Array)

```
GATILHOS: "Duas extremidades", "Contraste", "Remove duplicates"
Exemplo: Container With Most Water, Valid Palindrome, Merge Sorted

Padrão: left=0, right=n-1, move baseado em condição
Complexidade: O(n)
```

### Binary Search (não só em answer)

```
GATILHOS: "Array ordenado", "Buscar posição", "First/Last occurrence"
Exemplo: First Bad Version, Find Minimum in Rotated Array

Padrão: left=0, right=n-1, mid=(left+right)//2
Complexidade: O(log n)
```

### Greedy (com prova!)

```
GATILHOS: "Máximo/mínimo com escolha local"
Exemplo: Jump Game, Interval Scheduling, Gas Station

⚠️ CRÍTICO: Sempre prove ou teste exaustivamente!
Padrão: Escolha local ótima → ótimo global
```

### HashMap/HashSet (Frequency)

```
GATILHOS: "Contagem", "Frequência", "Encontrar duplicatas"
Exemplo: Two Sum, Contains Duplicate, Valid Anagram

Padrão: count[x] += 1 durante iteração
Complexidade: O(n) average, O(n²) worst case (colisões)
```

### Heap / Priority Queue (Top K)

```
GATILHOS: "Top K", "Kth elemento", "Merge K lists"
Exemplo: Kth Largest Element, Top K Frequent Words

Padrão: heappush() / heappop()
Complexidade: O(n log k)
```

### Dynamic Programming (Subproblems)

```
GATILHOS: "Mínimo/máximo", "Contar formas", "É possível?"
Exemplo: Coin Change, House Robber, LIS

Padrão: dp[i] = f(dp[i-1], dp[i-2], ...)
Complexidade: O(n·m) ou O(n²)
```

### Backtracking (All Solutions)

```
GATILHOS: "Todas as combinações", "Todas as permutações", "Puzzles"
Exemplo: N-Queens, Permutations, Sudoku Solver

Padrão: Explore → Prune → Backtrack
Complexidade: O(k·n!) onde k é tamanho da solução
```

---

## 📊 Matriz de Decisão Rápida

```
┌─────────────────────────────────────────────────────────────┐
│ TIPO DE PROBLEMA → PADRÃO SUGERIDO                          │
├─────────────────────────────────────────────────────────────┤
│ Array/String ordenado?                                      │
│  → Binary Search O(log n)                                   │
│                                                              │
│ Precisa de todas as soluções?                               │
│  → Backtracking / DFS O(k·n!)                               │
│                                                              │
│ Otimização com subestrutura ótima?                          │
│  → Dynamic Programming O(n²) ou O(n³)                       │
│                                                              │
│ Próximo elemento MAIOR/MENOR?                               │
│  → Monotonic Stack O(n)                                     │
│                                                              │
│ Grafo com vizinhanças/níveis?                               │
│  → BFS (shortest path) O(V+E)                               │
│  → DFS (conectividade) O(V+E)                               │
│  → Topological Sort (DAG) O(V+E)                            │
│  → DSU (ciclos/componentes) O(α(n))                         │
│                                                              │
│ Substring/subarray com janela?                              │
│  → Sliding Window O(n)                                      │
│  → Two Pointers O(n)                                        │
│                                                              │
│ Contagem/frequência?                                        │
│  → HashMap O(n) average                                     │
│  → Heap para Top K O(n log k)                               │
│                                                              │
│ Escolha local ótima → global ótima?                         │
│  → Greedy O(n) (COM PROVA!)                                 │
│                                                              │
│ Função é MONOTÔNICA?                                        │
│  → Binary Search on Answer O(n log max)                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Workflow Final: Como Abordar Qualquer Problema

```
1. LER O PROBLEMA
   ↓
2. SPEC: Entrada? Saída? Constraints? Edge cases?
   ↓
3. FORÇA BRUTA: Sempre comece com brute force!
   (Te ensina o que precisa otimizar)
   ↓
4. RECONHECER PADRÃO:
   - Grafo/Árvore? → BFS/DFS/DSU
   - Otimização? → Função é monotônica? → Binary Search
   - Otimização? → Subestrutura ótima? → DP
   - Otimização? → Greedy choice? → Greedy (com prova!)
   - Precisa todas soluções? → Backtracking
   - Vizinhança/ordenação local? → Monotonic Stack/Two Pointers
   - Substring/janela? → Sliding Window
   - Frequência? → HashMap/Heap
   - String patterns? → Trie/Regex
   ↓
5. PLAN: Trade-off entre técnicas
   ↓
6. CÓDIGO: Implementar com testes
   ↓
7. VALIDAR: Edge cases + complexidade
```

---

## 🌳 Tree Algorithms: Traversals & Construction

### Tree Traversals (DFS Variants)

**SPEC:**
- Input: `root: TreeNode`
- Output: `List[int]` (valores em ordem específica)
- Padrão: **In-order, Pre-order, Post-order, Level-order (BFS)**
- Propriedade: Cada tipo de traversal tem uso específico

**Tipos de Traversal:**
```
     1
   /   \
  2     3

PRE-ORDER (root, left, right):    [1, 2, 3] ← Serialization
IN-ORDER (left, root, right):     [2, 1, 3] ← BST → sorted
POST-ORDER (left, right, root):   [2, 3, 1] ← Delete, evaluate
LEVEL-ORDER (BFS):                [1, 2, 3] ← Layer by layer
```

**CÓDIGO:**
```python
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root: Optional[TreeNode]) -> List[int]:
    """Pre-order: root → left → right."""
    result = []
    def dfs(node):
        if not node: return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

def inorder(root: Optional[TreeNode]) -> List[int]:
    """In-order: left → root → right. BST → sorted!"""
    result = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result

def postorder(root: Optional[TreeNode]) -> List[int]:
    """Post-order: left → right → root."""
    result = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result

def levelorder(root: Optional[TreeNode]) -> List[List[int]]:
    """Level-order: BFS, retorna por nível."""
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# Tests
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
assert preorder(root) == [1, 2, 4, 5, 3]
assert inorder(root) == [4, 2, 5, 1, 3]
assert postorder(root) == [4, 5, 2, 3, 1]
assert levelorder(root) == [[1], [2, 3], [4, 5]]
print("✓ Tree Traversals Passed")
```

---

### Construct Tree from Preorder & Inorder

**SPEC:**
- Input: `preorder: List[int]`, `inorder: List[int]`
- Output: `TreeNode` (reconstruir árvore)
- Propriedade: Pre + Inorder determinam árvore unicamente

**CÓDIGO:**
```python
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Reconstruct tree from preorder & inorder."""
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    root_idx = inorder.index(root_val)
    
    root.left = buildTree(preorder[1:root_idx+1], inorder[:root_idx])
    root.right = buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
    
    return root

# Tests
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
assert inorder(root) == [9, 3, 15, 20, 7]
print("✓ Construct Tree Passed")
```

---

## 🔗 Linked List: Advanced Patterns

### Merge K Sorted Lists

**SPEC:**
- Input: `lists: List[Optional[ListNode]]` (k listas ordenadas)
- Output: `ListNode` (uma lista ordenada)
- Padrão: **Heap O(n log k)** ou **Divide & Conquer**

**CÓDIGO:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge K lists com min-heap."""
    if not lists: return None
    
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Tests
def create_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = create_list([1,4,5])
l2 = create_list([1,3,4])
l3 = create_list([2,6])
result = mergeKLists([l1, l2, l3])
assert list_to_array(result) == [1,1,2,1,3,4,4,5,6]
print("✓ Merge K Lists Passed")
```

---

### Reorder List

**SPEC:**
- Input: `head: ListNode`
- Output: Reordena in-place: [1,2,3,4] → [1,4,2,3]

**CÓDIGO:**
```python
def reorderList(head: Optional[ListNode]) -> None:
    """Reorder: divide → reverse → merge alternado."""
    if not head or not head.next: return
    
    # Encontra meio
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse segunda metade
    second = slow.next
    slow.next = None
    
    def reverse(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second = reverse(second)
    
    # Merge alternado
    first = head
    while first and second:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next

# Tests
l1 = create_list([1,2,3,4])
reorderList(l1)
assert list_to_array(l1) == [1,4,2,3]
print("✓ Reorder List Passed")
```

---

## 🎯 DP Avançado: LIS & LCS

### Longest Increasing Subsequence (LIS)

**SPEC:**
- Input: `nums: List[int]`
- Output: `int` (comprimento LIS)
- Exemplo: [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])

**CÓDIGO O(n²):**
```python
def lengthOfLIS(nums: List[int]) -> int:
    """LIS com DP: dp[i] = LIS terminando em i."""
    if not nums: return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Tests
assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
assert lengthOfLIS([3,10,2,1,20]) == 3
print("✓ LIS Passed")
```

**CÓDIGO O(n log n) com Binary Search:**

**Version 1: Using bisect (Recommended - Pythonic)**
```python
def lengthOfLIS_fast(nums: List[int]) -> int:
    """LIS com Binary Search (using bisect)."""
    import bisect
    tails = []
    
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

assert lengthOfLIS_fast([10,9,2,5,3,7,101,18]) == 4
print("✓ LIS (Bisect) Passed")
```

**Version 2: Pure Binary Search (Educational)**
```python
def lengthOfLIS_pure(nums: List[int]) -> int:
    """LIS com Pure Binary Search (manual implementation)."""
    tails = []
    
    def binary_search(arr, target):
        """Find leftmost position where target should be inserted."""
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    for num in nums:
        pos = binary_search(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

assert lengthOfLIS_pure([10,9,2,5,3,7,101,18]) == 4
print("✓ LIS (Pure) Passed")
```

**Comparison:**
| Aspect | bisect | Pure Binary Search |
|--------|--------|-------------------|
| **Time** | O(n log n) | O(n log n) |
| **Space** | O(n) | O(n) |
| **Pythonic** | ✓ Recommended | Educational |
| **Production** | Use this | Use for interviews if asked |

---

### Longest Common Subsequence (LCS)

**SPEC:**
- Input: `text1: str`, `text2: str`
- Output: `int` (comprimento LCS)
- Exemplo: "abcde" e "ace" → 3

**CÓDIGO:**
```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    """LCS com DP 2D."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Tests
assert longestCommonSubsequence("abcde", "ace") == 3
assert longestCommonSubsequence("abc", "abc") == 3
assert longestCommonSubsequence("abc", "def") == 0
print("✓ LCS Passed")
```

---

**Criado em:** Maio 2026  
**Versão:** 1.1  
**Status:** Master Reference para FAANG Preparation