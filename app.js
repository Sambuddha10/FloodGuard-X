function runSimulation() {

    // Generate a simulated environmental scenario

    const scenario = generateScenario();


    // Display environmental values

    document.getElementById("rainfall").innerText =
        scenario.rainfall + " mm";

    document.getElementById("waterLevel").innerText =
        scenario.waterLevel + " m";

    document.getElementById("soilMoisture").innerText =
        scenario.soilMoisture + "%";

    document.getElementById("temperature").innerText =
        scenario.temperature + "°C";


    // Send scenario to the Risk Engine

    const result = calculateRisk(
        scenario.rainfall,
        scenario.waterLevel,
        scenario.soilMoisture
    );


    // Display risk result

    document.getElementById("riskLevel").innerText =
        result.level;

    document.getElementById("simulationResult").innerText =
        "Simulation completed. Risk score: " + result.score;
}
