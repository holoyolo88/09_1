$(".btn,#btn-close-dialog").click(
  function () {
    $("#my-dialog,#dialog-background").toggle();
  }
);

$('.apply').click(
  function() { 
    location.replace('apply');
  }
);

$('.cancel').click(
  function() { 
    location.replace('cancel');
  }
);