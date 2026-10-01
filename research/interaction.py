# =====================================================
# FLOODGUARD-X
# Experiment 7: Variable Interaction Analysis
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


def calculate_fri(
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

    fri = (
        rainfall_score * 0.40
        +
        water_score * 0.40
        +
        soil_score * 0.20
    )

    return round(fri, 2)


# =====================================================
# INTERACTION SCENARIOS
# =====================================================

scenarios = [

    {
        "name": "High Rainfall + Low Water",
        "rainfall": 120,
        "water": 1.0,
        "soil": 50
    },

    {
        "name": "Low Rainfall + High Water",
        "rainfall": 30,
        "water": 4.0,
        "soil": 50
    },

    {
        "name": "High Rainfall + High Water",
        "rainfall": 120,
        "water": 4.0,
        "soil": 50
    },

    {
        "name": "High Rainfall + High Soil Moisture",
        "rainfall": 120,
        "water": 2.0,
        "soil": 95
    },

    {
        "name": "High Water + High Soil Moisture",
        "rainfall": 60,
        "water": 4.0,
        "soil": 95
    },

    {
        "name": "All High Conditions",
        "rainfall": 140,
        "water": 4.5,
        "soil": 95
    }

]


# =====================================================
# DISPLAY RESULTS
# =====================================================

print()

print("=" * 70)
print("FLOODGUARD-X — VARIABLE INTERACTION ANALYSIS")
print("=" * 70)

print()

print(
    f"{'Scenario':<40}"
    f"{'FRI':<10}"
)

print("-" * 55)


for scenario in scenarios:

    fri = calculate_fri(

        scenario["rainfall"],

        scenario["water"],

        scenario["soil"]

    )

    print(
        f"{scenario['name']:<40}"
        f"{fri:<10.2f}"
    )


# =====================================================
# INDIVIDUAL CONDITION COMPARISON
# =====================================================

print()

print("=" * 70)
print("INTERACTION COMPARISON")
print("=" * 70)

print()


high_rain_low_water = calculate_fri(
    120,
    1.0,
    50
)

low_rain_high_water = calculate_fri(
    30,
    4.0,
    50
)

high_rain_high_water = calculate_fri(
    120,
    4.0,
    50
)


print(
    "High Rainfall + Low Water:",
    high_rain_low_water
)

print(
    "Low Rainfall + High Water:",
    low_rain_high_water
)

print(
    "High Rainfall + High Water:",
    high_rain_high_water
)

print()

print(
    "Combined high rainfall and water level produces a"
)

print(
    "higher FRI than either condition alone."
)


# =====================================================
# ADDITIONAL INTERACTION COMPARISONS
# =====================================================

print()

print("=" * 70)
print("MULTI-VARIABLE INTERACTION")
print("=" * 70)

print()


rain_soil = calculate_fri(
    120,
    2.0,
    95
)

water_soil = calculate_fri(
    60,
    4.0,
    95
)

all_high = calculate_fri(
    140,
    4.5,
    95
)


print(
    "High Rainfall + High Soil:",
    rain_soil
)

print(
    "High Water + High Soil:",
    water_soil
)

print(
    "All High Conditions:",
    all_high
)


print()

print("=" * 70)

print(
    "Variable interaction analysis completed successfully."
)

print("=" * 70)
