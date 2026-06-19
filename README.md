# ✈️ Aircraft Turbofan Engine Predictive Maintenance Web Application

An interactive, web-based Machine Learning application designed to monitor and predict the **Remaining Useful Life (RUL)** of commercial aircraft turbofan engines using real-time sensor streams. This system transitions aircraft servicing from rigid schedules to data-driven, dynamic operations using the world-renowned **NASA C-MAPSS** dataset.

The system relies strictly on **classical Machine Learning architectures** (Gradient Boosting / Random Forest) paired with manual time-series feature engineering—**completely bypassing Deep Learning** to achieve lightweight, ultra-fast, real-time edge deployment.

---

## 🚀 Live Interactive Features

This web app functions as a digital operational control suite for a fleet maintenance engineer, providing:
1. **Fleet In-Service Selection:** A dynamic sidebar interface allowing the operator to select a specific live aircraft engine ID from the `test_FD001` fleet.
2. **Real-Time Telemetry Simulation:** Interactive sliders mapping directly to physical engine properties (Turbine Temperatures, Core Speeds, Static Pressure, Bypass Ratios). Adjusting a slider updates the engine state and recalculates the RUL in real-time.
3. **Automated Risk Triaging:** Operational thresholds automatically color-code the health index output:
   - 🟢 **Green (RUL > 50 Cycles):** Optimal Engine State.
   - 🟡 **Yellow (21 - 50 Cycles):** Maintenance Required Soon (Schedule servicing).
   - 🔴 **Red (≤ 20 Cycles):** **CRITICAL RISK.** Immediate ground intervention mandatory.
4. **Historical Trend Projection:** Integrated interactive line charts displaying historical sensor degradation profiles up to the exact moment of inspection.

---

## 🛠️ Machine Learning Pipeline Architecture

Because Deep Learning networks (such as LSTMs or RNNs) are excluded, the core intelligence of this engine relies on a standard tabular machine learning pipeline: