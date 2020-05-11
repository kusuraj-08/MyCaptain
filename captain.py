#...................Area of the Circle....................!
import numpy as np
radius=float(input("Input the radius of the circle:"))
area=(2*np.pi*(radius*2))
print("The area of the circle with radius %.1f is:%f" %(radius,area))

#...............Print Extension of the file............!
filename=input("Input the Filename:")
extns= filename.split(".")
print("The extension of the file is: "+ repr(extns[-1]))
