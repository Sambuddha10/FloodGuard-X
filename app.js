function runSimulation() {

    // Get selected scenario
    const selectedScenario =
        document.getElementById("scenarioSelect").value;

    // Generate scenario
    const scenario =
        generateScenario(selectedScenario);


    // =========================
    // DISPLAY SENSOR VALUES
    // =========================

    document.getElementById("rainfall").innerText =
        scenario.rainfall + " mm";

    document.getElementById("waterLevel").innerText =
        scenario.waterLevel + " m";

    document.getElementById("soilMoisture").innerText =
        scenario.soilMoisture + "%";

    document.getElementById("temperature").innerText =
        scenario.temperature + "°C";


    // =========================
    // FLOOD RISK CALCULATION
    // =========================

    const result = calculateRisk(
        scenario.rainfall,
        scenario.waterLevel,
        scenario.soilMoisture
    );

    const riskLevel =
        document.getElementById("riskLevel");

    const riskMessage =
        document.getElementById("riskMessage");

    const statusCard =
        document.querySelector(".status-card");


    riskLevel.innerText = result.level;

    riskLevel.classList.remove(
        "risk-low",
        "risk-medium",
        "risk-high"
    );


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

    else {

        riskLevel.classList.add("risk-high");

        riskMessage.innerText =
            "High flood risk detected. Immediate attention is recommended.";

        statusCard.style.border =
            "4px solid #ef4444";
    }


    document.getElementById("simulationResult").innerText =
        "Simulation completed. Risk score: " + result.score;


    // =========================
    // ANOMALY DETECTION
    // =========================

    let anomalyScore = 0;
    let anomalyMessages = [];


    // Rainfall anomaly
    if (scenario.rainfall >= 120) {

        anomalyScore += 40;

        anomalyMessages.push(
            "Extremely high rainfall detected."
        );
    }

    else if (scenario.rainfall >= 90) {

        anomalyScore += 20;

        anomalyMessages.push(
            "Unusually high rainfall detected."
        );
    }


    // Water level anomaly
    if (scenario.waterLevel >= 4) {

        anomalyScore += 40;

        anomalyMessages.push(
            "Critical water level detected."
        );
    }

    else if (scenario.waterLevel >= 3) {

        anomalyScore += 20;

        anomalyMessages.push(
            "Unusually high water level detected."
        );
    }


    // Soil moisture anomaly
    if (scenario.soilMoisture >= 90) {

        anomalyScore += 20;

        anomalyMessages.push(
            "Extremely high soil moisture detected."
        );
    }

    else if (scenario.soilMoisture >= 80) {

        anomalyScore += 10;

        anomalyMessages.push(
            "High soil moisture detected."
        );
    }


    // Get anomaly elements
    const anomalyStatus =
        document.getElementById("anomalyStatus");

    const anomalyMessage =
        document.getElementById("anomalyMessage");


    // Display anomaly
    if (anomalyScore >= 40) {

        anomalyStatus.innerText =
            "ANOMALY DETECTED";

        anomalyStatus.classList.remove(
            "anomaly-safe"
        );

        anomalyStatus.classList.add(
            "anomaly-warning"
        );

        anomalyMessage.innerText =
            anomalyMessages.join(" ");

    }

    else {

        anomalyStatus.innerText =
            "NO ANOMALY";

        anomalyStatus.classList.remove(
            "anomaly-warning"
        );

        anomalyStatus.classList.add(
            "anomaly-safe"
        );

        anomalyMessage.innerText =
            "No unusual environmental conditions detected.";
    }
}
