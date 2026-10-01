# =====================================================
# FLOODGUARD-X
# Experiment 5: Anomaly Detection Analysis
# =====================================================


# -----------------------------------------------------
# ANOMALY DETECTION
# -----------------------------------------------------

def detect_anomalies(
    rainfall,
    water_level,
    soil_moisture
):

    anomaly_score = 0
    messages = []


    # Extremely high rainfall
    if rainfall >= 120:

        anomaly_score += 40

        messages.append(
            "Extremely high rainfall detected."
        )

    elif rainfall >= 90:

        anomaly_score += 20

        messages.append(
            "Unusually high rainfall detected."
        )


    # Critical water level
    if water_level >= 4:

        anomaly_score += 40

        messages.append(
            "Critical water level detected."
        )

    elif water_level >= 3:

        anomaly_score += 20

        messages.append(
            "Unusually high water level detected."
        )


    # Extremely high soil moisture
    if soil_moisture >= 90:

        anomaly_score += 20

        messages.append(
            "Extremely high soil moisture detected."
        )


    # Final anomaly decision
    if anomaly_score >= 40:

        anomaly = "ANOMALY DETECTED"

    else:

        anomaly = "NORMAL"


    return anomaly_score, anomaly, messages


# -----------------------------------------------------
# TEST SCENARIOS
# -----------------------------------------------------

scenarios = [

    {
        "name": "Normal Conditions",
        "rainfall": 20,
        "water": 1.2,
        "soil": 40
    },

    {
        "name": "High Rainfall",
        "rainfall": 100,
        "water": 2.0,
        "soil": 60
    },

    {
        "name": "Extreme Rainfall",
        "rainfall": 130,
        "water": 2.0,
        "soil": 60
    },

    {
        "name": "Critical Water Level",
        "rainfall": 60,
        "water": 4.2,
        "soil": 60
    },

    {
        "name": "Extreme Soil Moisture",
        "rainfall": 60,
        "water": 2.0,
        "soil": 95
    },

    {
        "name": "Multiple Anomalies",
        "rainfall": 140,
        "water": 4.5,
        "soil": 95
    }

]


# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

print()

print("=" * 70)

print(
    "FLOODGUARD-X — ANOMALY DETECTION ANALYSIS"
)

print("=" * 70)

print()


# -----------------------------------------------------
# RUN EXPERIMENT
# -----------------------------------------------------

for scenario in scenarios:

    score, anomaly, messages = detect_anomalies(

        scenario["rainfall"],

        scenario["water"],

        scenario["soil"]

    )


    print("-" * 70)

    print(
        "Scenario:",
        scenario["name"]
    )

    print(
        "Rainfall:",
        scenario["rainfall"],
        "mm"
    )

    print(
        "Water Level:",
        scenario["water"],
        "m"
    )

    print(
        "Soil Moisture:",
        scenario["soil"],
        "%"
    )

    print()

    print(
        "Anomaly Score:",
        score
    )

    print(
        "Result:",
        anomaly
    )


    if messages:

        print(
            "Detected Conditions:"
        )

        for message in messages:

            print(
                "-",
                message
            )

    else:

        print(
            "Detected Conditions: None"
        )


print()


# -----------------------------------------------------
# COMPLETE
# -----------------------------------------------------

print("=" * 70)

print(
    "Anomaly detection analysis completed successfully."
)

print("=" * 70)
