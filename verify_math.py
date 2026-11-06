"""Numerical independent checks of derivatives and definite integrals in new material."""
import math
from unit_content import checks
scope={k:getattr(math,k) for k in ['sin','cos','exp','log','pi']};scope['abs']=abs

def value(expr,x):return eval(expr,{'__builtins__':{}},{**scope,'x':x})
def derivative(expr,x):
 h=1e-5*max(1,abs(x));return (value(expr,x-2*h)-8*value(expr,x-h)+8*value(expr,x+h)-value(expr,x+2*h))/(12*h)
more=[
('(x**2+1)/(x+1)','x**2/2-x+2*log(abs(x+1))'),
('(x**2+2*x+3)/(x+1)','x**2/2+x+2*log(abs(x+1))'),
('(x**3+1)/(x-1)','x**3/3+x**2/2+x+2*log(abs(x-1))'),
('(3*x+1)/((x+1)*(x+2))','-2*log(abs(x+1))+5*log(abs(x+2))'),
('1/((x-1)*(x+1))','log(abs(x-1))/2-log(abs(x+1))/2'),
('(2*x+3)/((x+1)*(x+2))','log(abs(x+1))+log(abs(x+2))'),
('(x**2+1)/(x**2-3*x+2)','x-2*log(abs(x-1))+5*log(abs(x-2))'),
('x**2/(x**2-1)','x+log(abs(x-1))/2-log(abs(x+1))/2'),
('(2*x**2+1)/(x**2-1)','2*x+1.5*log(abs(x-1))-1.5*log(abs(x+1))'),
('1/(x**2-3*x+2)','-log(abs(x-1))+log(abs(x-2))'),
('log(x)','x*log(x)-x'),
('x**2*exp(x)','exp(x)*(x**2-2*x+2)'),
('(x+1)/(x-1)**2','log(abs(x-1))-2/(x-1)'),
('6*x','3*x**2'),
('(3*x+4)/((x+1)*(x+2))','log(abs(x+1))+2*log(abs(x+2))'),
('2*x*(x*x+1)**2','(x*x+1)**3/3')]
for f,F in checks+more:
 for x in [.3,.8,1.4,2.2]:
  a=value(f,x);b=derivative(F,x)
  assert math.isclose(a,b,rel_tol=2e-6,abs_tol=2e-6),(f,F,x,a,b)

def integ(f,a,b):
 n=10000;h=(b-a)/n
 return h/3*(value(f,a)+value(f,b)+sum((4 if i%2 else 2)*value(f,a+i*h) for i in range(1,n)))
definite=[('3*x**2-2',-1,2,3),('sin(x)',0,math.pi,2),('6-2*x',0,2,8),('x-3',0,2,-4),('1/x',2,1,-math.log(2)),('exp(x)+2*x',0,1,math.e),('x*(x**2+1)**2',0,2,62/3),('sin(x)*cos(x)',0,math.pi/2,.5),('3*x**2*(x**3+1)**2',0,1,7/3),('x*exp(x)',0,1,1),('log(x)',1,math.e,1),('x*cos(x)',0,1,math.sin(1)+math.cos(1)-1),('x**2*exp(x)',0,1,math.e-2),('1/(x*(x-1))',2,3,math.log(4/3)),('2*x/(x*x+1)',0,1,math.log(2)),('x*sin(x)',0,math.pi,math.pi)]
definite.extend([
 ('abs(x*x-x)',-1,2,11/6),
 ('abs(x*x-2*x)',-1,3,4),
 ('abs(2*x)',-2,1,5),
 ('x+2',-1,1,4),
 ('2*x-1',0,2,2),
 ('2*x-4',0,3,-3),
 ('abs(2*x-4)',0,3,5),
 ('2*x',3,-1,-8),
 ('x*x',1,2,7/3),
 ('x*x',0,1,1/3),
])
for f,a,b,want in definite:
 got=integ(f,a,b);assert math.isclose(got,want,rel_tol=1e-7,abs_tol=1e-7),(f,got,want)
print(f'{len(checks+more)} stofnföll prófuð með tölulegri diffrun á fjórum stöðum; {len(definite)} ákveðin heildi prófuð tölulega.')
