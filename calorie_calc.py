print("""Get ready to take control of your nutritional journey. Our calorie calculator helps you understand your daily caloric needs based on your activity level and weight goals.

Simply enter your age, height, weight, and select your activity level to receive a tailored estimate of how many 
calories you need each day to maintain, lose, or gain weight. Start your path to a healthier lifestyle today!""")
a = int(input("put 1 for men and 2 for woman : "))
w = float(input("put your weight in kg : "))
h = float(input("put height in cm : "))
j = float(input("put age in years : "))
k = int(input("""Based on your lifestyle choice, please select one of the following:

1. no to less exercise.

2. light exercise.

3. moderate exercise.

4. intense exercise.

5. very intense exercise.

Choose the option that best describes your activity level : """))

"""Calculate your BMR You can use the Harris and Benedict formula to calculate your BMR based on your weight, height, 
and age:"""
bmr = 0
#For men
if a == 1:
    bmr = w * 13.7516 + 500.33 * h / 100 - 6.7550 * j + 66.479
#For woman
elif a == 2:
    bmr = 9.740 * w + 184.96 * h / 100 - 4.6756 * j + 655.0955
else:
    raise ValueError("Value should be between 1 and 2")

if k == 1:
    n = bmr * 1.2
    bmr = n
elif k == 2:
    m = bmr * 1.375
    bmr = m
elif k == 3:
    o = bmr * 1.55
    bmr = o
elif k == 4:
    p = bmr * 1.725
    bmr = p
elif k == 5:
    q = bmr * 1.9
    bmr = q

print(f"""Caloric Needs for Weight Management

To maintain your weight, you need:

{bmr:.0f} calories/day (100% of daily caloric intake).

For weight loss:

Mild weight loss (0.25 kg/week): {bmr * 86 / 100:.0f} calories/day (86% of daily caloric intake).

Weight loss (0.5 kg/week): {bmr * 72 / 100:.0f} calories/day (72% of daily caloric intake).

Extreme weight loss (1 kg/week): {bmr * 44 / 100:.0f} calories/day (44% of daily caloric intake).

Please consult with a doctor when losing 0.5 kg or more per week, as it requires consuming less than the minimum recommended 1,500 calories a day. You probably do not need to lose weight!

For weight gain:

Mild weight gain (0.25 kg/week): {bmr * 114 / 100:.0f} calories/day (114% of daily caloric intake).

Weight gain (0.5 kg/week): {bmr * 128 / 100:.0f} calories/day (128% of daily caloric intake).

Fast weight gain (1 kg/week): {bmr * 156 / 100:.0f} calories/day (156% of daily caloric intake).""")
