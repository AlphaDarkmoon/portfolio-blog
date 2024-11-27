document.addEventListener("DOMContentLoaded", function () {
    var splash = document.getElementById("splash");
    var content = document.getElementById("content");

    // Simulate loading time with setTimeout
    setTimeout(function () {
        // Fade out the splash screen
        splash.style.opacity = 0;

        // After the animation, hide the splash screen and show the content
        setTimeout(function () {
            splash.style.display = "none";
            content.style.display = "block";
        }, 1000); // Adjust the duration to match the CSS transition duration
    }, 3000); // Adjust the timeout to simulate loading time
});