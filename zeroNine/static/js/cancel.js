$('.submit').click(function() { 
    var txt;
    var result = confirm('정말 취소하시겠습니까?'); 

    if(result) {  
        alert("감사합니다");
    }

    location.replace('main');
}); 