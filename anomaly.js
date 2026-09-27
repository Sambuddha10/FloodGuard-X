function detectAnomaly(
    rainfall,
    waterLevel,
    soilMoisture
) {

    let anomalyScore = 0;

    let messages = [];


    // EXTREME RAINFALL

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


    // WATER LEVEL

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


    // SOIL MOISTURE

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
