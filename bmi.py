weight = int(input('Enter your weight: '))
height = float(input('Enter your height(separate by dot .): '))
bmi = float

bmi = weight / (height * height)
if bmi < 20:
  print('Underweight')
else:
  if bmi <= 25:
    print('Normal weight')
  else:
    if bmi <= 30:
      print('Overweight')
    else:
      if bmi <= 35:
        print('Obese')
      else:
        print('Obesity mobid')