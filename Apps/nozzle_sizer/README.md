# 🚀 Nozzle Sizer Calculator

This Python tool calculates either the **internal nozzle diameter** or the **outlet flow velocity**, based on flowrate and fluid properties. It supports **liquid**, **gas**, and **two-phase** (gas-liquid) flows.

---

## ✅ Features

- Supports 3 fluid types:
  - 💧 Liquid
  - 🌬️ Gas
  - 🌫️ Two-phase (gas-liquid mixtures)
- Choose calculation mode:
  - Pipe **diameter** from flowrate and velocity
  - Flow **velocity** from flowrate and diameter
- Includes engineering notes based on velocity ranges
- CLI-based for quick use and easy testing
- Built with clean modular code structure

---

## 📘 Why This Matters

Proper nozzle sizing ensures:
- ✅ Accurate jet or spray discharge
- ✅ Prevents high-velocity erosion and noise
- ✅ Avoids cavitation in liquids and instability in two-phase flows
- ✅ Used in reactors, distributors, compressors, and injection systems

---

## 📐 Engineering Formulas Used

### Flow Velocity:
\[
u = \frac{Q}{A} = \frac{Q}{\frac{\pi D^2}{4}}
\]

### Nozzle Diameter:
\[
D = \sqrt{ \frac{4Q}{\pi u} }
\]

Where:
- \( Q \) = Volumetric flowrate [m³/s]  
- \( u \) = Flow velocity [m/s]  
- \( D \) = Nozzle inner diameter [m]

> Flowrate is internally converted from m³/h to m³/s.

---

## 🧪 Velocity Guidelines

| Fluid Type    | Typical Velocity Range |
|---------------|-------------------------|
| Liquid        | 2 – 15 m/s              |
| Gas           | 15 – 100 m/s            |
| Two-Phase     | 5 – 20 m/s              |

> ⚠️ Always validate with mechanical design limits for critical service nozzles.

---

## 🧾 References

- Perry’s Chemical Engineers' Handbook, 8th Ed.
- Denn – *Process Fluid Mechanics*
- Chemical Engineering Design Standards (BHR Group, API)

---

## 🚀 How to Run

```bash
python nozzle_sizer.py
