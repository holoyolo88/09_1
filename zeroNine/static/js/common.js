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
  
$("#logo_img").click(
    function () {
      location.replace('main');
    }
);

$("#loginbtn").click(
    function(){
      location.replace('login');
    }
)