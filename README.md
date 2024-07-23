# Quantum Supply Chain Optimization

This project demonstrates a simple quantum computing task using Qiskit to optimize a basic supply chain problem. The project consists of a quantum circuit that uses superposition and entanglement to explore possible states of a supply chain model.

## Files

1. `supply_chain_optimization.py`: The main quantum computing script.
2. `utils.py`: Utility functions.
3. `requirements.txt`: The necessary dependencies.
4. `README.md`: Project instructions.

## Requirements

- Python 3.8 or later
- Qiskit
- Matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quantum-supply-chain-optimization.git
   cd quantum-supply-chain-optimization
    ```
   
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
   ```
    
    Usage
Run the main script to execute the quantum supply chain optimization:

bash
Copier le code
python supply_chain_optimization.py
This will run the quantum circuit on a simulator and display a histogram of the results.

Project Description
The supply_chain_optimization.py script creates a quantum circuit with 2 qubits and 2 classical bits, applies Hadamard and CX (CNOT) gates to create superposition and entanglement, and then measures the qubits. The simulation results are plotted as a histogram.

The utils.py file contains utility functions that can be used for additional tasks, such as displaying the circuit layout.

Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

License
This project is licensed under the MIT License.
