Ax = int(input('x точки A: '))
Ay = int(input('y точки A: '))
import math
Az = int(input('z точки A: '))
Bx = int(input('x точки B: '))
By = int(input('y точки B: '))
Bz = int(input('z точки B: '))
Cx = int(input('x точки C: '))
Cy = int(input('y точки C: '))
Cz = int(input('z точки C: '))

a = math.sqrt((Bx-Cx)**2 + (By-Cy)**2 + (Bz-Cz)**2)
b = math.sqrt((Ax-Cx)**2 + (Ay-Cy)**2 + (Az-Cz)**2)
c = math.sqrt((Ax-Bx)**2 + (Ay-By)**2 + (Az-Bz)**2)
Px = int(input('x произвольной точки: '))
Py = int(input('y произвольной точки: '))
Pz = int(input('z произвольной точки: '))

AP = math.sqrt((Ax-Px)**2 + (Ay-Py)**2 + (Az-Pz)**2)
BP = math.sqrt((Bx-Px)**2 + (By-Py)**2 + (Bz-Pz)**2)
CP = math.sqrt((Cx-Px)**2 + (Cy-Py)**2 + (Cz-Pz)**2)

p = (c + AP + BP)/2
SABP = math.sqrt(p*(p-c)*(p-BP)*(p-AP))
p = (a + BP + CP)/2
SBCP = math.sqrt(p*(p-a)*(p-BP)*(p-CP))
p = (b + AP + CP)/2
SACP = math.sqrt(p*(p-b)*(p-CP)*(p-AP))
p = (a + b + c)/2

SABC = math.sqrt(p*(p-a)*(p-b)*(p-c))
hBPC = SBCP*2/a
hACP = SACP*2/b
hABP = SABP*2/c

lw = hBPC
if lw > hACP:
    lw = hACP
if lw > hABP:
    lw = hABP
print('Расстояние до ближайшей стороны или ее продолжения = ', '{:.3}'.format(lw))
