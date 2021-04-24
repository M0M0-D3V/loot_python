$(document).ready(function () {
  console.log("ready!");
  $(".number").hide();
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
    // $(this).trigger().submit();
  });

  // every jquery above this line
});
