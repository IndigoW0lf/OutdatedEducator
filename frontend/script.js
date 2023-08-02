function getFacts() {
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
})
.catch(error => {
  console.error('Error:', error);
  document.getElementById('results').textContent = 'An error occurred. Please try again later.';
});

}
