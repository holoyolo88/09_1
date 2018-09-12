$(".btn,#btn-close-dialog").click(
  function () {
    $("#my-dialog,#dialog-background").toggle();
  }
);

$('.apply').click(
  function() { 
    location.replace('apply.html');
  }
);

$('.cancel').click(
  function() { 
    location.replace('cancel.html');
  }
);