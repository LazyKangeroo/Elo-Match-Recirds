// adding new player
// getting player values for elo change
// getting player values for sorting etc

async function getJson() {
    const response = await fetch("./db.json");
    const data = await response.json();
    console.log(data);
  }
getJson()