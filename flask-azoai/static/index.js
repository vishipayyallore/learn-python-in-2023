function generateResponse() {
    const userInput = document.getElementById("userInput").value;
    const responseContainer = document.getElementById("response");

    // Make an API request to your Flask API
    fetch("/api/get?msg=" + userInput)
        .then(response => response.text())
        .then(data => {
            responseContainer.innerText = data;
        })
        .catch(error => {
            console.error("An error occurred:", error);
            responseContainer.innerText = "An error occurred while processing the request.";
        });
}
