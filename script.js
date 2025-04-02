function convertTime() {
    const conversion = document.getElementById("conversion").value;
    const value = parseFloat(document.getElementById("value").value);
    const resultElement = document.getElementById("result");

    if (isNaN(value) || value < 0) {
        resultElement.textContent = "Please enter a valid number.";
        return;
    }

    let result;

    if (conversion === "seconds-to-minutes") {
        result = value / 60;
        resultElement.textContent = `${value} seconds is about ${result.toFixed(2)} minutes.`;
    } else if (conversion === "seconds-to-hours") {
        result = value / 3600;
        resultElement.textContent = `${value} seconds is about ${result.toFixed(2)} hours.`;
    } else if (conversion === "minutes-to-hours") {
        result = value / 60;
        resultElement.textContent = `${value} minutes is about ${result.toFixed(2)} hours.`;
    } else if (conversion === "hours-to-minutes") {
        result = value * 60;
        resultElement.textContent = `${value} hours is about ${result.toFixed(2)} minutes.`;
    } else if (conversion === "hours-to-seconds") {
        result = value * 3600;
        resultElement.textContent = `${value} hours is about ${result.toFixed(2)} seconds.`;
    } else {
        resultElement.textContent = "Unknown transform option.";
    }
}