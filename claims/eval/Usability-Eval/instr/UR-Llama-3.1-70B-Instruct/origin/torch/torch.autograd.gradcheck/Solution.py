import torch
import torch.autograd as autograd
import torch.testing
import unittest
import math
from torch.testing import assert_allclose

# Helper function to check gradients via finite differences
def _checkCtxFiniteDifference(ctx, uplest, func):
    def func_wrapper(*args):
        inputs = list(args)
        for i, inp in enumerate(uplest):
            if isinstance(inp, torch.Tensor):
                inputs[i] = uplest[i].clone().detach().requires_grad_(True)
        return func(*inputs)

    torch.autograd.gradcheck(func_wrapper, uplest, eps=1e-4, atol=1e-3, raise_exception=True)

class TestAutograd(unittest.TestCase):
    def test_torch_finite_differences_all_dtypes(self):
        # Real-valued Tensors with requires_grad=True
        for dtype in [torch.float32, torch.float64, torch.bfloat16]:
            inputs = (torch.randn(1, requires_grad=True, dtype=dtype),)
            _checkCtxFiniteDifference("cpu", inputs, lambda x: torch.sin(x))

        # Complex-valued Tensors with requires_grad=True
        for dtype in [torch.complex64, torch.complex128]:
            inputs = (torch.randn(1, requires_grad=True, dtype=dtype),)
            _checkCtxFiniteDifference("cpu", inputs, lambda x: torch.sin(x))

    def test_torch_finite_differences_all_dtypes_cuda(self):
        # Real-valued Tensors with requires_grad=True
        for dtype in [torch.float32, torch.float64, torch.bfloat16]:
            inputs = (torch.randn(1, requires_grad=True, dtype=dtype).to('cuda'),)
            _checkCtxFiniteDifference("cuda", inputs, lambda x: torch.sin(x))

        # Complex-valued Tensors with requires_grad=True
        for dtype in [torch.complex64, torch.complex128]:
            inputs = (torch.randn(1, requires_grad=True, dtype=dtype).to('cuda'),)
            _checkCtxFiniteDifference("cuda", inputs, lambda x: torch.sin(x))

if __name__ == '__main__':
    unittest.main()
