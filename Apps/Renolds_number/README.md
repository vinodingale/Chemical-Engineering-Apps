# 🌀 Reynolds Number Calculator with Flow Regime Visualization

This Python-based tool calculates the **Reynolds Number** for fluid flow through a pipe and visually indicates the flow regime: **Laminar**, **Transitional**, or **Turbulent**. It's a fundamental utility for Chemical and Mechanical Engineers to classify flow behavior quickly and accurately.

---

## 🔧 Features

- ✅ Calculates Reynolds Number from user input:
  - Fluid Velocity (m/s)
  - Pipe Diameter (m)
  - Fluid Density (kg/m³)
  - Dynamic Viscosity (Pa·s)
- ✅ Determines Flow Regime:
  - Laminar (Re < 2000)
  - Transitional (2000 ≤ Re ≤ 4000)
  - Turbulent (Re > 4000)
- ✅ Graphical Output:
  - Visual chart shows where the calculated Reynolds number lies on the flow regime scale.
- ✅ Clean, beginner-friendly interface (Tkinter or CLI-based)
- ✅ Lightweight and easy to use

---

## 📸 Screenshot

![Figure_1](https://github.com/user-attachments/assets/7e19d341-5c4b-4d44-86b1-6c494fc50402)


---

## 🧮 Formula Used

\[
Re = \frac{{\rho \cdot v \cdot D}}{{\mu}}
\]

Where:
- \( \rho \): Density (kg/m³)
- \( v \): Velocity (m/s)
- \( D \): Pipe Diameter (m)
- \( \mu \): Dynamic Viscosity (Pa·s)

---

## 🖥️ How to Run
   ```bash
python reynolds_calculator.py
