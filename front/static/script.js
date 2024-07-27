// script.js
const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form submission

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Basic input validation
  if (username === '') {
    alert('Please enter a username');
    return;
  }

  if (password === '') {
    alert('Please enter a password');
    return;
  }

  // Submit the form or perform other actions
  form.submit();
});