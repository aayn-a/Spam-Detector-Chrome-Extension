document.getElementById("detectButton").addEventListener("click", async function() {
    const inputText = document.getElementById("inputText").value;
    console.log(`Sending input: ${inputText}`);  // Log the input being sent
    const backendURL = window.location.hostname.includes("railway.app") 
        ? "https://spam-detector-chrome-extension-production.up.railway.app/detectSpam"
        : "http://127.0.0.1:5000/detectSpam";  // Ensure the local URL is correct
    console.log(`Backend URL: ${backendURL}`);  // Log the backend URL
    try {
        let response = await fetch(backendURL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: inputText }),
        });

        if (!response.ok) {
            throw new Error("Server error, try again later.");
        }

        let data = await response.json();
        console.log(`Received response: ${JSON.stringify(data)}`);  // Log the response
        document.getElementById("outputText").innerText = 'Prediction: ' + data.prediction;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("outputText").innerText = "Server is down. Try again later.";
    }
});