from qiskit import Aer, execute, QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import utils

# Define the Quantum Circuit for a simple optimization problem
def supply_chain_circuit():
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Apply a Hadamard gate to both qubits to create superposition
    qc.h([0, 1])
    
    # Apply a CX (CNOT) gate
    qc.cx(0, 1)
    
    # Measure the qubits
    qc.measure([0, 1], [0, 1])
    
    return qc

# Main function to run the optimization
def main():
    # Create the quantum circuit
    qc = supply_chain_circuit()
    
    # Simulate the circuit using Aer's qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')
    
    # Compile the quantum circuit for the simulator
    compiled_circuit = transpile(qc, simulator)
    
    # Execute the circuit on the qasm simulator
    job = execute(compiled_circuit, simulator, shots=1024)
    
    # Grab the results from the job
    result = job.result()
    
    # Get the counts (number of occurrences for each result)
    counts = result.get_counts(qc)
    
    # Print the counts and plot the histogram
    print("\nTotal count for each state are:", counts)
    plot_histogram(counts)
    plt.show()

if __name__ == "__main__":
    main()
