"""
Nozzle Sizer Calculator
Author: Vinod Ingale
Date: 29-May-2025

Calculates nozzle diameter or flow velocity for:
- Single-phase: Liquid or Gas
- Two-phase: Gas-Liquid mixtures

References:
- Perry’s Chemical Engineers’ Handbook
- Process Fluid Mechanics (Denn)
"""

import math
import sys
import os

# Add Utilities path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Utilities import unit_conversions as uc

def calculate_nozzle_diameter(flowrate_m3ph, velocity_mps):
    """Calculate nozzle diameter (m)."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = flowrate_m3ps / velocity_mps
    return math.sqrt((4 * area) / math.pi)

def calculate_velocity(flowrate_m3ph, diameter_m):
    """Calculate flow velocity (m/s)."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = math.pi * (diameter_m / 2) ** 2
    return flowrate_m3ps / area

def get_engineering_note(fluid, velocity):
    """Return engineering note based on fluid and velocity."""
    if fluid == "Liquid":
        if 2 < velocity < 15:
            return "✅ Velocity is within recommended range for liquid nozzles."
        else:
            return "⚠️ Velocity may be too high or too low for liquid. Check erosion/cavitation limits."

    elif fluid == "Gas":
        if 15 < velocity < 100:
            return "✅ Velocity is within recommended range for gas nozzles."
        else:
            return "⚠️ Velocity may be outside typical range for gas. Watch for noise or choking."

    elif fluid == "Two-Phase":
        if 5 < velocity < 20:
            return "✅ Velocity is typical for two-phase nozzle flow (gas-liquid mixture)."
        else:
            return "⚠️ Velocity out of suggested range. Confirm with design correlations for two-phase discharge."

def main():
    print("=== Nozzle Sizer Tool by Vinod Ingale ===")

    print("Choose calculation mode:")
    print("1 - Calculate Nozzle Diameter")
    print("2 - Calculate Flow Velocity")
    mode = input("Enter option (1 or 2): ").strip()

    print("\nSelect fluid type:")
    print("1 - Liquid")
    print("2 - Gas")
    print("3 - Two-Phase")
    fluid_type = input("Enter fluid type (1/2/3): ").strip()

    fluid_map = {'1': "Liquid", '2': "Gas", '3': "Two-Phase"}
    fluid = fluid_map.get(fluid_type)

    if not fluid:
        print("❌ Invalid fluid type selected.")
        return

    print(f"\n--- Input for {fluid} Nozzle ---")

    if mode == '1':
        flowrate = float(input("Enter Flowrate (m³/h): "))
        velocity = float(input("Enter Acceptable Velocity (m/s): "))
        diameter = calculate_nozzle_diameter(flowrate, velocity)

        print("\n--- Output ---")
        print(f"Nozzle Diameter = {diameter:.3f} meters")
        print(get_engineering_note(fluid, velocity))

    elif mode == '2':
        flowrate = float(input("Enter Flowrate (m³/h): "))
        diameter = float(input("Enter Nozzle Diameter (m): "))
        velocity = calculate_velocity(flowrate, diameter)

        print("\n--- Output ---")
        print(f"Flow Velocity = {velocity:.2f} m/s")
        print(get_engineering_note(fluid, velocity))

    else:
        print("❌ Invalid mode selected.")

if __name__ == "__main__":
    main()
