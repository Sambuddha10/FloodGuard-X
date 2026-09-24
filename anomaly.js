function detectAnomaly(rainfall, waterLevel, soilMoisture) {

    let anomalyScore = 0;
    let messages = [];

    if (rainfall >= 120) {
        anomalyScore += 40;
        messages.push("Extremely high rainfall detected.");
    }

    if (waterLevel >= 4) {
        anomalyScore += 40;
        messages.push("Critical water level detected.");
    }

    if (soilMoisture >= 90) {
        anomalyScore += 20;
        messages.push("Extremely high soil moisture detected.");
    }

    return {
        isAnomaly: anomalyScore >= 40,
        score: anomalyScore,
        messages: messages
    };
}
