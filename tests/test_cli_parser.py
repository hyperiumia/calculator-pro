"""Tests for CLI argument parser."""

import pytest
from src.cli import build_parser


class TestCLIParser:

    def test_gui_command(self):
        parser = build_parser()
        args = parser.parse_args(["gui"])
        assert args.command == "gui"

    def test_calc_command(self):
        parser = build_parser()
        args = parser.parse_args(["calc", "2+3"])
        assert args.command == "calc"
        assert args.expression == "2+3"

    def test_calc_scientific(self):
        parser = build_parser()
        args = parser.parse_args(["calc", "sqrt(144)"])
        assert args.expression == "sqrt(144)"

    def test_history_command(self):
        parser = build_parser()
        args = parser.parse_args(["history"])
        assert args.command == "history"
