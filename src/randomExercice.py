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
    """
    Seleciona um exercício aleatório
    
    Returns:
        Path do arquivo .ipynb selecionado
    """
    exercises = get_all_exercises()
    selected = random.choice(exercises)
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
