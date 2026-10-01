# =====================================================
# FLOODGUARD-X
# Experiment 6: Variable Influence Analysis
# =====================================================


def normalize_rainfall(rainfall):

    return min(
        100,
        max(
            0,
            (rainfall / 150) * 100
        )
    )


def normalize_water_level(water_level):

    return min(
        100,
        max(
            0,
            (water_level / 5) * 100
        )
    )


def normalize_soil_moisture(soil_moisture):

    return min(
        100,
        max(
            0,
            soil_moisture
        )
    )


def calculate_contributions(
    rainfall,
    water_level,
    soil_moisture
):

    rainfall_score = normalize_rainfall(
        rainfall
    )

    water_score = normalize_water_level(
        water_level
    )

    soil_score = normalize_soil_moisture(
        soil_moisture
    )


    rainfall_contribution = (
        rainfall_score * 0.40
    )

    water_contribution = (
        water_score * 0.40
    )

    soil_contribution = (
        soil_score * 0.20
    )


    fri = (
        rainfall_contribution
        + water_contribution
        + soil_contribution
    )


    return (
        rainfall_contribution,
        water_contribution,
        soil_contribution,
        round(fri, 2)
    )


# =====================================================
# TEST SCENARIOS
# =====================================================

scenarios = [

    {
        "name": "Normal Conditions",
        "rainfall": 20,
        "water": 1.2,
        "soil": 40
    },

    {
        "name": "Heavy Rainfall",
        "rainfall": 110,
        "water": 2.2,
        "soil": 75
    },

    {
        "name": "Rising Water Level",
        "rainfall": 70,
        "water": 3.5,
        "soil": 85
    },

    {
        "name": "Extreme Flood",
        "rainfall": 140,
        "water": 4.5,
        "soil": 95
    }

]


# =====================================================
# ANALYSIS
# =====================================================

total_rainfall = 0
total_water = 0
total_soil = 0


print()

print("=" * 70)
print("FLOODGUARD-X — VARIABLE INFLUENCE ANALYSIS")
print("=" * 70)

print()


for scenario in scenarios:

    (
        rainfall_contribution,
        water_contribution,
        soil_contribution,
        fri
    ) = calculate_contributions(

        scenario["rainfall"],

        scenario["water"],

        scenario["soil"]

    )


    total_rainfall += rainfall_contribution
    total_water += water_contribution
    total_soil += soil_contribution


    print("-" * 70)

    print(
        "Scenario:",
        scenario["name"]
    )

    print(
        "Rainfall Contribution:",
        round(rainfall_contribution, 2)
    )

    print(
        "Water Level Contribution:",
        round(water_contribution, 2)
    )

    print(
        "Soil Moisture Contribution:",
        round(soil_contribution, 2)
    )

    print(
        "Total FRI:",
        fri
    )

    print()


# =====================================================
# AVERAGE CONTRIBUTION
# =====================================================

number_of_scenarios = len(
    scenarios
)

average_rainfall = (
    total_rainfall
    / number_of_scenarios
)

average_water = (
    total_water
    / number_of_scenarios
)

average_soil = (
    total_soil
    / number_of_scenarios
)


total_average = (
    average_rainfall
    + average_water
    + average_soil
)


print("=" * 70)
print("AVERAGE VARIABLE CONTRIBUTION")
print("=" * 70)

print()

print(
    "Rainfall:",
    round(average_rainfall, 2)
)

print(
    "Water Level:",
    round(average_water, 2)
)

print(
    "Soil Moisture:",
    round(average_soil, 2)
)

print()

print("=" * 70)
print("RELATIVE CONTRIBUTION")
print("=" * 70)

print()


rainfall_percentage = (
    average_rainfall
    / total_average
    * 100
)

water_percentage = (
    average_water
    / total_average
    * 100
)

soil_percentage = (
    average_soil
    / total_average
    * 100
)


print(
    "Rainfall:",
    round(rainfall_percentage, 2),
    "%"
)

print(
    "Water Level:",
    round(water_percentage, 2),
    "%"
)

print(
    "Soil Moisture:",
    round(soil_percentage, 2),
    "%"
)


print()

print("=" * 70)
print(
    "Variable influence analysis completed successfully."
)
print("=" * 70)
