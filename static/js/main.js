document.addEventListener('DOMContentLoaded', function() {
    const predictForm = document.getElementById('predict-form');
    const predictionResult = document.getElementById('prediction-result');

    predictForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(predictForm);
        fetch('/predict_expense', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            predictionResult.textContent = `Predicted expense: $${data.predicted_amount}`;
        });
    });

    // Fetch and render category chart
    fetch('/expenses_by_category')
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('categoryChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: Object.keys(data),
                datasets: [{
                    data: Object.values(data),
                    backgroundColor: [
                        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
                    ]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        left: 10,
                        right: 10,
                        top: 10,
                        bottom: 10
                    }
                },
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            boxWidth: 12,
                            font: {
                                size: 10
                            }
                        }
                    },

                }
            }
        });
    });

    // Fetch and render time chart
    fetch('/expenses_over_time')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('timeChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.map(item => item.date),
                    datasets: [{
                        label: 'Expenses Over Time',
                        data: data.map(item => item.amount),
                        borderColor: '#36A2EB',
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Expenses Over Time'
                    },
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day'
                            }
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});