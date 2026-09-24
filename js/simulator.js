function generateScenario(type = "random") {

    // Random scenario
    if (type === "random") {

        return {
            rainfall: Math.floor(Math.random() * 150),
            waterLevel: Number((Math.random() * 5).toFixed(2)),
            soilMoisture: Math.floor(Math.random() * 100),
            temperature: Math.floor(20 + Math.random() * 20)
        };
    }


    // Normal conditions
    if (type === "normal") {

        return {
            rainfall: 20,
            waterLevel: 1.2,
            soilMoisture: 40,
            temperature: 28
        };
    }


    // Heavy rainfall
    if (type === "heavyRain") {

        return {
            rainfall: 110,
            waterLevel: 2.2,
            soilMoisture: 75,
            temperature: 25
        };
    }


    // Rising water level
    if (type === "risingWater") {

        return {
            rainfall: 70,
            waterLevel: 3.5,
            soilMoisture: 85,
            temperature: 26
        };
    }


    // Extreme flood
    if (type === "extremeFlood") {

        return {
            rainfall: 140,
            waterLevel: 4.5,
            soilMoisture: 95,
            temperature: 24
        };
    }
}
