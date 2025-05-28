"""
Nozzle Sizer Calculator
Author: Vinod Ingale
Date: 28-May-2025

This tool calculates nozzle internal diameter or outlet velocity for both liquids and gases.

References:
- Perry’s Chemical Engineers’ Handbook
- Process Fluid Mechanics (Denn)
- Typical Nozzle Velocities:
  • Liquid: 2 – 15 m/s
  • Gas: 15 – 100 m/s (or up to choked flow in special cases)
"""

import math
import sys
import os

# Add Utilities path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Utilities import unit_conversions as uc

def calculate_nozzle_diameter(flowrate_m3ph, velocity_mps):
    """Calculate nozzle internal diameter (m)."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = flowrate_m3ps / velocity_mps
    diameter = math.sqrt((4 * area) / math.pi)
    return diameter

def calculate_velocity(flowrate_m3ph, diameter_m):
    """Calculate flow velocity in nozzle (m/s)."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = math.pi * (diameter_m / 2) ** 2
    velocity = flowrate_m3ps / area
    return velocity

def main():
    print("=== Nozzle Sizer Tool by Vinod Ingale ===")

    print("Choose calculation mode:")
    print("1 - Calculate Nozzle Diameter")
    print("2 - Calculate Outlet Velocity")
    mode = input("Enter option (1 or 2): ").strip()

    print("\nSelect fluid type:")
    print("1 - Liquid")
    print("2 - Gas")
    fluid_type = input("Enter fluid type (1 or 2): ").strip()

    if fluid_type == '1':
        fluid = "Liquid"
    elif fluid_type == '2':
        fluid = "Gas"
    else:
        print("Invalid fluid type selected.")
        return

    print(f"\n--- Input for {fluid} Nozzle ---")

    if mode == '1':
        flowrate = float(input("Enter Flowrate (m³/h): "))
        velocity = float(input("Enter Acceptable Velocity (m/s): "))
        diameter = calculate_nozzle_diameter(flowrate, velocity)
        print("\n--- Output ---")
        print(f"Nozzle Diameter = {diameter:.3f} meters")

        # Engineering note
        if fluid == "Liquid" and 2 < velocity < 15:
            print("Note: Velocity is within recommended range for liquid nozzle.")
        elif fluid == "Gas" and 15 < velocity < 100:
            print("Note: Velocity is within recommended range for gas nozzle.")
        else:
            print("Warning: Velocity may be outside typical range. Check erosion/cavitation limits.")

    elif mode == '2':
        flowrate = float(input("Enter Flowrate (m³/h): "))
        diameter = float(input("Enter Nozzle Diameter (m): "))
        velocity = calculate_velocity(flowrate, diameter)
        print("\n--- Output ---")
        print(f"Flow Velocity = {velocity:.2f} m/s")

        # Engineering note
        if fluid == "Liquid" and 2 < velocity < 15:
            print("Note: Velocity is within recommended range for liquid nozzle.")
        elif fluid == "Gas" and 15 < velocity < 100:
            print("Note: Velocity is within recommended range for gas nozzle.")
        else:
            print("Warning: Velocity may be outside typical range. Review design criteria.")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
