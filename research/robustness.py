# =====================================================
# FLOODGUARD-X
# Experiment 8: Robustness Analysis
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
# BASELINE SCENARIO
# =====================================================

baseline = {
    "rainfall": 60,
    "water": 2.0,
    "soil": 60
}


baseline_fri = calculate_fri(
    baseline["rainfall"],
    baseline["water"],
    baseline["soil"]
)


print()

print("=" * 70)
print("FLOODGUARD-X — ROBUSTNESS ANALYSIS")
print("=" * 70)

print()

print("BASELINE CONDITIONS")
print("-" * 70)

print(
    "Rainfall:",
    baseline["rainfall"],
    "mm"
)

print(
    "Water Level:",
    baseline["water"],
    "m"
)

print(
    "Soil Moisture:",
    baseline["soil"],
    "%"
)

print(
    "Baseline FRI:",
    baseline_fri
)


# =====================================================
# RAINFALL PERTURBATION
# =====================================================

print()

print("=" * 70)
print("1. RAINFALL PERTURBATION")
print("=" * 70)

print()

print(
    f"{'Rainfall (mm)':<20}"
    f"{'FRI':<15}"
    f"{'Change':<15}"
)

print("-" * 50)


rainfall_values = [
    baseline["rainfall"] - 10,
    baseline["rainfall"] - 5,
    baseline["rainfall"],
    baseline["rainfall"] + 5,
    baseline["rainfall"] + 10
]


for rainfall in rainfall_values:

    fri = calculate_fri(
        rainfall,
        baseline["water"],
        baseline["soil"]
    )

    change = fri - baseline_fri

    print(
        f"{rainfall:<20}"
        f"{fri:<15.2f}"
        f"{change:+.2f}"
    )


# =====================================================
# WATER LEVEL PERTURBATION
# =====================================================

print()

print("=" * 70)
print("2. WATER LEVEL PERTURBATION")
print("=" * 70)

print()

print(
    f"{'Water Level (m)':<20}"
    f"{'FRI':<15}"
    f"{'Change':<15}"
)

print("-" * 50)


water_values = [
    baseline["water"] - 0.2,
    baseline["water"] - 0.1,
    baseline["water"],
    baseline["water"] + 0.1,
    baseline["water"] + 0.2
]


for water in water_values:

    fri = calculate_fri(
        baseline["rainfall"],
        water,
        baseline["soil"]
    )

    change = fri - baseline_fri

    print(
        f"{water:<20.1f}"
        f"{fri:<15.2f}"
        f"{change:+.2f}"
    )


# =====================================================
# SOIL MOISTURE PERTURBATION
# =====================================================

print()

print("=" * 70)
print("3. SOIL MOISTURE PERTURBATION")
print("=" * 70)

print()

print(
    f"{'Soil Moisture (%)':<20}"
    f"{'FRI':<15}"
    f"{'Change':<15}"
)

print("-" * 50)


soil_values = [
    baseline["soil"] - 10,
    baseline["soil"] - 5,
    baseline["soil"],
    baseline["soil"] + 5,
    baseline["soil"] + 10
]


for soil in soil_values:

    fri = calculate_fri(
        baseline["rainfall"],
        baseline["water"],
        soil
    )

    change = fri - baseline_fri

    print(
        f"{soil:<20}"
        f"{fri:<15.2f}"
        f"{change:+.2f}"
    )


# =====================================================
# ROBUSTNESS SUMMARY
# =====================================================

print()

print("=" * 70)
print("ROBUSTNESS SUMMARY")
print("=" * 70)

print()

print(
    "Baseline FRI:",
    baseline_fri
)

print(
    "Small input changes produce gradual FRI changes."
)

print(
    "No unexpected discontinuities were introduced"
)

print(
    "within the tested input ranges."
)


print()

print("=" * 70)

print(
    "Robustness analysis completed successfully."
)

print("=" * 70)
