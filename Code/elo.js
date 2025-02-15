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

function update_elo(result) {
  elo = elo;
  games += 1;
  switch (result) {
    case 1:
      wins += 1;
      break;
    case 0:
      lose += 1;
      break;
    case 0.5:
      draw += 1;
      break;
  }
}
