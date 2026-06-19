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

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "6.+Turbofan+Engine+Degradation+Simulation+Data+Set" / "6. Turbofan Engine Degradation Simulation Data Set" / "CMAPSSData"
TEST_FILE = DATA_DIR / "test_FD001.txt"
MODEL_FILE = BASE_DIR / "best_model.pkl"
SCALER_FILE = BASE_DIR / "scaler.pkl"

RAW_COLUMNS = [
    "unit",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
] + [f"s{i}" for i in range(1, 22)]

RISK_THRESHOLDS = {
    "healthy": 50,
    "warning": 20,
}

CRITICAL_SENSOR_MAP = {
    "Temperature proxy (S2)": "s2",
    "Pressure proxy (S3)": "s3",
    "Core speed proxy (S4)": "s4",
    "Bypass ratio proxy (S7)": "s7",
}


