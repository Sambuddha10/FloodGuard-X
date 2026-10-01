import csv
import os


# =====================================================
# FLOODGUARD-X
# Experiment 1: Flood Risk Index Evaluation
# =====================================================


# -----------------------------------------------------
# FILE PATH
# -----------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(
    BASE_DIR,
    "scenarios.csv"
)


# -----------------------------------------------------
# FLOOD RISK INDEX
# -----------------------------------------------------

def calculate_fri(
    rainfall,
    water_level,
    soil_moisture
):

    # Normalize rainfall
    rainfall_score = min(
        100,
        max(
            0,
            (rainfall / 150) * 100
        )
    )


    # Normalize water level
    water_level_score = min(
        100,
        max(
            0,
            (water_level / 5) * 100
        )
    )


    # Soil moisture is already 0-100
    soil_moisture_score = min(
        100,
        max(
            0,
            soil_moisture
        )
    )


    # Weighted contributions
    rainfall_contribution = (
        rainfall_score * 0.40
    )


    water_level_contribution = (
        water_level_score * 0.40
    )


    soil_moisture_contribution = (
        soil_moisture_score * 0.20
    )


    # Final Flood Risk Index
    fri = (
        rainfall_contribution
        + water_level_contribution
        + soil_moisture_contribution
    )


    # Risk classification
    if fri >= 70:
        risk = "HIGH"

    elif fri >= 40:
        risk = "MEDIUM"

    else:
        risk = "LOW"


    return (
        round(fri, 2),
        risk
    )


# -----------------------------------------------------
# READ DATASET
# -----------------------------------------------------

results = []


with open(
    CSV_FILE,
    "r",
    newline=""
) as file:

    reader = csv.DictReader(file)


    for row in reader:

        rainfall = float(
            row["Rainfall_mm"]
        )

        water_level = float(
            row["Water_Level_m"]
        )

        soil_moisture = float(
            row["Soil_Moisture_percent"]
        )


        fri, risk = calculate_fri(

            rainfall,

            water_level,

            soil_moisture

        )


        results.append({

            "Scenario_ID":
                row["Scenario_ID"],

            "Rainfall":
                rainfall,

            "Water_Level":
                water_level,

            "Soil_Moisture":
                soil_moisture,

            "FRI":
                fri,

            "Risk":
                risk

        })


# -----------------------------------------------------
# DISPLAY RESULTS
# -----------------------------------------------------

print()
print("=" * 60)
print("FLOODGUARD-X — FLOOD RISK INDEX EXPERIMENT")
print("=" * 60)

print()

print(
    f"{'ID':<6}"
    f"{'Rain':<10}"
    f"{'Water':<10}"
    f"{'Soil':<10}"
    f"{'FRI':<10}"
    f"{'Risk'}"
)

print("-" * 60)


for result in results:

    print(

        f"{result['Scenario_ID']:<6}"

        f"{result['Rainfall']:<10.1f}"

        f"{result['Water_Level']:<10.1f}"

        f"{result['Soil_Moisture']:<10.1f}"

        f"{result['FRI']:<10.2f}"

        f"{result['Risk']}"

    )


# -----------------------------------------------------
# SUMMARY
# -----------------------------------------------------

low_count = 0
medium_count = 0
high_count = 0


for result in results:

    if result["Risk"] == "LOW":

        low_count += 1

    elif result["Risk"] == "MEDIUM":

        medium_count += 1

    elif result["Risk"] == "HIGH":

        high_count += 1


print()

print("=" * 60)
print("EXPERIMENT SUMMARY")
print("=" * 60)

print()

print(
    "Total scenarios:",
    len(results)
)

print(
    "LOW risk scenarios:",
    low_count
)

print(
    "MEDIUM risk scenarios:",
    medium_count
)

print(
    "HIGH risk scenarios:",
    high_count
)

print()

print(
    "Experiment completed successfully."
)

print("=" * 60)
