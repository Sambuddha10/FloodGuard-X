function detectAnomaly(rainfall, waterLevel, soilMoisture) {

    let anomalyScore = 0;
    let messages = [];

    // Check rainfall
    if (rainfall >= 120) {
        anomalyScore += 40;
        messages.push("Extremely high rainfall detected.");
    } else if (rainfall >= 90) {
        anomalyScore += 20;
        messages.push("Unusually high rainfall detected.");
    }

    // Check water level
    if (waterLevel >= 4) {
        anomalyScore += 40;
        messages.push("Critical water level detected.");
    } else if (waterLevel >= 3) {
        anomalyScore += 20;
        messages.push("Unusually high water level detected.");
    }

    // Check soil moisture
    if (soilMoisture >= 90) {
        anomalyScore += 20;
        messages.push("Extremely high soil moisture detected.");
    } else if (soilMoisture >= 80) {
        anomalyScore += 10;
        messages.push("High soil moisture detected.");
    }

    // Determine anomaly status
    let isAnomaly = anomalyScore >= 40;

    return {
        isAnomaly: isAnomaly,
        score: anomalyScore,
        messages: messages
    };
}
