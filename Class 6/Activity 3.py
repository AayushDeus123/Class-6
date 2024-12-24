#Calculating the BMI
h = float(input('Enter your height in CentiMeters (cm) : '))
w = float(input('Enter your weight in KiloGrams (kg) : '))
bmi = w/(h/100)**2
if bmi<18.4:
    print('You are underweight')
elif bmi>=18.4 and bmi<=24.9:
    print('You are healthy')
elif bmi>=25 and bmi<=29.9:
    print('You are overweight')
elif bmi>=30 and bmi<=34.9:
    print('You are severely overweight')
else:
    print('You are obese')
    