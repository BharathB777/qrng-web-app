from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile, assemble

def generate_quantum_bits(num_bits=1):
    qc = QuantumCircuit(num_bits, num_bits)
    qc.h(range(num_bits))  # Hadamard gate to create superposition
    qc.measure(range(num_bits), range(num_bits))  # Measure qubits

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    qobj = assemble(compiled_circuit, shots=1)
    result = simulator.run(qobj).result()

    counts = result.get_counts(qc)
    return list(counts.keys())[0]  # Return binary string (e.g., '01101001')
