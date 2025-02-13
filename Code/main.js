// Select all radio buttons
const radios = document.querySelectorAll('input[type="radio"]');

// Add event listener for change event on each radio button
radios.forEach(radio => {
  radio.addEventListener('change', () => {
    const selectedRadio = document.querySelector('input[name="sorting"]:checked');
    if (selectedRadio) {
      console.log(`Selected option: ${selectedRadio.id}`);
    }
  });
});