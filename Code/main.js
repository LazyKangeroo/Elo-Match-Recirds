/*
  Sorting
*/
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

/*
  Actions
*/
const add_player = document.querySelector('input[type="button"]#add-player');
const add_game = document.querySelector('input[type="button"]#add-game');
const home = document.querySelector('input[type="button"]#home');

add_game.addEventListener('click', () => {
  console.log(`Add Game`);
});
add_player.addEventListener('click', () => {
  console.log(`Add Player`);
});
home.addEventListener('click', () => {
  console.log(`Home`);
});