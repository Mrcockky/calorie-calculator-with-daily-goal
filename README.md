# Calorie Calculator

This Python script is a **Calorie Calculator** designed to help users understand their daily caloric needs based on their activity level, gender, weight, height, and age. By entering this information, the calculator provides tailored estimates on the number of calories required to maintain, lose, or gain weight. 

## Features
- **Personalized Caloric Needs**: Calculates daily caloric intake requirements tailored to your body and activity level.
- **Weight Management Options**: Provides recommendations for caloric intake based on goals to maintain, lose, or gain weight.
- **User-Friendly Prompts**: Guides you through entering your details with clear instructions.
- **Activity Levels**: Choose from five different levels of activity to refine your caloric needs.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
Clone or download this repository, then navigate to the script's directory in your terminal.

### Usage
1. Run the script with:
    ```py
    python calorie_calculator.py
    ```

2. Follow the prompts:
   - Select your gender.
   - Enter your weight in kilograms, height in centimeters, and age in years.
   - Choose your activity level based on your lifestyle from the options provided.

### Activity Levels
The program allows you to select from the following activity levels:
- **1**: No or minimal exercise.
- **2**: Light exercise (1-3 days per week).
- **3**: Moderate exercise (3-5 days per week).
- **4**: Intense exercise (6-7 days per week).
- **5**: Very intense exercise (physical job or twice-daily workouts).

### Example Output
After entering your information, the program calculates and displays your daily caloric needs for maintaining, losing, or gaining weight:
plaintext
Caloric Needs for Weight Management

To maintain your weight, you need:
2100 calories/day (100% of daily caloric intake).

For weight loss:
Mild weight loss (0.25 kg/week): 1806 calories/day (86% of daily caloric intake).
Weight loss (0.5 kg/week): 1512 calories/day (72% of daily caloric intake).
Extreme weight loss (1 kg/week): 924 calories/day (44% of daily caloric intake).

For weight gain:
Mild weight gain (0.25 kg/week): 2394 calories/day (114% of daily caloric intake).
Weight gain (0.5 kg/week): 2688 calories/day (128% of daily caloric intake).
Fast weight gain (1 kg/week): 3276 calories/day (156% of daily caloric intake)

### Formula Used

This script uses the **Harris-Benedict equation** for calculating the Basal Metabolic Rate (BMR) based on the user's gender, weight, height, and age. The BMR is then adjusted according to the activity level to determine daily caloric needs.

## Important Notes

- **Consult a healthcare professional**: If aiming for significant weight loss or gain, particularly if consuming less than 1,500 calories/day.
- **Maintain a balanced diet**: Ensure your nutritional needs are met even when adjusting calorie intake.
