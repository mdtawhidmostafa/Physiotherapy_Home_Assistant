var passwordInput = document.getElementById("password");
var confirmInput = document.getElementById("confirm_password");

function validatePassword() {
    if (passwordInput.value != confirmInput.value) {
        confirmInput.setCustomValidity("Passwords do not match");
    } else {
        confirmInput.setCustomValidity("");
    }
}

passwordInput.addEventListener("input", validatePassword);
confirmInput.addEventListener("input", validatePassword);