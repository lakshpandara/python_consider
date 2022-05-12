// onload = function(){ theme.appendChild(main_content);}

$(document).ready(function(){
    theme.appendChild(main_index);
    /* Info Sobre Trigger */
    $("#banner_info").click(function () {
        $("#modal_sobre").css("display", "block");
    });
    $("#return_sobre_top").click(function () {
        $("#modal_sobre").css("display", "none");
    });
    $("#return_sobre_botton").click(function () {
        $("#modal_sobre").css("display", "none");
    });

    /* Info Termo Trigger */
    $("#banner_term").click(function () {
        $("#modal_termo").css("display", "block");
    });
    $("#return_termo_top").click(function () {
        $("#modal_termo").css("display", "none");
    });
    $("#return_termo_botton").click(function () {
        $("#modal_termo").css("display", "none");
    });
    
});