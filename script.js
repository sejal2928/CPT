document.getElementById('patientForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var patient_id = document.getElementById('patient_id').value;
    // Get other input fields and their values

    // Send data to backend
    fetch('backend_endpoint_url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            patient_id: patient_id,
            // Add other data fields here
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Data saved successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
