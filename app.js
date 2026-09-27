function runSimulation() {


    // ========================================
    // GET SELECTED SCENARIO
    // ========================================

    const selectedScenario =
        document.getElementById(
            "scenarioSelect"
        ).value;


    // ========================================
    // GENERATE SCENARIO
    // ========================================

    const scenario =
        generateScenario(
            selectedScenario
        );


    // ========================================
    // DISPLAY ENVIRONMENTAL VALUES
    // ========================================

    document.getElementById(
        "rainfall"
    ).innerText =
        scenario.rainfall + " mm";


    document.getElementById(
        "waterLevel"
    ).innerText =
        scenario.waterLevel + " m";


    document.getElementById(
        "soilMoisture"
    ).innerText =
        scenario.soilMoisture + "%";


    document.getElementById(
        "temperature"
    ).innerText =
        scenario.temperature + "°C";


    // ========================================
    // RISK ENGINE
    // ========================================

    const result =
        calculateRisk(

            scenario.rainfall,

            scenario.waterLevel,

            scenario.soilMoisture

        );


    // ========================================
    // RISK ELEMENTS
    // ========================================

    const riskLevel =
        document.getElementById(
            "riskLevel"
        );


    const riskMessage =
        document.getElementById(
            "riskMessage"
        );


    const statusCard =
        document.querySelector(
            ".status-card"
        );


    // ========================================
    // UPDATE RISK LEVEL
    // ========================================

    riskLevel.innerText =
        result.level;


    riskLevel.classList.remove(

        "risk-low",

        "risk-medium",

        "risk-high"

    );


    // ========================================
    // LOW
    // ========================================

    if (
        result.level === "LOW"
    ) {

        riskLevel.classList.add(
            "risk-low"
        );


        riskMessage.innerText =
            "Current conditions indicate a low flood risk.";


        statusCard.style.border =
            "4px solid #22c55e";

    }


    // ========================================
    // MEDIUM
    // ========================================

    else if (
        result.level === "MEDIUM"
    ) {

        riskLevel.classList.add(
            "risk-medium"
        );


        riskMessage.innerText =
            "Moderate flood risk detected. Monitoring is recommended.";


        statusCard.style.border =
            "4px solid #f59e0b";

    }


    // ========================================
    // HIGH
    // ========================================

    else {

        riskLevel.classList.add(
            "risk-high"
        );


        riskMessage.innerText =
            "High flood risk detected. Immediate attention is recommended.";


        statusCard.style.border =
            "4px solid #ef4444";

    }


    // ========================================
    // SIMULATION RESULT
    // ========================================

    document.getElementById(
        "simulationResult"
    ).innerText =

        "Simulation completed. Risk score: " +
        result.score;


    // ========================================
    // ANOMALY DETECTION
    // ========================================

    const anomaly =
        detectAnomaly(

            scenario.rainfall,

            scenario.waterLevel,

            scenario.soilMoisture

        );


    // ========================================
    // ANOMALY ELEMENTS
    // ========================================

    const anomalyStatus =
        document.getElementById(
            "anomalyStatus"
        );


    const anomalyMessage =
        document.getElementById(
            "anomalyMessage"
        );


    // ========================================
    // REMOVE OLD ANOMALY STYLE
    // ========================================

    anomalyStatus.classList.remove(

        "anomaly-safe",

        "anomaly-warning"

    );


    // ========================================
    // ANOMALY DETECTED
    // ========================================

    if (
        anomaly.isAnomaly
    ) {

        anomalyStatus.innerText =
            "ANOMALY DETECTED";


        anomalyStatus.classList.add(
            "anomaly-warning"
        );


        anomalyMessage.innerText =

            anomaly.messages.join(
                " "
            );

    }


    // ========================================
    // NO ANOMALY
    // ========================================

    else {

        anomalyStatus.innerText =
            "NO ANOMALY";


        anomalyStatus.classList.add(
            "anomaly-safe"
        );


        anomalyMessage.innerText =
            "No unusual environmental conditions detected.";

    }


    // ========================================
    // SAVE TO RISK HISTORY
    // ========================================

    addRiskHistory(

        selectedScenario,

        scenario.rainfall,

        scenario.waterLevel,

        scenario.soilMoisture,

        scenario.temperature,

        result.score,

        result.level,

        anomaly.isAnomaly
            ? "YES"
            : "NO"

    );

}
