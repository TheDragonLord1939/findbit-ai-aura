# -*- coding:utf-8 -*-
import torch
from torch import nn
from torch.optim import *
from algorithm.darkbox_func import *
import numpy as np

class FunctionSim2(nn.Module):
    def __init__(self, hidden_num = 100):
        super(FunctionSim2, self).__init__()
        self.model = nn.Sequential(nn.Linear(1, hidden_num),
                                   nn.Sigmoid(),
                                   nn.Linear(hidden_num, hidden_num),
                                   nn.ReLU(),
                                   nn.Linear(hidden_num, 1))

    def forward(self, x):
        return self.model(x)

class FunctionSim1(nn.Module):
    def __init__(self):
        super(FunctionSim1, self).__init__()
        self.a = nn.Parameter(torch.Tensor(np.random.rand(1)))
        self.b = nn.Parameter(torch.Tensor(np.random.rand(1)))
        self.c = nn.Parameter(torch.Tensor(np.random.rand(1)))

    # define your own function
    def forward(self, x):
        return self.a * x.pow(2) + self.b * x + self.c

if __name__ == '__main__':
    # model = FunctionSim1()#FunctionSim2(100)
    model = FunctionSim2(100)
    opt = Adam(list(model.parameters()))
    # opt = SGD(list(model.parameters()), lr=0.001)
    loop_count = 0

    # device = torch.device('cuda')
    device = torch.device('cpu')
    model.to(device)
    samples = get_samples(100000)
    epochs = 10
    loss = []
    loss_val = 0
    batch_size = 32
    for _ in range(epochs):
        np.random.shuffle(samples)
        #(x#特征，, y#标签)
        for (x, _y) in samples:
            y = model.forward(torch.Tensor([x]))
            _y = torch.Tensor([_y])
            # loss = ((y - _y).pow(2))
            # loss_val = loss.item()
            # loss.backward()
            # opt.step()
            loop_count += 1

            loss.append((y - _y).pow(2))
            if loop_count % batch_size == 0:
                loss = torch.sum(torch.stack(loss))
                loss.backward()
                opt.step()
                opt.zero_grad()
                loss_val = loss.item()
                loss = []

            if loop_count % 100 == 0:
                print(loss_val)
                # print(model.a, model.b, model.c)

            # 最近k轮平均loss < threshold

