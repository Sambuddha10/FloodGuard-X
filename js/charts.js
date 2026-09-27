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

        scenario:
            scenarioName,

        rainfall:
            rainfall,

        waterLevel:
            waterLevel,

        soilMoisture:
            soilMoisture,

        temperature:
            temperature,

        score:
            score,

        level:
            level,

        anomaly:
            anomaly
    });


    // Keep latest 10 simulations

    if (riskHistory.length > 10) {

        riskHistory.shift();

    }


    updateRiskHistory();
}


function updateRiskHistory() {

    const historyElement =
        document.getElementById(
            "riskHistory"
        );


    if (!historyElement) {

        return;

    }


    historyElement.innerHTML = "";


    riskHistory.forEach(
        (item, index) => {

            const row =
                document.createElement(
                    "div"
                );


            row.className =
                "history-item";


            row.innerText =
                "Simulation " +
                (index + 1) +

                " | Scenario: " +
                item.scenario +

                " | Rain: " +
                item.rainfall +
                " mm" +

                " | Water: " +
                item.waterLevel +
                " m" +

                " | Soil: " +
                item.soilMoisture +
                "%" +

                " | Temperature: " +
                item.temperature +
                "°C" +

                " | Risk: " +
                item.level +

                " | Score: " +
                item.score +

                " | Anomaly: " +
                item.anomaly;


            historyElement.appendChild(
                row
            );
        }
    );
}
