#!/usr/bin/env python3
"""
🎯 Random Exercise Selector
Picks a random .ipynb exercise from /src/exercices/ directory
"""

import random
import os
from pathlib import Path
from typing import Optional, List


def get_all_exercises() -> List[Path]:
    """
    Recursivamente busca todos os arquivos .ipynb em /src/exercices/
    
    Returns:
        Lista de caminhos absolutos para arquivos .ipynb
    """
    exercises_dir = Path(__file__).parent / "exercices"
    
    if not exercises_dir.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {exercises_dir}")
    
    # Encontra todos os arquivos .ipynb recursivamente
    notebooks = list(exercises_dir.rglob("*.ipynb"))
    
    if not notebooks:
        raise FileNotFoundError(f"Nenhum arquivo .ipynb encontrado em {exercises_dir}")
    
    return sorted(notebooks)


def get_random_exercise() -> Path:
    exercises = get_all_exercises()
    
    # Criar um arquivo simples de histórico para evitar repetições
    history_file = Path(__file__).parent / ".exercise_history.txt"
    
    if history_file.exists():
        past_exercises = history_file.read_text().splitlines()
    else:
        past_exercises = []

    # Filtra exercícios que ainda não foram feitos
    available = [e for e in exercises if str(e) not in past_exercises]

    # Se todos já foram feitos, reseta o histórico
    if not available:
        print("🔄 All exercises completed! Resetting history.")
        available = exercises
        past_exercises = []

    selected = random.choice(available)

    # Salva no histórico
    with open(history_file, "a") as f:
        f.write(str(selected) + "\n")

    return selected


def print_exercise_info(exercise_path: Path) -> None:
    """
    Imprime informações sobre o exercício selecionado
    
    Args:
        exercise_path: Caminho do arquivo .ipynb
    """
    # Obtém o caminho relativo a partir do diretório /src/exercices
    exercises_base = Path(__file__).parent / "exercices"
    relative_path = exercise_path.relative_to(exercises_base)
    category = relative_path.parent.name
    filename = exercise_path.stem
    
    print("=" * 70)
    print("🎲 RANDOM EXERCISE SELECTED")
    print("=" * 70)
    print(f"📁 Category:  {category}")
    print(f"📝 Exercise:  {filename}")
    print(f"📂 Full Path: {exercise_path}")
    print("=" * 70)


def main():
    """Função principal"""
    try:
        exercise = get_random_exercise()
        print_exercise_info(exercise)
        
        # Opcionalmente, retorna o caminho para uso programático
        return str(exercise)
    
    except FileNotFoundError as e:
        print(f"❌ Erro: {e}")
        return None


if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n✅ Exercise ready at: {result}")
