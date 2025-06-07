"""
Pathlib demo
"""
import os
from pathlib import Path


def main():
    # p = Path(".")
    # print("Current directory:", p.resolve())
    p = Path(__file__).parent
    print("Current directory:", p.resolve())
    for file in p.rglob("*.py"):
        print(file.name)
if __name__ == "__main__":
    main()
    print("os.path.abspath(__file__):", os.path.abspath(__file__))
    print("Path(__file__).resolve():", Path(__file__).resolve())
    # main()