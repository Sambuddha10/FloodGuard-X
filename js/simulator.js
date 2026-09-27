function generateScenario(type = "random") {

    // RANDOM CONDITIONS

    if (type === "random") {

        return {

            rainfall:
                Math.floor(Math.random() * 150),

            waterLevel:
                Number(
                    (Math.random() * 5).toFixed(2)
                ),

            soilMoisture:
                Math.floor(Math.random() * 100),

            temperature:
                Math.floor(
                    20 + Math.random() * 20
                )
        };
    }


    // NORMAL CONDITIONS

    if (type === "normal") {

        return {

            rainfall: 20,

            waterLevel: 1.2,

            soilMoisture: 40,

            temperature: 28
        };
    }


    // HEAVY RAINFALL

    if (type === "heavyRain") {

        return {

            rainfall: 110,

            waterLevel: 2.2,

            soilMoisture: 75,

            temperature: 25
        };
    }


    // RISING WATER

    if (type === "risingWater") {

        return {

            rainfall: 70,

            waterLevel: 3.5,

            soilMoisture: 85,

            temperature: 26
        };
    }


    // EXTREME FLOOD

    if (type === "extremeFlood") {

        return {

            rainfall: 140,

            waterLevel: 4.5,

            soilMoisture: 95,

            temperature: 24
        };
    }


    // DEFAULT

    return {

        rainfall: 20,

        waterLevel: 1.2,

        soilMoisture: 40,

        temperature: 28
    };
}
