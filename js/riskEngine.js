function calculateRisk(rainfall, waterLevel, soilMoisture) {

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


    // Risk classification
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
