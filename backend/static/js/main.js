// Función para generar datos de latencia aleatorios (simulación)
function generarDatosAleatorios(cantidad, max) {
    return Array.from({ length: cantidad }, () => Math.floor(Math.random() * max));
}

// Opciones comunes para ambos gráficos
const opcionesGrafico = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false
        }
    }
};

// Gráfico de Latencia en Tiempo Real
const ctxLatenciaTiempoReal = document.getElementById('graficaLatenciaTiempoReal').getContext('2d');
const graficoLatenciaTiempoReal = new Chart(ctxLatenciaTiempoReal, {
    type: 'line',
    data: {
        labels: Array.from({ length: 12 }, (_, i) => `${i * 5} s`), // Cada 5 segundos
        datasets: [{
            label: 'Latencia (ms)',
            data: generarDatosAleatorios(12, 300),
            borderColor: '#17a2b8',
            backgroundColor: 'rgba(23, 162, 184, 0.2)',
            tension: 0.4,
            fill: true
        }]
    },
    options: {
        ...opcionesGrafico,
        scales: {
            y: {
                suggestedMin: 0,
                suggestedMax: 300,
                title: {
                    display: true,
                    text: 'Milisegundos'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Tiempo'
                }
            }
        }
    }
});

// Gráfico de Latencia por Servidor
const ctxLatenciaPorServidor = document.getElementById('graficaLatenciaPorServidor').getContext('2d');
const graficoLatenciaPorServidor = new Chart(ctxLatenciaPorServidor, {
    type: 'bar',
    data: {
        labels: ['Servidor 1', 'Servidor 2', 'Servidor 3', 'Servidor 4'],
        datasets: [{
            label: 'Latencia (ms)',
            data: generarDatosAleatorios(4, 300),
            backgroundColor: ['#007bff', '#6610f2', '#6f42c1', '#e83e8c']
        }]
    },
    options: {
        ...opcionesGrafico,
        scales: {
            y: {
                suggestedMin: 0,
                suggestedMax: 300,
                title: {
                    display: true,
                    text: 'Milisegundos'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Servidores'
                }
            }
        }
    }
});

// Actualizar datos de latencia en tiempo real cada 5 segundos (simulación)
setInterval(() => {
    graficoLatenciaTiempoReal.data.datasets[0].data = generarDatosAleatorios(12, 300);
    graficoLatenciaTiempoReal.update();

    graficoLatenciaPorServidor.data.datasets[0].data = generarDatosAleatorios(4, 300);
    graficoLatenciaPorServidor.update();
}, 5000);


function exportarReporte(formato) {
    if (formato === 'pdf') {
        alert("Exportando reporte como PDF...");
        // Aquí podrías añadir la lógica para generar el PDF
    } else if (formato === 'csv') {
        alert("Exportando reporte como CSV...");
        // Aquí podrías añadir la lógica para generar el archivo CSV
    } else {
        alert("Formato de exportación no soportado.");
    }
}

