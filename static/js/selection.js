document.addEventListener("DOMContentLoaded", function () {
    const botonSeleccion = document.getElementById("select");
    const contadorSpan = document.getElementById("contador");

    function actualizarContador() {
        const seleccionadas = document.querySelectorAll(".form-check-input:checked").length;
        contadorSpan.textContent = seleccionadas; // Actualiza el número en la interfaz
    }

    // Evento para actualizar el contador cada vez que se cambia una checkbox
    document.querySelectorAll(".form-check-input").forEach((checkbox) => {
        checkbox.addEventListener("change", actualizarContador);
    });

    botonSeleccion.addEventListener("click", function () {
        let seleccionadas = [];

        // Buscar todas las checkboxes marcadas
        document.querySelectorAll(".form-check-input:checked").forEach((checkbox) => {
            let nombreImagen = checkbox.id.replace("select_", "");
            seleccionadas.push(nombreImagen);
        });

        console.log("Imágenes seleccionadas:", seleccionadas);

        if (seleccionadas.length === 0) {
            alert("No has seleccionado ninguna imagen.");
            return;
        }

        fetch("/user/guardar_seleccion", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ imagenes: seleccionadas })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Respuesta del servidor:", data);
            alert(data.mensaje); 
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Hubo un error al enviar la selección.");
        });
    });
});
