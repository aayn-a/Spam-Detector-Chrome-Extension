document.getElementById("detectButton").addEventListener("click", function() {
    const inputText = document.getElementById("inputText").value;
    fetch('/detectSpam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: inputText}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputText").innerText = data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    })});