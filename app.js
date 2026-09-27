// ======================================================
// FLOODGUARD-X
// COMPLETE SELF-CONTAINED APPLICATION
// ======================================================


// ======================================================
// SCENARIO GENERATOR
// ======================================================

function generateScenario(type) {

    if (type === "normal") {

        return {
            rainfall: 20,
            waterLevel: 1.2,
            soilMoisture: 40,
            temperature: 28
        };
    }


    if (type === "heavyRain") {

        return {
            rainfall: 110,
            waterLevel: 2.2,
            soilMoisture: 75,
            temperature: 25
        };
    }


    if (type === "risingWater") {

        return {
            rainfall: 70,
            waterLevel: 3.5,
            soilMoisture: 85,
            temperature: 26
        };
    }


    if (type === "extremeFlood") {

        return {
            rainfall: 140,
            waterLevel: 4.5,
            soilMoisture: 95,
            temperature: 24
        };
    }


    // RANDOM

    return {

        rainfall:
            Math.floor(Math.random() * 150),

        waterLevel:
            Number(
                (Math.random() * 5).toFixed(2)
            ),

        soilMoisture:
            Math.floor(Math.random() * 100),

        temperature:
            Math.floor(
                20 + Math.random() * 20
            )
    };
}


// ======================================================
// FLOOD RISK ENGINE
// ======================================================

function calculateRisk(
    rainfall,
    waterLevel,
    soilMoisture
) {

    let score = 0;


    // Rainfall

    if (rainfall >= 100) {

        score += 40;

    }

    else if (rainfall >= 50) {

        score += 20;
    }


    // Water level

    if (waterLevel >= 3) {

        score += 40;

    }

    else if (waterLevel >= 2) {

        score += 20;
    }


    // Soil moisture

    if (soilMoisture >= 80) {

        score += 20;
    }


    let level;


    if (score >= 70) {

        level = "HIGH";

    }

    else if (score >= 40) {

        level = "MEDIUM";

    }

    else {

        level = "LOW";
    }


    return {

        score: score,
        level: level
    };
}


// ======================================================
// ANOMALY DETECTION
// ======================================================

function detectAnomaly(
    rainfall,
    waterLevel,
    soilMoisture
) {

    let anomalyScore = 0;

    let messages = [];


    // Rainfall anomaly

    if (rainfall >= 120) {

        anomalyScore += 40;

        messages.push(
            "Extremely high rainfall detected."
        );

    }

    else if (rainfall >= 90) {

        anomalyScore += 20;

        messages.push(
            "Unusually high rainfall detected."
        );
    }


    // Water level anomaly

    if (waterLevel >= 4) {

        anomalyScore += 40;

        messages.push(
            "Critical water level detected."
        );

    }

    else if (waterLevel >= 3) {

        anomalyScore += 20;

        messages.push(
            "Unusually high water level detected."
        );
    }


    // Soil moisture anomaly

    if (soilMoisture >= 90) {

        anomalyScore += 20;

        messages.push(
            "Extremely high soil moisture detected."
        );

    }

    else if (soilMoisture >= 80) {

        anomalyScore += 10;

        messages.push(
            "High soil moisture detected."
        );
    }


    return {

        isAnomaly:
            anomalyScore >= 40,

        score:
            anomalyScore,

        messages:
            messages
    };
}


// ======================================================
// MAIN SIMULATION
// ======================================================

