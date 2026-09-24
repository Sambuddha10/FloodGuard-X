function runSimulation() {

    // Get selected scenario
    const selectedScenario =
        document.getElementById("scenarioSelect").value;


    // Generate scenario
    const scenario =
        generateScenario(selectedScenario);


    // Display environmental values
    document.getElementById("rainfall").innerText =
        scenario.rainfall + " mm";

    document.getElementById("waterLevel").innerText =
        scenario.waterLevel + " m";

    document.getElementById("soilMoisture").innerText =
        scenario.soilMoisture + "%";

    document.getElementById("temperature").innerText =
        scenario.temperature + "°C";


    // Calculate flood risk
    const result = calculateRisk(
        scenario.rainfall,
        scenario.waterLevel,
        scenario.soilMoisture
    );


    // Get risk elements
    const riskLevel =
        document.getElementById("riskLevel");

    const riskMessage =
        document.getElementById("riskMessage");

    const statusCard =
        document.querySelector(".status-card");


    // Display risk level
    riskLevel.innerText = result.level;


    // Remove old risk styles
    riskLevel.classList.remove(
        "risk-low",
        "risk-medium",
        "risk-high"
    );


    // Update risk appearance
    if (result.level === "LOW") {

        riskLevel.classList.add("risk-low");

        riskMessage.innerText =
            "Current conditions indicate a low flood risk.";

        statusCard.style.border =
            "4px solid #22c55e";
    }

    else if (result.level === "MEDIUM") {

        riskLevel.classList.add("risk-medium");

        riskMessage.innerText =
            "Moderate flood risk detected. Monitoring is recommended.";

        statusCard.style.border =
            "4px solid #f59e0b";
    }

    else if (result.level === "HIGH") {

        riskLevel.classList.add("risk-high");

        riskMessage.innerText =
            "High flood risk detected. Immediate attention is recommended.";

        statusCard.style.border =
            "4px solid #ef4444";
    }


    // Display risk score
    document.getElementById("simulationResult").innerText =
        "Simulation completed. Risk score: " + result.score;


    // =========================
    // ANOMALY DETECTION
    // =========================

    const anomaly = detectAnomaly(
        scenario.rainfall,
        scenario.waterLevel,
        scenario.soilMoisture
    );


    // Get anomaly elements
    const anomalyStatus =
        document.getElementById("anomalyStatus");

    const anomalyMessage =
        document.getElementById("anomalyMessage");


    // Remove previous anomaly styles
    anomalyStatus.classList.remove(
        "anomaly-safe",
        "anomaly-warning"
    );


    // Display anomaly result
    if (anomaly.isAnomaly) {

        anomalyStatus.innerText =
            "ANOMALY DETECTED";

        anomalyStatus.classList.add(
            "anomaly-warning"
        );

        anomalyMessage.innerText =
            anomaly.messages.join(" ");

    }

    else {

        anomalyStatus.innerText =
            "NO ANOMALY";

        anomalyStatus.classList.add(
            "anomaly-safe"
        );

        anomalyMessage.innerText =
            "No unusual environmental conditions detected.";
    }
}
