function runSimulation() {

    // Generate simulated environmental conditions

    let rainfall = Math.floor(Math.random() * 150);

    let waterLevel = Number(
        (Math.random() * 5).toFixed(2)
    );

    let soilMoisture = Math.floor(
        Math.random() * 100
    );

    let temperature = Math.floor(
        20 + Math.random() * 20
    );


    // Display environmental values

    document.getElementById("rainfall").innerText =
        rainfall + " mm";

    document.getElementById("waterLevel").innerText =
        waterLevel + " m";

    document.getElementById("soilMoisture").innerText =
        soilMoisture + "%";

    document.getElementById("temperature").innerText =
        temperature + "°C";


    // Send data to the Risk Engine

    let result = calculateRisk(
        rainfall,
        waterLevel,
        soilMoisture
    );


    // Display risk result

    document.getElementById("riskLevel").innerText =
        result.level;

    document.getElementById("simulationResult").innerText =
        "Simulation completed. Risk score: " + result.score;

}
