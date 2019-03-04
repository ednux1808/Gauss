
#@Metodo gauss seiden 

import numpy as np
print('Array Uno Datos :')
a01 = float(input())
a02 = float(input())
a03 = float(input())
b0 = float(input())
print('Array Dos Datos :')
a11 = float(input())
a12 = float(input())
a13 = float(input())
b1 = float(input())
print('Array Tres Datos :')
a21 = float(input())
a22 = float(input())
a23 = float(input())
b2 = float(input())

a = np.array([[a01,a02,a03],[a11,a12,a13],[a21,a22,a23]])
b = np.array([b0,b1,b2])
x = np.linalg.solve(a,b)
print('| x1 =',x[0] , '| x2 =',x[1] , '| x3 =',x[2] )
print('| Rx1 =',a[0][0]*x[0]+a[0][1]*x[1]+a[0][2]*x[2])
print('| Rx2 =',a[1][0]*x[0]+a[1][1]*x[1]+a[1][2]*x[2])
print('| Rx3 =',a[2][0]*x[0]+a[2][1]*x[1]+a[2][2]*x[2])

