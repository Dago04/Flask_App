


document.addEventListener('DOMContentLoaded', function () {

    const myModal = new bootstrap.Modal(document.getElementById('confirmacion'))

    function mostrarConfirmacion() {

        myModal.show();
    }

    // Obtén el botón "Eliminar" por su id
    const btnEliminar = document.getElementById('btnEliminar');

    btnEliminar.addEventListener('click', function (event) {
        // Previene el comportamiento predeterminado del enlace (navegación)
        event.preventDefault();

        // Llama a la función para mostrar el modal
        mostrarConfirmacion();
    });
    // Tu código aquí
});

