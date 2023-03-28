const toggleSwitch = document.querySelector('.toggle-switch');
const body = document.querySelector('body');

toggleSwitch.addEventListener('click', () => {
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    toggleSwitch.innerText = 'Dark Mode';
  } else {
    body.classList.add('dark-mode');
    toggleSwitch.innerText = 'Light Mode';
  }
});
