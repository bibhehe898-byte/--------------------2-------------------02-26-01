"""Настройка путей для pytest."""
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path, чтобы `from num_series import ...` работал
ROOT = Path(__file__).parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))