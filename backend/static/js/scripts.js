// Función auxiliar para generar datos aleatorios
function generateRandomData(count, max) {
    return Array.from({ length: count }, () => Math.floor(Math.random() * max));
}

// Configuración común para las gráficas
const commonOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false
        }
    }
};

// Gráficas
new Chart(document.getElementById('serverLoads'), {
    type: 'line',
    data: {
        labels: ['1h', '2h', '3h', '4h', '5h', '6h'],
        datasets: [{
            data: generateRandomData(6, 100),
            borderColor: '#3498db',
            tension: 0.4,
            fill: true,
            backgroundColor: 'rgba(52, 152, 219, 0.1)'
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('networkLatency'), {
    type: 'bar',
    data: {
        labels: ['Server 1', 'Server 2', 'Server 3', 'Server 4'],
        datasets: [{
            data: generateRandomData(4, 50),
            backgroundColor: '#e74c3c'
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('congestionManagement'), {
    type: 'doughnut',
    data: {
        labels: ['Normal', 'Moderado', 'Alto'],
        datasets: [{
            data: [60, 30, 10],
            backgroundColor: ['#2ecc71', '#f1c40f', '#e74c3c']
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('predictiveAlerts'), {
    type: 'radar',
    data: {
        labels: ['CPU', 'Memoria', 'Disco', 'Red', 'Procesos'],
        datasets: [{
            data: generateRandomData(5, 100),
            borderColor: '#9b59b6',
            backgroundColor: 'rgba(155, 89, 182, 0.2)'
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('responseTimes'), {
    type: 'line',
    data: {
        labels: Array.from({ length: 12 }, (_, i) => `${i * 5}min`),
        datasets: [{
            data: generateRandomData(12, 200),
            borderColor: '#f1c40f',
            tension: 0.2
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('packetLoss'), {
    type: 'bar',
    data: {
        labels: ['Zona 1', 'Zona 2', 'Zona 3', 'Zona 4'],
        datasets: [{
            data: generateRandomData(4, 5),
            backgroundColor: '#e67e22'
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('serverAllocation'), {
    type: 'pie',
    data: {
        labels: ['Disponible', 'En uso', 'Mantenimiento'],
        datasets: [{
            data: [45, 45, 10],
            backgroundColor: ['#27ae60', '#2980b9', '#c0392b']
        }]
    },
    options: commonOptions
});

new Chart(document.getElementById('systemPerformance'), {
    type: 'line',
    data: {
        labels: Array.from({ length: 8 }, (_, i) => `${i + 1}h`),
        datasets: [{
            data: generateRandomData(8, 100),
            borderColor: '#16a085',
            tension: 0.4,
            fill: true,
            backgroundColor: 'rgba(22, 160, 133, 0.1)'
        }]
    },
    options: commonOptions
});
