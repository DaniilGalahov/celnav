import setup

import astrometry
import angle
import almanac


def parse_string(input_str): #ChatGPT made
    import calendar
    # Split the input string into components
    components = input_str.split()
    # Extract and parse the date
    date_str = components[0]
    year, month_str, day = date_str.split('-')
    Y = int(year)
    M = list(calendar.month_abbr).index(month_str[:3])  # Convert month abbreviation to number
    D = int(day)
    # Extract and parse the time
    time_str = components[1]
    h, m = map(int, time_str.split(':'))
    s = 0  # Seconds are not present in the input, default to 0
    # Extract azimuth and elevation angles
    az = float(components[3])
    el = float(components[4])
    return Y, M, D, h, m, s, az, el

def parse_file(file_name):  #ChatGPT made
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

def WriteStringsToFile(output_strings,file_name):
    with open(file_name, 'w') as file:
        file.writelines(output_strings)

def DeviationTestFor(celestialObjectName,phi,lambda_,inputStrings):
    outputStrings=[]
    for inputString in inputStrings:
        Y,M,D,h,m,s,azHrz,elHrz=parse_string(inputString)
        azLoc,elLoc=astrometry.AzElFor(celestialObjectName,phi,lambda_,Y,M,D,h,m,s) #no refraction correction, angles from pure vector.
        deltaAz=azHrz-azLoc
        deltaEl=elHrz-elLoc
        outputString=str(int(Y))+";"+str(int(M))+";"+str(round(azHrz,6))+";"+str(round(elHrz,6))+";"+str(round(deltaAz,6))+";"+str(round(deltaEl,6))+";\n"
        outputStrings.append(outputString)
    return outputStrings


#This tests using Horizon input for tests. Example in HrzMars.txt
# ----- Mars test -----
celestialObjectName="Mars"

phi=33.3562811 #Palomar observatory (precisely)
lambda_=-116.8651156

inputStrings=parse_file("Hrz"+celestialObjectName+".txt")
outputStrings=DeviationTestFor(celestialObjectName,phi,lambda_,inputStrings)
WriteStringsToFile(outputStrings,"DevTest"+celestialObjectName+".txt")
        
'''
So, basing on deep testing, I understood that Vallado's ephemerides providing position of a planet non-precisely.
They provide position WITHOUT refraction correction. Deviation of azimuth and elevation are systematic but very complex,
and I can not describe them mathematically.
I think that I should stop my tries of achieve high precision for now. I should finish all other parts of system, i.e., geodesy,
great circle navigation and star compass. After this, I should preform a complex test of precision for multiple positions on Earth,
to understand real precision of my algorithms.
'''
