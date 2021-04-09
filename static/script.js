$(document).ready(function () {
  console.log("ready!");

  $("#title").click(function () {
    $(this).hide();
    $("#player-input").show();
    console.log("trying to hide title and show the player Input");
  });
  $("#num-players").submit(function (event) {
    event.preventDefault();
    console.log("preventing default reload");
    $("#num-players").hide();
    console.log("player # input hidden");
    // new form
    console.log("creating new form...");
    var $numPlayers = $("#input-num").val();
    console.log(`numPlayers is: ${$numPlayers}`);
    var newForm = `<form id="player-names" action="/player_names" method="POST">`;
    for (var i = 0; i < $numPlayers; i++) {
      newForm += `<label for="player-${i + 1}">Player ${i + 1} name </label>`;
      newForm += `<input id="name-${
        i + 1
      }" type="text" name="player_name_${i}" placeholder="momo" /><br>`;
    }
    newForm += `<input type="hidden" name="num_players" value="${$numPlayers}" />`;
    newForm += `<button type="submit">Start Game</button>`;
    $("#player-input").append(newForm);
    console.log("new form created");
  });
});
