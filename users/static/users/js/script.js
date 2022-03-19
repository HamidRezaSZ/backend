document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("sign").onclick = function () { // show signup form
        document.getElementById("sign-form").style.display = "block";
        document.getElementById("buttons-index").style.display = "none";
    };

    document.getElementById("log").onclick = function () { // show login form
        document.getElementById("log-form").style.display = "block";
        document.getElementById("buttons-index").style.display = "none";
    };

    document.getElementById("back-log").onclick = function () { // back login form
        document.getElementById("log-form").style.display = "none";
        document.getElementById("buttons-index").style.display = "block";
    };

    document.getElementById("back-sign").onclick = function () { // back signup form
        document.getElementById("sign-form").style.display = "none";
        document.getElementById("buttons-index").style.display = "block";

    };
});