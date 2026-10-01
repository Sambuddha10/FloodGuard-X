# =====================================================
# FLOODGUARD-X
# Experiment 4: Threshold Stability Analysis
# =====================================================

def classify_risk(fri):

    if fri >= 70:
        return "HIGH"

    elif fri >= 40:
        return "MEDIUM"

    else:
        return "LOW"


# -----------------------------------------------------
# TEST VALUES
# -----------------------------------------------------

threshold_values = [
    39.8,
    39.9,
    40.0,
    40.1,
    40.2,
    69.8,
    69.9,
    70.0,
    70.1,
    70.2
]


# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

print()

print("=" * 65)
print("FLOODGUARD-X — THRESHOLD STABILITY ANALYSIS")
print("=" * 65)

print()


# -----------------------------------------------------
# RISK THRESHOLDS
# -----------------------------------------------------

print("RISK CLASSIFICATION THRESHOLDS")
print("-" * 65)

print("FRI < 40        -> LOW")
print("40 <= FRI < 70  -> MEDIUM")
print("FRI >= 70       -> HIGH")

print()


# -----------------------------------------------------
# TEST RESULTS
# -----------------------------------------------------

print("THRESHOLD TEST RESULTS")
print("-" * 65)

print(
    f"{'FRI':<15}"
    f"{'Risk Level'}"
)

print("-" * 35)


for fri in threshold_values:

    risk = classify_risk(fri)

    print(
        f"{fri:<15.1f}"
        f"{risk}"
    )


# -----------------------------------------------------
# BOUNDARY CHECK
# -----------------------------------------------------

print()
print("=" * 65)
print("BOUNDARY CHECK")
print("=" * 65)

print()


# LOW -> MEDIUM

print("LOW -> MEDIUM boundary")

print(
    "FRI 39.9:",
    classify_risk(39.9)
)

print(
    "FRI 40.0:",
    classify_risk(40.0)
)

print(
    "FRI 40.1:",
    classify_risk(40.1)
)

print()


# MEDIUM -> HIGH

print("MEDIUM -> HIGH boundary")

print(
    "FRI 69.9:",
    classify_risk(69.9)
)

print(
    "FRI 70.0:",
    classify_risk(70.0)
)

print(
    "FRI 70.1:",
    classify_risk(70.1)
)


# -----------------------------------------------------
# COMPLETE
# -----------------------------------------------------

print()

print("=" * 65)

print(
    "Threshold stability analysis completed successfully."
)

print("=" * 65)
