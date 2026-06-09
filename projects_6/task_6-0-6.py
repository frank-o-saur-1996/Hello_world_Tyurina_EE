import pandas as pd
df = pd.read_csv('wild_boars.csv')
q1_group = df.groupby('gender')['length_cm'].quantile(0.25)
q1_M = q1_group['Male']
q1_F = q1_group['Female']

q3_group = df.groupby('gender')['length_cm'].quantile(0.75)
q3_M = q3_group['Male']
q3_F = q3_group['Female']

iqr_M = q3_M - q1_M
iqr_F = q3_F - q1_F

with open('length_by_gender_boars.txt', 'w') as file:
    
    file.write(f"Q1_male (25%): {q1_M:.1f} cm")
    file.write(f"\nQ3_male (75%): {q3_M:.1f} cm")
    file.write(f"\nIQR_male: {iqr_M:.1f} cm")
    
    file.write(f"\n\nQ1_female (25%): {q1_F:.1f} cm")
    file.write(f"\nQ3_female (75%): {q3_F:.1f} cm")
    file.write(f"\nIQR_female: {iqr_F:.1f} cm")