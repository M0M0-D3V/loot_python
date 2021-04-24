$(document).ready(function () {
  console.log("ready!");
  // alert("Play a card or Draw Card to skip turn");

  $(".hand").click(function () {
    // $(this).hide();
    $(this).trigger().submit();
  });

  // every jquery above this line
});
