import torch
obj = torch.tensor([[2,3], [4,5], [5,9]])
print(obj)
print(type(obj), len(obj))
print(torch.is_nonzero(torch.tensor([0])))
print(torch.is_nonzero(torch.tensor([.1])))
arr = torch.arange(start=20, end=40).chunk
print(arr)