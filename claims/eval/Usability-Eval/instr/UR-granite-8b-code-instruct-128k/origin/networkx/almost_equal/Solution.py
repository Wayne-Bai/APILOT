import networkx as nx

def assert_equal_numbers(number1, number2, tolerance=1e-6):
    assert abs(number1 - number2) <= tolerance, f"Numbers are not equal within tolerance: {number1} != {number2}"

def assert_equal_sequences(sequence1, sequence2, tolerance=1e-6):
    assert len(sequence1) == len(sequence2), f"Sequences have different lengths: {len(sequence1)} != {len(sequence2)}"
    for i in range(len(sequence1)):
        assert abs(sequence1[i] - sequence2[i]) <= tolerance, f"Sequences are not equal within tolerance at index {i}: {sequence1[i]} != {sequence2[i]}"

