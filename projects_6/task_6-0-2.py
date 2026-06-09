import pandas as pd
df = pd.read_csv('wild_boars.csv')
with open("mean_boars.txt", "w", encoding="utf-8") as file:
    average_age = df['age_years'].mean()
    file.write(f"average age is {average_age:.2f} years\n")
    
    average_weight = df['weight_kg'].mean()
    file.write(f"average weight is {average_weight:.2f} kg\n")
    
    average_len = df['length_cm'].mean()
    file.write(f"average length is {average_len:.2f} cm\n")

    average_shoulder_height = df['shoulder_height_cm'].mean()
    file.write(f"average shoulder height is {average_shoulder_height:.2f} cm\n")

    average_tusk_length = df['tusk_length_cm'].mean()
    file.write(f"average tusk length is {average_tusk_length:.2f} cm\n")

    average_litter_size = df['litter_size'].mean()
    file.write(f"average litter size is {average_litter_size:.2f}\n")

    average_health_score = df['health_score'].mean()
    file.write(f"average health score is {average_health_score:.2f}\n")

    average_territory = df['territory_ha'].mean()
    file.write(f"average territory is {average_territory:.2f} ha\n")