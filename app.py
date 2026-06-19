from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


APP_TITLE = "Aircraft Turbofan RUL Predictor"
APP_SUBTITLE = "Classical ML inference for NASA C-MAPSS FD001"
WINDOW_SIZE = 15
FUTURE_STEPS = 10

