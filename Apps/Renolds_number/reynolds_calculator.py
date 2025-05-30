import matplotlib.pyplot as plt

def calculate_reynolds_number(density, velocity, diameter, viscosity):
    Re = (density * velocity * diameter) / viscosity
    return Re

def classify_flow(Re):
    if Re < 2000:
        return "Laminar Flow"
    elif 2000 <= Re <= 4000:
        return "Transitional Flow"
    else:
        return "Turbulent Flow"

def plot_flow_regime(Re):
    plt.figure(figsize=(10, 2))
    plt.axvspan(0, 2000, color='lightgreen', label='Laminar')
    plt.axvspan(2000, 4000, color='khaki', label='Transitional')
    plt.axvspan(4000, 10000, color='salmon', label='Turbulent')
    plt.axvline(Re, color='blue', linewidth=3, linestyle='--', label=f'Re = {Re:.0f}')
    plt.xlim(0, 10000)
    plt.ylim(0, 1)
    plt.yticks([])
    plt.xlabel("Reynolds Number")
    plt.title("Flow Regime Based on Reynolds Number")
    plt.legend(loc='upper center', ncol=4)
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def main():
    print("📌 Reynolds Number Calculator")
    try:
        density = float(input("Enter density (kg/m³): "))
        velocity = float(input("Enter velocity (m/s): "))
        diameter = float(input("Enter diameter (m): "))
        viscosity = float(input("Enter viscosity (Pa·s): "))

        Re = calculate_reynolds_number(density, velocity, diameter, viscosity)
        regime = classify_flow(Re)

        print(f"\n🔍 Reynolds Number: {Re:.2f}")
        print(f"🧠 Flow Regime: {regime}")
        plot_flow_regime(Re)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
