
import numpy
from scipy.weave import converters
from scipy import weave

code = """
for(int i=0; i<arr_size; i++) {
    output[i] = input1[i] + input2[i];
}
"""

arr_size = 5
input1 = numpy.array([1, 2, 3, 4, 5])
input2 = numpy.array([5, 4, 3, 2, 1])
output = numpy.zeros(arr_size, dtype=numpy.int32)

weave.inline(code, ['input1', 'input2', 'output', 'arr_size'],
             type_converters=converters.blitz)

print("Input 1:", input1)
print("Input 2:", input2)
print("Output:", output)