function runSimulation() {


    // --------------------------------------------------
    // GET SCENARIO
    // --------------------------------------------------

    const scenarioSelect =
        document.getElementById("scenarioSelect");


    const selectedScenario =
        scenarioSelect.value;


    // --------------------------------------------------
    // GENERATE DATA
    // --------------------------------------------------

    const scenario =
        generateScenario(
            selectedScenario
        );


    // --------------------------------------------------
    // UPDATE ENVIRONMENTAL VALUES
    // --------------------------------------------------

    document.getElementById("rainfall").innerText =
        scenario.rainfall + " mm";


    document.getElementById("waterLevel").innerText =
        scenario.waterLevel + " m";


    document.getElementById("soilMoisture").innerText =
        scenario.soilMoisture + "%";


    document.getElementById("temperature").innerText =
        scenario.temperature + "°C";


    // --------------------------------------------------
    // CALCULATE RISK
    // --------------------------------------------------

    const result =
        calculateRisk(

            scenario.rainfall,

            scenario.waterLevel,

            scenario.soilMoisture
        );


    // --------------------------------------------------
    // RISK UI
    // --------------------------------------------------

    const riskLevel =
        document.getElementById("riskLevel");


    const riskMessage =
        document.getElementById("riskMessage");


    const statusCard =
        document.querySelector(".status-card");


    riskLevel.classList.remove(
        "risk-low",
        "risk-medium",
        "risk-high"
    );


    if (result.level === "LOW") {

        riskLevel.innerText =
            "LOW";

        riskLevel.classList.add(
            "risk-low"
        );

        riskMessage.innerText =
            "Current conditions indicate a low flood risk.";

        statusCard.style.border =
            "4px solid #22c55e";
    }


    else if (result.level === "MEDIUM") {

        riskLevel.innerText =
            "MEDIUM";

        riskLevel.classList.add(
            "risk-medium"
        );

        riskMessage.innerText =
            "Moderate flood risk detected. Monitoring is recommended.";

        statusCard.style.border =
            "4px solid #f59e0b";
    }


    else {

        riskLevel.innerText =
            "HIGH";

        riskLevel.classList.add(
            "risk-high"
        );

        riskMessage.innerText =
            "High flood risk detected. Immediate attention is recommended.";

        statusCard.style.border =
            "4px solid #ef4444";
    }


    // --------------------------------------------------
    // SIMULATION RESULT
    // --------------------------------------------------

    document.getElementById(
        "simulationResult"
    ).innerText =

        "Simulation completed. Risk score: " +
        result.score;


    // --------------------------------------------------
    // ANOMALY DETECTION
    // --------------------------------------------------

    const anomaly =
        detectAnomaly(

            scenario.rainfall,

            scenario.waterLevel,

            scenario.soilMoisture
        );


    const anomalyStatus =
        document.getElementById(
            "anomalyStatus"
        );


    const anomalyMessage =
        document.getElementById(
            "anomalyMessage"
        );


    anomalyStatus.classList.remove(
        "anomaly-safe",
        "anomaly-warning"
    );


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


    // --------------------------------------------------
    // RISK HISTORY
    // --------------------------------------------------

    const historyElement =
        document.getElementById(
            "riskHistory"
        );


    if (!historyElement) {

        alert(
            "Risk History element not found."
        );

        return;
    }



    // Create record

    const historyItem =
        document.createElement(
            "div"
        );


    historyItem.className =
        "history-item";


    historyItem.innerHTML = `

        <strong>
            Simulation Recorded
        </strong>

        <br><br>

        <strong>Scenario:</strong>
        ${selectedScenario}

        <br>

        <strong>Rainfall:</strong>
        ${scenario.rainfall} mm

        <br>

        <strong>Water Level:</strong>
        ${scenario.waterLevel} m

        <br>

        <strong>Soil Moisture:</strong>
        ${scenario.soilMoisture}%

        <br>

        <strong>Temperature:</strong>
        ${scenario.temperature}°C

        <br>

        <strong>Risk:</strong>
        ${result.level}

        <br>

        <strong>Risk Score:</strong>
        ${result.score}

        <br>

        <strong>Anomaly:</strong>
        ${anomaly.isAnomaly ? "YES" : "NO"}

    `;


    // Add record

    historyElement.appendChild(
        historyItem
    );


    // --------------------------------------------------
    // FINAL CONFIRMATION
    // --------------------------------------------------

    console.log(
        "FloodGuard-X simulation recorded successfully."
    );

}
