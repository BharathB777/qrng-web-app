from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def generate_quantum_bit():
    qc = QuantumCircuit(8, 8)
    qc.h(range(8))  # Apply Hadamard to all 8 qubits
    qc.measure(range(8), range(8))

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1).result()
    counts = result.get_counts(qc)

    return list(counts.keys())[0]
