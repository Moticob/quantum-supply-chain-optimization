# Utility functions can be added here for any auxiliary tasks
# Example utility function to display the circuit (optional)

from qiskit.visualization import plot_circuit_layout

def display_circuit_layout(circuit, backend):
    plot_circuit_layout(circuit, backend)
