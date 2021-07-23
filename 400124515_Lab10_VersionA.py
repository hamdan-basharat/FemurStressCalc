'''
Hamdan Basharat
4000124515
basham1
IBEHS 1P10
Lab 10 Version A Assignment
Novenmber 17th, 2017
This program calculates the medial and lateral stress upon a femur through a series of defined equations.
'''

#define constants
g = 9.81
A = 364.42
I = 39039
y = 16.5

'''defining the function to calculate axial load
@param: float m
@return: axialLoad                            '''
def calculateAxialLoad(m):
    W = m*g
    axialLoad = 3.5*W
    return(axialLoad)

'''defining the function to calculate bending moment
@param: float m, float x
@return: bendMoment                              '''
def calculateBendingMoment(m,x):
    W = m*g
    F = 3.5*W
    bendMoment = F*x
    return(bendMoment)

'''defining the function to calculate axial stress
@param: float m
@return: axialStress                            '''
def calculateAxialStress(m):
    axialStress = calculateAxialLoad(m)/A
    return(axialStress)

'''defining the function to calculate bending stress
@param: float m, float x
@return: bendingStress                           '''
def calculateBendingStress(m,x):
    bendingStress = (calculateBendingMoment(m,x)*y)/I
    return(bendingStress)

'''defining the function to calculate medial stress
@param: float m, float x
@return: medStress                              '''
def calculateMedialStress(m,x):
    medStress = -(calculateAxialStress(m))-(calculateBendingStress(m,x))
    return(medStress)

'''defining the function to calculate lateral stress
@param: float m, float x
@return: latStress                               '''
def calculateLateralStress(m,x):
    latStress = -(calculateAxialStress(m))+(calculateBendingStress(m,x))
    return(latStress)

#request the user to input values for variables. Values were saved as floats
m = float(input("Please enter the subject's mass (kg): "))
x = float(input("Please enter the distance from the centre of the femoral head to the mid-axis (m): "))

#prints the calculated values for medial and lateral stress
print("The medial stress of the femoral diaphysis is " + str(calculateMedialStress(m,x)) + " N/mm^2")
print("The lateral stress of the femoral diaphysis is " + str(calculateLateralStress(m,x)) + " N/mm^2")
          



