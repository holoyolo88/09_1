$(function(){
    $(".submit,#btn-close-dialog").click(
        function () {
		    $("#apply-modal,#dialog-background").toggle();
    });
});

$('#input-btn').click(function() { 
    var txt;
    var result = confirm('정말로 신청하시겠습니까?\n이후 취소를 삼가해주세요'); 

    if(result) {  
        alert("감사합니다!");
    }

    location.replace('main.html');
}); 