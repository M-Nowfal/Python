# PROGRAM 1 – Program using Arrays and String functions.

print("\t\t********************")
print("\t\t STRING OPERATIONS ")
print("\t\t*********************")

S1 = "Python Program"
S2 = "String Operations"

print("\nAvailable Strings")
print("Srting 1: ", S1, '\nString 2: ', S2)

print("\n STRING LENGTH:")
print('STR1: ', len(S1))
print('STR2: ', len(S2))

print("\n SLICING STRINGS")
print('STR 1:')
print(S1[2:9])
print(S1[2:9:2])
print(S1[2:7])
print(S1[2:9:1])
print(S1[::-1])

print('STR 2:')
print(S2[1:6])
print(S2[2:8:2])
print(S2[2:8])
print(S2[2:8:1])
print(S2[::-1])

print("\nSTRING CASE CONVERSION")
print("Upper case:")
print(S1.upper())
print(S2.upper())

print("Lower case:")
print(S1.lower())
print(S2.lower())

print("\n VERIFYING START & END OF THE STRING")
print("STARTS WITH:")
print("S1 starts with 'P': ", S1.startswith("P"))
print("S2 starts with 's': ", S2.startswith("s"))

print("ENDS WITH:")
print("S1 Ends with 'm': ", S1.endswith("m"))
print("S1 Ends with 'S': ", S2.endswith("S"))

print("\nSPLITTING STRINGS")
S1_SPLT = S1.split(" ")
print(S1_SPLT)

S2_SPLT = S2.split(" ")
print(S2_SPLT)

print("\nSTRING CONCATENATION")
print(S1 + S2)
print(S2 + S1)
print(S2 + ' using ' + S1)

import numpy as np

print("\t\t\t\t *******************************")
print("\t\t\t\t CREATING AND RESHAPING ARRAY")
print("\t\t\t\t *******************************")

array = np.arange(1, 8)

print("Original array", array)
print("Dimension of the Original Array", array.ndim)
print("Shape of the Original Array", array.shape)
print("Size of the Original Array", array.size)
print("Itemsize of the Original Array", array.itemsize)
print("Datatype of the Original Array", array.dtype)
print("Number of bytes occupied by the Original Array", array.nbytes)

array = np.arange(8).reshape(4,2)

print("Reshaped 2D array:\n", array)
print("Dimension of the Reshaped 2D Array", array.ndim)
print("Shape of the Reshaped 2D Array", array.shape)

array = np.arange(8).reshape(2, 2, 2)

print("3D array:\n", array)
print("Dimension of the Reshaped 3D Array", array.ndim)
print("Shape of the Reshaped 3D Array", array.shape)

print("Flattening the array to 1D array", array.flatten())
