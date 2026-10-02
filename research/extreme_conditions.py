print("=" * 70)
print("FLOODGUARD-X — EXTREME CONDITION ANALYSIS")
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
# Extreme Environmental Conditions
# ------------------------------------------------------------

print("\nEXTREME ENVIRONMENTAL CONDITIONS")
print("-" * 70)

scenarios = [
    ("Maximum Model Inputs", 150, 5.0, 100),
    ("Extreme Rainfall", 300, 2.0, 60),
    ("Extreme Water Level", 60, 10.0, 60),
    ("Extreme Soil Moisture", 60, 2.0, 150),
    ("All Variables Extreme", 300, 10.0, 150),
    ("Zero Conditions", 0, 0.0, 0),
]

print(
    f"{'Scenario':<28}"
    f"{'Rainfall':<12}"
    f"{'Water':<10}"
    f"{'Soil':<10}"
    f"{'FRI':<10}"
    f"{'Class'}"
)
print("-" * 70)

for name, rainfall, water, soil in scenarios:
    fri = calculate_fri(rainfall, water, soil)

    print(
        f"{name:<28}"
        f"{rainfall:<12.1f}"
        f"{water:<10.1f}"
        f"{soil:<10.1f}"
        f"{fri:<10.2f}"
        f"{classify(fri)}"
    )


# ------------------------------------------------------------
# Boundary / Capping Check
# ------------------------------------------------------------

print("\nNORMALIZATION AND FRI BOUND CHECK")
print("-" * 70)

test_values = [
    ("Rainfall below minimum", -50, 2.0, 60),
    ("Rainfall above maximum", 300, 2.0, 60),
    ("Water below minimum", 60, -5.0, 60),
    ("Water above maximum", 60, 10.0, 60),
    ("Soil below minimum", 60, 2.0, -20),
    ("Soil above maximum", 60, 2.0, 150),
]

print(f"{'Test':<30}{'FRI':<10}{'Classification'}")
print("-" * 70)

for name, rainfall, water, soil in test_values:
    fri = calculate_fri(rainfall, water, soil)

    print(
        f"{name:<30}"
        f"{fri:<10.2f}"
        f"{classify(fri)}"
    )


# ------------------------------------------------------------
# FRI Range Verification
# ------------------------------------------------------------

print("\nFRI RANGE VERIFICATION")
print("-" * 70)

range_tests = [
    (0, 0, 0),
    (150, 5, 100),
    (300, 10, 150),
    (-100, -10, -50),
]

all_valid = True

for rainfall, water, soil in range_tests:
    fri = calculate_fri(rainfall, water, soil)

    valid = 0 <= fri <= 100

    print(
        f"Rainfall={rainfall}, "
        f"Water={water}, "
        f"Soil={soil} "
        f"-> FRI={fri:.2f} "
        f"-> {'VALID' if valid else 'INVALID'}"
    )

    if not valid:
        all_valid = False


print("\n" + "-" * 70)

if all_valid:
    print("RESULT: FRI RANGE CHECK PASSED")
    print("The calculated FRI remained within the expected 0–100 range.")
else:
    print("RESULT: FRI RANGE CHECK FAILED")
    print("The calculated FRI exceeded the expected 0–100 range.")


print("\n" + "=" * 70)
print("EXTREME CONDITION ANALYSIS COMPLETE")
print("=" * 70)
