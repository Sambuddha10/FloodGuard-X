function runSimulation() {

    // Generate simulated environmental conditions

    let rainfall = Math.floor(Math.random() * 150);
    let waterLevel = (Math.random() * 5).toFixed(2);
    let soilMoisture = Math.floor(Math.random() * 100);
    let temperature = Math.floor(20 + Math.random() * 20);


    // Display the simulated values

    document.getElementById("rainfall").innerText =
        rainfall + " mm";

    document.getElementById("waterLevel").innerText =
        waterLevel + " m";

    document.getElementById("soilMoisture").innerText =
        soilMoisture + "%";

    document.getElementById("temperature").innerText =
        temperature + "°C";


    // Simple initial risk calculation

    let riskScore = 0;


    if (rainfall > 100) {
        riskScore += 40;
    } else if (rainfall > 50) {
        riskScore += 20;
    }


    if (waterLevel > 3) {
        riskScore += 40;
    } else if (waterLevel > 2) {
        riskScore += 20;
    }


    if (soilMoisture > 80) {
        riskScore += 20;
    }


    // Determine risk level

    let riskLevel;

    if (riskScore >= 70) {

        riskLevel = "HIGH";

    } else if (riskScore >= 40) {

        riskLevel = "MEDIUM";

    } else {

        riskLevel = "LOW";

    }


    document.getElementById("riskLevel").innerText =
        riskLevel;

    document.getElementById("simulationResult").innerText =
        "Simulation completed. Risk score: " + riskScore;

}
