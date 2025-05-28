"""
Unit Conversions Utilities
Author: Vinod Ingale
Date: 28-May-2025

This module provides basic unit conversions for Chemical Engineering calculations.
"""

# -------------------------------
# Volume Flow Conversions
# -------------------------------

def m3ph_to_m3ps(flowrate_m3ph):
    """
    Convert flowrate from cubic meters per hour (m³/h) to cubic meters per second (m³/s).
    """
    return flowrate_m3ph / 3600

def m3ps_to_m3ph(flowrate_m3ps):
    """
    Convert flowrate from cubic meters per second (m³/s) to cubic meters per hour (m³/h).
    """
    return flowrate_m3ps * 3600

def lpm_to_m3ps(flowrate_lpm):
    """
    Convert flowrate from liters per minute (L/min) to cubic meters per second (m³/s).
    """
    return flowrate_lpm / (1000 * 60)

def m3ps_to_lpm(flowrate_m3ps):
    """
    Convert flowrate from cubic meters per second (m³/s) to liters per minute (L/min).
    """
    return flowrate_m3ps * 1000 * 60

# -------------------------------
# Pressure Conversions
# -------------------------------

def pa_to_kpa(pressure_pa):
    """
    Convert pressure from Pascal (Pa) to kiloPascal (kPa).
    """
    return pressure_pa / 1000

def kpa_to_pa(pressure_kpa):
    """
    Convert pressure from kiloPascal (kPa) to Pascal (Pa).
    """
    return pressure_kpa * 1000

def pa_to_bar(pressure_pa):
    """
    Convert pressure from Pascal (Pa) to bar.
    """
    return pressure_pa / 100000

def bar_to_pa(pressure_bar):
    """
    Convert pressure from bar to Pascal (Pa).
    """
    return pressure_bar * 100000

def bar_to_psi(pressure_bar):
    """
    Convert pressure from bar to psi.
    """
    return pressure_bar * 14.5038

def psi_to_bar(pressure_psi):
    """
    Convert pressure from psi to bar.
    """
    return pressure_psi / 14.5038

# -------------------------------
# Temperature Conversions
# -------------------------------

def celsius_to_kelvin(temp_celsius):
    """
    Convert temperature from Celsius to Kelvin.
    """
    return temp_celsius + 273.15

def kelvin_to_celsius(temp_kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    """
    return temp_kelvin - 273.15

def celsius_to_fahrenheit(temp_celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (temp_celsius * 9/5) + 32

def fahrenheit_to_celsius(temp_fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (temp_fahrenheit - 32) * 5/9
