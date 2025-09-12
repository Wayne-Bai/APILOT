
import scipy

# Compile and execute C/C++ code on the fly using scipy.
code = "int main() { return 0; }"
scipy.compile_run(code)
