import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app.models import Base

target_metadata = Base.metadata

