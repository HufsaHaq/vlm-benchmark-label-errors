"""Smoke tests for the package scaffold."""

import vlmlabels


def test_package_imports():
    """Keep the package importable before feature modules are added."""
    assert vlmlabels.__version__ == "0.1.0"
