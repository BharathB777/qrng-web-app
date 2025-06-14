from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.transpiler import PassManager
from qiskit.compiler import transpile

def generate_quantum_bit(n=1):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))             # Apply Hadamard gates
    qc.measure(range(n), range(n))  # Measure the qubits

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1).result()
    counts = result.get_counts()
    bit_string = list(counts.keys())[0]
    return bit_string
