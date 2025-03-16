document.addEventListener("DOMContentLoaded", function () {
    console.log("popup.js loaded!"); // Debugging
    let iframe = document.getElementById("iframe");

    if (iframe) {
        iframe.src = "http://127.0.0.1:5000/";  // Ensure this is correct
        console.log("Setting iframe source to Flask app: " + iframe.src);

        iframe.onload = function () {
            console.log("Flask loaded successfully inside iframe.");
        };

        iframe.onerror = function () {
            console.error("Failed to load Flask inside iframe.");
        };
    } else {
        console.error("iframe not found!");
    }
});