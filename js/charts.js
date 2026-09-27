let riskHistory = [];

function addRiskHistory(
    scenarioName,
    rainfall,
    waterLevel,
    soilMoisture,
    temperature,
    score,
    level,
    anomaly
) {
    riskHistory.push({
        scenario: scenarioName,
        rainfall: rainfall,
        waterLevel: waterLevel,
        soilMoisture: soilMoisture,
        temperature: temperature,
        score: score,
        level: level,
        anomaly: anomaly
    });

    updateRiskHistory();
}

function updateRiskHistory() {

    const historyElement =
        document.getElementById("riskHistory");

    if (!historyElement) {
        return;
    }

    historyElement.innerHTML = "";

    riskHistory.forEach((item, index) => {

        const row = document.createElement("div");

        row.className = "history-item";

        row.innerHTML = `
            <strong>Simulation ${index + 1}</strong><br>
            Scenario: ${item.scenario}<br>
            Rainfall: ${item.rainfall} mm<br>
            Water Level: ${item.waterLevel} m<br>
            Soil Moisture: ${item.soilMoisture}%<br>
            Temperature: ${item.temperature}°C<br>
            Risk: ${item.level}<br>
            Risk Score: ${item.score}<br>
            Anomaly: ${item.anomaly}
        `;

        historyElement.appendChild(row);
    });
}
