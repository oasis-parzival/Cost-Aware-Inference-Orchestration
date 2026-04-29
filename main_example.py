"""
Minimal example showing how to import CAIO and optimize prompts in your application.

Usage:
    python main_example.py

This file is intended for users who have installed the package via `pip install caio-atharva`.
"""
from caio import CAIO


def main():
    optimizer = CAIO()
    prompt = """
    Hello, can you write a recursive fibonacci function in Python? Please include a docstring.
    """
    optimized = optimizer.optimize(prompt, tier="dev")
    print("Optimized prompt:\n", optimized["optimized_prompt"])


if __name__ == '__main__':
    main()
