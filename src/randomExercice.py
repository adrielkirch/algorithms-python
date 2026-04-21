#!/usr/bin/env python3
"""
🎯 Random Exercise Selector (Targeted Edition)
Picks a random exercise, optionally filtered by a "Hard" list.
"""

import random
import os
from pathlib import Path
from typing import Optional, List

# Define the specific filenames you consider difficult
HARD_LIST = [
    "alien_dictionary.ipynb",
    "word_search_2.ipynb",
    "number_of_island-II.ipynb",
    "min-cost-to-connect-all-points.ipynb",
    "word-break.ipynb",
    "word-break-ii.ipynb",
    "construct-binary-tree-from-preorder-and-inorder-traversal.ipynb",
    "construct-binary-tree-from-preorder-and-postorder-traversal.ipynb",
    "minimum_window_substring.ipynb",
    "lru-cache.ipynb",
    "insert-interval.ipynb",
    "longest-repeating-character-replacement.ipynb",
    "merge_two_sorted_list.ipynb",
    "merge_two_sorted_list.ipynb",
    "reorder_linked_list.ipynb",
    "house-robber-3.ipynb",
    "daily-temperatures",
    "largest-rectangle-in-histogram.ipynb",
    "clone_graph.ipynb"
]

def get_all_exercises(target_list: Optional[List[str]] = None) -> List[Path]:
    """
    Recursively finds .ipynb files. If target_list is provided, 
    only returns files that match those names.
    """
    exercises_dir = Path(__file__).parent / "exercices"
    
    if not exercises_dir.exists():
        raise FileNotFoundError(f"Directory not found: {exercises_dir}")
    
    # Get all notebooks
    all_notebooks = list(exercises_dir.rglob("*.ipynb"))
    
    if target_list:
        # Filter: only keep if the filename is in your Hard List
        notebooks = [e for e in all_notebooks if e.name in target_list]
    else:
        notebooks = all_notebooks
    
    if not notebooks:
        raise FileNotFoundError(f"No matching exercises found in {exercises_dir}")
    
    return sorted(notebooks)


def get_random_exercise(only_hard: bool = False) -> Path:
    """
    Selects a random exercise from the directory or from the Hard List.
    """
    filter_list = HARD_LIST if only_hard else None
    exercises = get_all_exercises(target_list=filter_list)
    
    history_file = Path(__file__).parent / ".exercise_history.txt"
    
    if history_file.exists():
        past_exercises = history_file.read_text().splitlines()
    else:
        past_exercises = []

    available = [e for e in exercises if str(e) not in past_exercises]

    if not available:
        print("🔄 Pool completed! Resetting history for this selection.")
        # Only reset the items currently in the active pool
        available = exercises

    selected = random.choice(available)

    # Save to history
    with open(history_file, "a") as f:
        f.write(str(selected) + "\n")

    return selected


def print_exercise_info(exercise_path: Path, mode: str) -> None:
    exercises_base = Path(__file__).parent / "exercices"
    relative_path = exercise_path.relative_to(exercises_base)
    category = relative_path.parent.name
    filename = exercise_path.name # Keeping .ipynb extension in view
    
    print("=" * 70)
    print(f"🎲 RANDOM {mode.upper()} EXERCISE SELECTED")
    print("=" * 70)
    print(f"📁 Category:  {category}")
    print(f"📝 Exercise:  {filename}")
    print(f"📂 Full Path: {exercise_path}")
    print("=" * 70)


def main():
    try:
        # Change this to False if you want to pick from ALL exercises
        FOCUS_ON_HARD = True 
        
        mode_label = "Hard" if FOCUS_ON_HARD else "General"
        exercise = get_random_exercise(only_hard=FOCUS_ON_HARD)
        print_exercise_info(exercise, mode_label)
        
        return str(exercise)
    
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n✅ Ready to solve: {result}")