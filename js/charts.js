let riskHistory = [];

function addRiskHistory(score, level) {

    riskHistory.push({
        score: score,
        level: level
    });

    // Keep only the latest 10 simulations
    if (riskHistory.length > 10) {
        riskHistory.shift();
    }

    updateRiskHistory();
}


function updateRiskHistory() {

    const historyElement =
        document.getElementById("riskHistory");

    if (!historyElement) {
        return;
    }

    historyElement.innerHTML = "";

    riskHistory.forEach((item, index) => {

        const row = document.createElement("div");

        row.innerText =
            "Simulation " +
            (index + 1) +
            " → " +
            item.level +
            " (Score: " +
            item.score +
            ")";

        historyElement.appendChild(row);
    });
}
