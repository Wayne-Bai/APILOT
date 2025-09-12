import numpy as np

def einsum(operation, *operands):
    # Parsing the operation to extract the operation path
    subscripts, _ = np.einsum_path(operation, *operands, optimize='optimal')
    
    # Loop over each operation in the path and carry out the specified tensor operation
    result = operands[subscripts[0][0]]
    for operand_indices, einsum_str, remaining in subscripts[1:]:
        operand_list = [operands[idx] for idx in operand_indices]
        sub_in, sub_out = einsum_str.split('->')
        input_subscripts = sub_in.split(',')

        # Prepare the axes for tensordot
        axes = ([], [])
        for i, sub in enumerate(input_subscripts):
            for char in sub:
                if char not in sub_out:
                    axes[i].append(sub.index(char))
                if char in input_subscripts[i - 1] and i > 0:
                    axes[i - 1].append(sub.index(char))

        # Perform the tensor operation using tensordot
        result = np.tensordot(result, operand_list[1], axes=axes)

        # Reorder axes if necessary
        if remaining:
            result = np.moveaxis(result, range(len(sub_out)), [sub_out.index(axis) for axis in remaining])

    return result

# Example usage:
a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print(einsum('i,i->', a, b))  # Should operate like np.dot(a, b)
