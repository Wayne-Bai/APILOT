def are_sequences_equal_with_tolerance(seq1, seq2, tolerance):
    # Check if the sequences have the same length
    if len(seq1) != len(seq2):
        return False

    # Check if each element is equal to corresponding element of the other sequence within tolerance
    for i in range(len(seq1)):
        if abs(seq1[i] - seq2[i]) > tolerance:
            return False

    # If all checks passed, the sequences are equal within tolerance
    return True
