#!/usr/bin/env python3
"""Calculator Pro - Entry Point. Built by Patricio Tirado (Hyperium IA)."""

import sys
from src.cli import build_parser, run


def main():
    parser = build_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        args.command = "gui"

    run(args)


if __name__ == "__main__":
    main()
