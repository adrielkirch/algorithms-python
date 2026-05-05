#!/usr/bin/env python3
"""
🎯 Random Exercise Selector (True Random Edition)
Picks a random exercise from the 'exercices' folder regardless of difficulty.
"""

import random
from pathlib import Path
from typing import List

def get_all_exercises() -> List[Path]:
    """
    Recursively finds all .ipynb files in the exercices directory.
    """
    exercises_dir = Path(__file__).parent / "exercices"
    
    if not exercises_dir.exists():
        raise FileNotFoundError(f"Directory not found: {exercises_dir}")
    
    # Busca todos os notebooks recursivamente
    notebooks = list(exercises_dir.rglob("*.ipynb"))
    
    if not notebooks:
        raise FileNotFoundError(f"No .ipynb files found in {exercises_dir}")
    
    return sorted(notebooks)


def get_random_exercise() -> Path:
    """
    Selects a random exercise and manages history to avoid immediate repetition.
    """
    exercises = get_all_exercises()
    
    history_file = Path(__file__).parent / ".exercise_history.txt"
    
    if history_file.exists():
        past_exercises = history_file.read_text().splitlines()
    else:
        past_exercises = []

    # Filtra os que ainda não foram feitos nesta rodada
    available = [e for e in exercises if str(e) not in past_exercises]

    if not available:
        print("🔄 Pool completed! Resetting history for a new round.")
        # Limpa o arquivo de histórico para recomeçar
        history_file.write_text("")
        available = exercises

    selected = random.choice(available)

    # Salva no histórico
    with open(history_file, "a") as f:
        f.write(str(selected) + "\n")

    return selected


def print_exercise_info(exercise_path: Path) -> None:
    exercises_base = Path(__file__).parent / "exercices"
    # Tenta pegar a categoria pela pasta pai, se existir
    try:
        relative_path = exercise_path.relative_to(exercises_base)
        category = relative_path.parent.name if relative_path.parent.name else "Root"
    except ValueError:
        category = "Unknown"

    filename = exercise_path.name
    
    print("=" * 70)
    print(f"🎲 RANDOM EXERCISE SELECTED")
    print("=" * 70)
    print(f"📁 Category:  {category}")
    print(f"📝 Exercise:  {filename}")
    print(f"📂 Full Path: {exercise_path}")
    print("=" * 70)


def main():
    try:
        exercise = get_random_exercise()
        print_exercise_info(exercise)
        return str(exercise)
    
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n✅ Ready to solve: {result}")