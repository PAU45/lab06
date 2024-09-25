document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".form");
    const errorDiv = document.querySelector(".error");

    form.addEventListener("submit", (event) => {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Verificar 
        if (username === "a" && password === "a") {
            // Redirigir a la página principal
            window.location.href = "/admin"; // Asegúrate de que esta URL sea correcta
        } else {
            // Mostrar mensaje de error
            event.preventDefault(); 
            errorDiv.textContent = "Nombre de usuario o contraseña incorrectos.";
            errorDiv.style.color = "red"; 
        }
    });
});