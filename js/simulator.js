function generateScenario() {

    const rainfall = Math.floor(Math.random() * 150);

    const waterLevel = Number(
        (Math.random() * 5).toFixed(2)
    );

    const soilMoisture = Math.floor(
        Math.random() * 100
    );

    const temperature = Math.floor(
        20 + Math.random() * 20
    );

    return {
        rainfall: rainfall,
        waterLevel: waterLevel,
        soilMoisture: soilMoisture,
        temperature: temperature
    };
}
