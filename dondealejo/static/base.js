document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const botonHamburguesa = document.getElementById('alejo-boton-hamburguesa');
    const botonCerrar = document.getElementById('alejo-boton-cerrar');
    const barraNav = document.getElementById('alejo-barra-nav');
    const overlay = document.getElementById('alejo-overlay');
    
    // Función para abrir el menú
    function abrirMenu() {
        if (barraNav) barraNav.classList.add('activo');
        if (overlay) overlay.classList.add('activo');
        document.body.style.overflow = 'hidden'; // Prevenir scroll
    }
    
    // Función para cerrar el menú
    function cerrarMenu() {
        if (barraNav) barraNav.classList.remove('activo');
        if (overlay) overlay.classList.remove('activo');
        document.body.style.overflow = ''; // Restaurar scroll
    }
    
    // Event listeners
    if (botonHamburguesa) {
        botonHamburguesa.addEventListener('click', abrirMenu);
    }
    
    if (botonCerrar) {
        botonCerrar.addEventListener('click', cerrarMenu);
    }
    
    if (overlay) {
        overlay.addEventListener('click', cerrarMenu);
    }
    
    // Cerrar menú al hacer clic en enlaces
    const enlaces = document.querySelectorAll('.alejo-enlace, .alejo-item-menu');
    enlaces.forEach(enlace => {
        enlace.addEventListener('click', cerrarMenu);
    });
    
    // Cerrar menú en pantallas grandes
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            cerrarMenu();
        }
    });
});