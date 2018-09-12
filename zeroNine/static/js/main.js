$(".img").hover(
  function () {
    $(this).addClass("darkness");
  }
);

$(".img").mouseleave(
  function () {
    $(this).removeClass("darkness");
  }
);
