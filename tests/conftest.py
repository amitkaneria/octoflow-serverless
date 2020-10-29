import os
import sys
from pathlib import Path

import pytest

# Add dependencies/python folder as a PATH to handle test cases
SHARED_UTILS_PATH = Path(__file__).parent.parent.joinpath("dependencies","python")
sys.path.insert(0, str(SHARED_UTILS_PATH))
