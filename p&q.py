import sympy
N=778295693469049358264658856187
f=778295693469047586274338726816
p,q=sympy.symbols("p q")
a=sympy.solve([(p-1)*(q-1)-f,p*q-N],[p,q])
print(a)