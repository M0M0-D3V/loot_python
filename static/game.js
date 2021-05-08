$(document).ready(function () {
  console.log("ready!");
  $(".number").hide();

  // if no merchant ships in play, then all pirate cards in hand are inactive to click

  $(".hand").click(function () {
    var message = "";
    if (confirm("Play this card?")) {
      message = `you are playing ${this}`;
      $(this).css("backgroundColor", "black");
      var this_card = $(".number", this).text();
      console.log(`this card is: ${this_card}`);
      console.log(`trying to replace the hidden input`);
      $(".player-action input").val(this_card);
      $(".player-action")
        .append(`<button type="submit"></button>`)
        .trigger("submit", function (event) {
          event.preventDefault();
          console.log("preventing default reload");
        });
    } else {
      message = "you choose not to play";
    }
    console.log(message);
  });

  $(".cards").click(function () {
    if (confirm("Draw a card?")) {
      $(".draw-card")
        .append(`<button type="submit"></button>`)
        .trigger("submit", function (event) {
          event.preventDefault();
          console.log("preventing default reload");
        });
    }
  });

  // if card clicked is a pirate
  // check if div class field merchant contains a merchant card first
  // if no merchant card, alert or validate to player different card

  // every jquery above this line
});
