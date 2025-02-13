class Players {
  constructor({ name, grade }) {
    this.name = name;
    this.grade = grade;
    this.elo = 600;
    this.wins = 0;
    this.lose = 0;
    this.draw = 0;
    this.games = 0;
    this.opponents = []
  }

  update(elo, result) {
    this.elo = elo;
    this.games += 1;
    switch (result) {
      case 1:
        this.wins += 1;
        break;
      case 0:
        this.lose += 1;
        break;
      case 0.5:
        this.draw += 1;
        break;
    }
  }
}

// Elo Calculation
function new_elo(result, playerA, playerB) {
  // Getting experience
  const K = Experience(playerA);

  // Getting expected result
  const E = ExpectedResult(playerA, playerB);

  // New Elo cal
  const New_Elo = playerA.elo + K * (result - E);
  return New_Elo;
}

function ExpectedResult(playerA, playerB) {
  const Q_A = 10 ** (playerA.elo / 400);
  const Q_B = 10 ** (playerB.elo / 400);
  return Q_A / (Q_A + Q_B);
}

function Experience(player) {
  if (player.games <= MIN_GAMES) {
    return K1;
  } else if (player.elo >= K2_ELO && player.elo <= K3_ELO) {
    return K2;
  } else if (player.elo <= K3_ELO) {
    return K3;
  }
}
