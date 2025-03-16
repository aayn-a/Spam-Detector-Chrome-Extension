document.getElementById("detectButton").addEventListener("click", async function() {
    const inputText = document.getElementById("inputText").value;
    try {
        let response = await fetch("http://127.0.0.1:8080/detectSpam", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: inputText }),
        });

        if (!response.ok) {
            throw new Error("Server error, try again later.");
        }

        let data = await response.json();
        document.getElementById("outputText").innerText = 'Prediction: ' + data.prediction;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("outputText").innerText = "Server is down. Try again later.";
    }
});