// Gráfico de Carga de la Red
const ctxCarga = document.getElementById('graficoCarga').getContext('2d');
new Chart(ctxCarga, {
    type: 'line',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Carga de la Red',
            data: [12, 19, 3, 5, 2],
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// Gráfico de Latencia
const ctxLatencia = document.getElementById('graficoLatencia').getContext('2d');
new Chart(ctxLatencia, {
    type: 'bar',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Latencia (ms)',
            data: [20, 30, 15, 25, 18],
            backgroundColor: 'rgba(255, 159, 64, 0.5)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// Gráfico de Alertas Críticas
const ctxAlertas = document.getElementById('graficoAlertas').getContext('2d');
new Chart(ctxAlertas, {
    type: 'pie',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Alertas Críticas',
            data: [5, 10, 3, 8, 4],
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)',
                'rgba(153, 102, 255, 0.7)'
            ],
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
            }
        }
    }
});





