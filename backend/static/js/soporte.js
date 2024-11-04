document.getElementById('supportForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Simulación de envío de formulario
    setTimeout(() => {
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('supportForm').reset();
        
        // Ocultar mensaje después de 5 segundos
        setTimeout(() => {
            document.getElementById('successMessage').style.display = 'none';
        }, 5000);
    }, 1000);
});
