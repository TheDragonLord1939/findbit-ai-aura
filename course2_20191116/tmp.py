# -*- coding: utf-8 -*-
'''
def one_36(x):
    return x, 0

l =  one_36(6)
z = 1


from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render("echarts/demo1.html")
bar


from pyecharts import Bar, Line, Overlap

attr = ['A', 'B', 'C', 'D', 'E', 'F']
v1 = [10, 20, 30, 40, 50, 60]
v2 = [38, 28, 58, 48, 78, 68]
bar = Bar("Line - Bar 示例")
bar.add("bar", attr, v1)
line = Line()
line.add("line", attr, v2)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)
overlap.render("echarts/demo3.1.html")
overlap


'''

import sympy.stats as stats
coin = stats.Die('coin',2)
P=stats.P
E=stats.E

import numpy as np
rd = np.random.random(1000)*2+1
z = rd.astype(int)


import sympy as sym
x, y = sym.symbols('x y')
normal = stats.Normal('N', 2, 3)

z = 1

import numpy as np
import scipy
import sympy as sym
import matplotlib
sym.init_printing()

x = sym.symbols('x')
a = sym.Integral(sym.cos(x)*sym.exp(x), x)
a.doit()
sym.Eq(a, a.doit())

z = 1

x, y = sym.symbols('x y')
z=sym.series((x-3)*(x+1)*(x+4)*(x-4)*x,x,x0=0,n=4)
z