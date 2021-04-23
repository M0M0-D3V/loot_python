$(document).ready(function () {
  console.log("ready!");
  alert("Play a card or Draw Card to skip turn");

  $(".hand").click(function () {
    $(this).hide();
    // var thisCard = $(this);
    // console.log(`thisCard is: ${thisCard.style.backgroundColor}`);
  });
  // every jquery above this line
});
