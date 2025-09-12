import torch

def check_gradients(model, inputs, target, log_interval):
    model.train()
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = model.loss(outputs, target)
    loss.backward()

    for p in model.parameters():
        if p.grad is None:
            print(f'Gradient not computed for: {p}')
        else:
            approx_grad = p.clone()
            approx_grad.backward(torch.ones_like(target))
            print(f'Float grad comparison: {p.grad.norm().item() - approx_grad.norm().item()}')
            if torch.cuda.is_available():
                approx_grad = p.data.clone()
                approx_grad.backward(torch.ones_like(target, device=inputs.device))
                print(f'Cuda grad comparison: {p.grad.norm().item() - approx_grad.norm().item()}')

    print('')

# example function call
inputs = torch.randn(1, requires_grad=True)
target = torch.randn(1)
mil = Sequential(Linear(1, 1), Identity())
mil = mil.regression(target)
check_gradients(mil, inputs, target, 1)
