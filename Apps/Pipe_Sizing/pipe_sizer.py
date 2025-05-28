"""
Pipe Sizer Calculator
Author: Vinod Ingale
Date: 28-May-2025

Description:
This tool calculates pipe diameter OR velocity depending on user input.
Supports both LIQUID and GAS flow.

Options:
1. Pipe Diameter (from Flowrate + Velocity)
2. Velocity (from Flowrate + Diameter)

References:
- McCabe & Smith – Unit Operations of Chemical Engineering
- Coulson & Richardson – Chemical Engineering Vol. 1, 6th Ed.
- Standard formulas for incompressible (liquid) and ideal gas flow

Assumptions:
- Steady-state flow
- No compressibility correction for gas
"""

import math
import sys
import os

# Add Utilities folder to import unit_conversions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Utilities import unit_conversions as uc

def calculate_diameter(flowrate_m3ph, velocity_mps):
    """Return diameter in meters from flowrate and velocity."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = flowrate_m3ps / velocity_mps
    diameter = math.sqrt((4 * area) / math.pi)
    return diameter

def calculate_velocity(flowrate_m3ph, diameter_m):
    """Return velocity in m/s from flowrate and pipe diameter."""
    flowrate_m3ps = uc.m3ph_to_m3ps(flowrate_m3ph)
    area = (math.pi / 4) * diameter_m**2
    velocity = flowrate_m3ps / area
    return velocity

def main():
    print("=== Pipe Sizer Tool by Vinod Ingale ===")
    print("Choose calculation mode:")
    print("1 - Calculate Pipe Diameter")
    print("2 - Calculate Flow Velocity")
    
    mode = input("Enter option (1 or 2): ").strip()
    if mode not in ['1', '2']:
        print("❌ Invalid selection. Please run again.")
        return
    
    print("\nSelect fluid type:")
    print("1 - Liquid")
    print("2 - Gas")
    fluid_type = input("Enter fluid type (1 or 2): ").strip()

    if fluid_type == '1':
        fluid = "Liquid"
    elif fluid_type == '2':
        fluid = "Gas"
    else:
        print("❌ Invalid fluid type.")
        return

    print(f"\n--- Input for {fluid} Flow ---")

    flowrate_m3ph = float(input("Enter Flowrate (m³/h): "))
    fluid_density = float(input("Enter Fluid Density (kg/m³): "))

    if mode == '1':
        velocity_mps = float(input("Enter Acceptable Velocity (m/s): "))
        diameter = calculate_diameter(flowrate_m3ph, velocity_mps)
        velocity = velocity_mps  # So velocity is available for note message
        print("\n--- Output ---")
        print(f"Minimum Pipe Diameter = {diameter:.3f} meters")

    else:
        diameter_m = float(input("Enter Internal Pipe Diameter (m): "))
        velocity = calculate_velocity(flowrate_m3ph, diameter_m)
        print("\n--- Output ---")
        print(f"Estimated Flow Velocity = {velocity:.2f} m/s")

    # Optional safety guidance
    if fluid == "Liquid":
        if 1.0 <= velocity <= 3.0:
            note = "✅ Velocity is in the recommended range for clean liquid flow."
        elif velocity < 1.0:
            note = "⚠️ Low velocity. Risk of solid settling or poor scouring."
        elif 3.0 < velocity <= 5.0:
            note = "⚠️ High velocity. Monitor for erosion/noise in long-term operation."
        else:
            note = "❌ Velocity too high! Erosion or noise likely. Consider resizing."

    else:  # Gas
        if 10.0 <= velocity <= 40.0:
            note = "✅ Velocity is within standard range for gas flow."
        elif velocity < 10.0:
            note = "⚠️ Velocity is low. May cause flow instability or poor mixing."
        elif 40.0 < velocity <= 60.0:
            note = "⚠️ High velocity. Monitor for noise and compressibility effects."
        else:
            note = "❌ Velocity very high! Consider compressibility and pressure drop."
        
    if mode == '2':
        print(f"\nEngineering Note: {note}")

if __name__ == "__main__":
    main()
