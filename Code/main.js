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
// btns
const add_player = document.querySelector('input[type="button"]#add-player');
const add_game = document.querySelector('input[type="button"]#add-game');
const home = document.querySelector('input[type="button"]#home');
// containers
const player_profile = document.querySelector('section#profile-container');
const home_display = document.querySelector('section#home-container');
const new_player = document.querySelector('section#new-player-container');
const new_game_input = document.querySelector('section#game-input-container');

add_game.addEventListener('click', () => {
  console.log(`Add Game`);
  hide_show(new_game_input,player_profile,home_display,new_player);
});
add_player.addEventListener('click', () => {
  console.log(`Add Player`);
  hide_show(new_player,new_game_input,player_profile,home_display);
});
home.addEventListener('click', () => {
  console.log(`Home`);
  hide_show(home_display,new_player,new_game_input,player_profile);
});

function hide_show(toShow, toHide1,toHide2,toHide3) {
    toShow.style.display = "block";
    toHide1.style.display = "none";
    toHide2.style.display = "none";
    toHide3.style.display = "none";
}