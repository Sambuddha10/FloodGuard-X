print("=" * 70)
print("FLOODGUARD-X — BOUNDARY SENSITIVITY ANALYSIS")
print("=" * 70)


def calculate_fri(rainfall, water_level, soil_moisture):
    rainfall_score = min(100, max(0, rainfall / 150 * 100))
    water_score = min(100, max(0, water_level / 5 * 100))
    soil_score = min(100, max(0, soil_moisture))

    fri = (
        0.40 * rainfall_score
        + 0.40 * water_score
        + 0.20 * soil_score
    )

    return fri


def classify(fri):
    if fri >= 70:
        return "HIGH"
    elif fri >= 40:
        return "MEDIUM"
    else:
        return "LOW"


# ------------------------------------------------------------
# Boundary 1: FRI = 40
# ------------------------------------------------------------

print("\nBOUNDARY 1 — LOW / MEDIUM")
print("-" * 70)

print(f"{'FRI':<10}{'Classification'}")
print("-" * 70)

for fri in [39.0, 39.5, 39.9, 40.0, 40.1, 40.5, 41.0]:
    print(f"{fri:<10.1f}{classify(fri)}")


# ------------------------------------------------------------
# Boundary 2: FRI = 70
# ------------------------------------------------------------

print("\nBOUNDARY 2 — MEDIUM / HIGH")
print("-" * 70)

print(f"{'FRI':<10}{'Classification'}")
print("-" * 70)

for fri in [69.0, 69.5, 69.9, 70.0, 70.1, 70.5, 71.0]:
    print(f"{fri:<10.1f}{classify(fri)}")


# ------------------------------------------------------------
# Environmental perturbation around FRI = 40
# ------------------------------------------------------------

print("\nENVIRONMENTAL SENSITIVITY AROUND FRI = 40")
print("-" * 70)

baseline = {
    "rainfall": 60,
    "water_level": 2.0,
    "soil_moisture": 60
}

print(
    f"Baseline: Rainfall={baseline['rainfall']} mm, "
    f"Water={baseline['water_level']} m, "
    f"Soil={baseline['soil_moisture']} %"
)

baseline_fri = calculate_fri(
    baseline["rainfall"],
    baseline["water_level"],
    baseline["soil_moisture"]
)

print(f"Baseline FRI: {baseline_fri:.2f}")
print(f"Classification: {classify(baseline_fri)}")

print("\nSmall environmental changes:")
print(f"{'Change':<25}{'FRI':<10}{'Classification'}")
print("-" * 70)

tests = [
    ("Rainfall -5 mm", 55, 2.0, 60),
    ("Rainfall +5 mm", 65, 2.0, 60),
    ("Water -0.1 m", 60, 1.9, 60),
    ("Water +0.1 m", 60, 2.1, 60),
    ("Soil -5 %", 60, 2.0, 55),
    ("Soil +5 %", 60, 2.0, 65),
]

for name, rainfall, water, soil in tests:
    fri = calculate_fri(rainfall, water, soil)
    print(f"{name:<25}{fri:<10.2f}{classify(fri)}")


# ------------------------------------------------------------
# Environmental perturbation around FRI = 70
# ------------------------------------------------------------

print("\nENVIRONMENTAL SENSITIVITY AROUND FRI = 70")
print("-" * 70)

baseline_high = {
    "rainfall": 100,
    "water_level": 3.0,
    "soil_moisture": 70
}

baseline_high_fri = calculate_fri(
    baseline_high["rainfall"],
    baseline_high["water_level"],
    baseline_high["soil_moisture"]
)

print(
    f"Baseline: Rainfall={baseline_high['rainfall']} mm, "
    f"Water={baseline_high['water_level']} m, "
    f"Soil={baseline_high['soil_moisture']} %"
)

print(f"Baseline FRI: {baseline_high_fri:.2f}")
print(f"Classification: {classify(baseline_high_fri)}")

print("\nSmall environmental changes:")
print(f"{'Change':<25}{'FRI':<10}{'Classification'}")
print("-" * 70)

tests_high = [
    ("Rainfall -5 mm", 95, 3.0, 70),
    ("Rainfall +5 mm", 105, 3.0, 70),
    ("Water -0.1 m", 100, 2.9, 70),
    ("Water +0.1 m", 100, 3.1, 70),
    ("Soil -5 %", 100, 3.0, 65),
    ("Soil +5 %", 100, 3.0, 75),
]

for name, rainfall, water, soil in tests_high:
    fri = calculate_fri(rainfall, water, soil)
    print(f"{name:<25}{fri:<10.2f}{classify(fri)}")


print("\n" + "=" * 70)
print("BOUNDARY SENSITIVITY ANALYSIS COMPLETE")
print("=" * 70)
