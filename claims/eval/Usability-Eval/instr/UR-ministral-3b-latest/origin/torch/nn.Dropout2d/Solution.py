import torch

def randomly_zero_channels(model, p):
    def zero_channels(module):
        def zero_out_channels():
            with torch.no_grad():
                return module(x) if module is not x else x

        def wrapper_forward(*args, **kwargs):
            out = moduleforward(*args, **kwargs)
            if isinstance(module, torch.nn.Conv2d) or isinstance(module, torch.nn.ConvTranspose2d):
                channel_zeroed = torch.zeros_like(module.weight[:][0])
                samples = torch.bernoulli(channel_zeroed.new_ones(module.weight.shape))
                mask = samples == 1
                module.weight.zero_()
                module.weight[mask.new_full(module.weight.shape[:-1], 0)] = 0
            return zero_out_channels()

        if isinstance(module, torch.nn.Module):
            module.forward = wrapper_forward
            return module
        else:
            return module

    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Conv2d) or isinstance(module, torch.nn.ConvTranspose2d):
            module.forward = zero_channels(module)
