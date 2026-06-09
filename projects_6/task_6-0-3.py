import pandas as pd
df = pd.read_csv('wild_boars.csv')
with open("median_boars.txt", "w", encoding="utf-8") as file:
    median_age = df['age_years'].median()
    file.write(f"median age is {median_age:.2f} years\n")
    
    median_weight = df['weight_kg'].median()
    file.write(f"median weight is {median_weight:.2f} kg\n")
    
    median_len = df['length_cm'].median()
    file.write(f"median length is {median_len:.2f} cm\n")

    median_shoulder_height = df['shoulder_height_cm'].median()
    file.write(f"median shoulder height is {median_shoulder_height:.2f} cm\n")

    median_tusk_length = df['tusk_length_cm'].median()
    file.write(f"median tusk length is {median_tusk_length:.2f} cm\n")

    median_litter_size = df['litter_size'].median()
    file.write(f"median litter size is {median_litter_size:.2f}\n")

    median_health_score = df['health_score'].median()
    file.write(f"median health score is {median_health_score:.2f}\n")

    median_territory = df['territory_ha'].median()
    file.write(f"median territory is {median_territory:.2f} ha\n")