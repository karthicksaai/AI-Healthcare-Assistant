function processData() {
    // Get user inputs
    const heartRate = document.getElementById('heartRate').value;
    const spo2 = document.getElementById('spo2').value;
    const bp = document.getElementById('bp').value;
    const caloriesBurnt = document.getElementById('caloriesBurnt').value;
    const hoursOfSleep = document.getElementById('hoursOfSleep').value;
    const weight = document.getElementById('weight').value;
    const totalSteps = document.getElementById('totalSteps').value;
    const totalDistance = document.getElementById('totalDistance').value;

    // Create a FormData object to send data to Python script
    const formData = new FormData();
    formData.append('heartRate', heartRate);
    formData.append('spo2', spo2);
    formData.append('bp', bp);
    formData.append('caloriesBurnt', caloriesBurnt);
    formData.append('hoursOfSleep', hoursOfSleep);
    formData.append('weight', weight);
    formData.append('totalSteps', totalSteps);
    formData.append('totalDistance', totalDistance);

    // Send data to Python script using Fetch API
    fetch('final.py', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        // Display the result on the webpage
        document.getElementById('mlResults').innerHTML = result;
    })
    .catch(error => console.error('Error:', error));
}
