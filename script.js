function convertTime() {
    const conversion = document.getElementById("conversion").value;
    const value = parseFloat(document.getElementById("value").value);
    const resultElement = document.getElementById("result");

    if (isNaN(value) || value <= 0) {
        resultElement.textContent = "Lūdzu ievadi derīgu skaitli.";
        return;
    }

    let result;
    if (conversion === "seconds-to-minutes") {
        result = value / 60;
        resultElement.textContent = `${value} sekundes ir aptuveni ${result.toFixed(2)} minūtes.`;
    } else if (conversion === "minutes-to-hours") {
        result = value / 60;
        resultElement.textContent = `${value} minūtes ir aptuveni ${result.toFixed(2)} stundas.`;
    } else {
        resultElement.textContent = "Nezināma pārveidošanas opcija.";
    }
}