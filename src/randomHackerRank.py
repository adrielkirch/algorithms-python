import random

def sortear_desafio():
    # Lista limpa apenas com os nomes dos exercícios
    exercicios = [
        "Queue using Two Stacks",
        "Roads and Libraries",
        "Balanced Brackets",
        "Find the Running Median",
        "Tries: Contacts",
        "Valid BST",
        "Rust & Murderer",
        "Even Tree",
        "Common Child",
        "Special String Again",
        "Making Anagrams",
        "Sherlock and the Valid String",
        "Hash Tables: Ransom Note",
        "Pairs",
        "Fraudulent Activity Notifications",
        "Frequency Queries",
        "Count Triplets",
        "Jack goes to Rapture",
        "Dijkstra: Shortest Reach 2",
        "Gridland Provinces",
        "Crossword Puzzle",
        "Bigger is Greater",
        "Tree: Height of a Binary Tree",
        "Cut the Tree",
        "Tree: Level Order Traversal",
        "Find the nearest clone",
        "Journey to the Moon",
        "DFS: Connected Cell in a Grid",
        "Connected Cells in a Grid",
        "BFS: Shortest Reach",
        "BFS: Shortest Reach in a Graph",
        "Beautiful Triplets",
        "Queen's Attack II",
        "Non-Divisible Subset",
        "Cut the sticks",
        "Picking Numbers",
        "Climbing the Leaderboard",
        "Subarray Division"
    ]

    escolhido = random.choice(exercicios)
    
    print("-" * 40)
    print(f"🚀 Próximo desafio: {escolhido}")
    print("-" * 40)

if __name__ == "__main__":
    sortear_desafio()