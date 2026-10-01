import csv
import os


# =====================================================
# FLOODGUARD-X
# Experiment 1: Model Evaluation
# =====================================================


# -----------------------------------------------------
# FILE PATH
# -----------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

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

    rainfall_score = min(
        100,
        max(
            0,
            (rainfall / 150) * 100
        )
    )

    water_level_score = min(
        100,
        max(
            0,
            (water_level / 5) * 100
        )
    )

    soil_moisture_score = min(
        100,
        max(
            0,
            soil_moisture
        )
    )


    fri = (

        rainfall_score * 0.40

        +

        water_level_score * 0.40

        +

        soil_moisture_score * 0.20

    )


    if fri >= 70:

        risk = "HIGH"

    elif fri >= 40:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    return round(fri, 2), risk


# -----------------------------------------------------
# LOAD DATA
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
            "fri": fri,
            "risk": risk
        })


# -----------------------------------------------------
# BASIC STATISTICS
# -----------------------------------------------------

total = len(results)


fri_values = [

    result["fri"]

    for result in results

]


average_fri = (
    sum(fri_values) / total
)


minimum_fri = min(
    fri_values
)


maximum_fri = max(
    fri_values
)


# -----------------------------------------------------
# RISK COUNTS
# -----------------------------------------------------

low_count = sum(

    1

    for result in results

    if result["risk"] == "LOW"

)


medium_count = sum(

    1

    for result in results

    if result["risk"] == "MEDIUM"

)


high_count = sum(

    1

    for result in results

    if result["risk"] == "HIGH"

)


# -----------------------------------------------------
# CONSISTENCY CHECK
# -----------------------------------------------------

classification_errors = 0


for result in results:

    fri = result["fri"]

    risk = result["risk"]


    expected_risk = None


    if fri >= 70:

        expected_risk = "HIGH"

    elif fri >= 40:

        expected_risk = "MEDIUM"

    else:

        expected_risk = "LOW"


    if risk != expected_risk:

        classification_errors += 1


# -----------------------------------------------------
# DISPLAY RESULTS
# -----------------------------------------------------

print()

print("=" * 60)

print(
    "FLOODGUARD-X — MODEL EVALUATION"
)

print("=" * 60)

print()


print(
    "Total scenarios:",
    total
)

print()


print(
    "Average FRI:",
    round(
        average_fri,
        2
    )
)

print(
    "Minimum FRI:",
    minimum_fri
)

print(
    "Maximum FRI:",
    maximum_fri
)

print()


print(
    "LOW risk:",
    low_count
)

print(
    "MEDIUM risk:",
    medium_count
)

print(
    "HIGH risk:",
    high_count
)

print()


print(
    "Classification consistency check:"
)


if classification_errors == 0:

    print(
        "PASSED — "
        "All classifications match "
        "their FRI thresholds."
    )

else:

    print(
        "FAILED —",
        classification_errors,
        "classification errors found."
    )


print()

print("=" * 60)
