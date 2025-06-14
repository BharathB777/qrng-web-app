from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def generate_quantum_bit(n=8):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))  # Put qubits in superposition
    qc.measure(range(n), range(n))  # Measure the qubits

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1).result()
    counts = result.get_counts(qc)

    return list(counts.keys())[0]
