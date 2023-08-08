function getFacts() {
  // Get the button element
  const button = document.getElementById("getFactsButton");
  
  // Change the button text to 'Please wait...'
  button.innerText = "Please wait...";
  button.disabled = true; // Optional: Disable the button to prevent multiple clicks.

  const year = document.getElementById("year").value;
  const country = document.getElementById("country").value;

  fetch('http://127.0.0.1:5000/getFacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ year: year, country: country }),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('results').textContent = 'Facts: ' + data.facts;
    
    // Once the process is complete, revert the button text and enable it
    button.innerText = "Get Facts";
    button.disabled = false;
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('results').textContent = 'An error occurred. Please try again later.';
    
    // In case of an error, also revert the button text and enable it
    button.innerText = "Get Facts";
    button.disabled = false;
  });
}
