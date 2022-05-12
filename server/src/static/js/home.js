$(document).ready(function(){
    theme.appendChild(main_content);
    
    //Trigger Conta
    $("#btn_conta").click(function () {
        $("#conta_lista").fadeToggle();
    });

    //Trigger profile feed
    $("#btn_profile, #btn_home").click(function () {
        //field
        $("#container_feed").fadeToggle();
        $("#container_profile").fadeToggle();
        //btns
        $("#profile_btn").toggle();
        $("#home_btn").toggle();
        //Forms Search
        $('#search_home').toggle();
    });

    //Trigger Criar Post
    $("#btn_criar").click(function () {
        $("#modal_post").fadeToggle();
    });

    $("#btn_return_modal").click(function () {
        $("#modal_post").fadeToggle();
    });

    //Trigger Modal Forms
    $("#card_consultoria").click(function () {
        $("#modal_post").fadeToggle();
        $("#modal_consultoria").fadeToggle();
    });
    $("#card_servicos").click(function () {
        $("#modal_post").fadeToggle();
        $("#modal_servicos").fadeToggle();
    });
    $("#card_emprego").click(function () {
        $("#modal_post").fadeToggle();
        $("#modal_emprego").fadeToggle();
    });

    //Trigger exit Modal Forms
    $("#btn_return_modal_consultoria").click(function () {
        $('#form_Consultoria').each (function(){
            this.reset();
        });
        $("#modal_consultoria").fadeToggle();
    });

    //Plus and Min Forms
    $("#number_plus").click(function () {
        var value = parseInt(document.getElementById('ftempo').value);
        value = isNaN(value) ? 0 : value;
        value++;
        document.getElementById('ftempo').value = value;
    });
    $("#number_min").click(function () {
        var value = parseInt(document.getElementById('ftempo').value);
        value = isNaN(value) ? 0 : value;
        value < 1 ? value = 1 : '';
        value--;
        document.getElementById('ftempo').value = value;
    });

    //Steps
    $(".next").click(function () {
        $(this).parent(".stage-button").parent(".active_step").removeClass("active_step");
        $(this).parent(".stage-button").parent().next().addClass("active_step");
        var step = $("#steps").children(".tpc");
        step.next().addClass("tpc")
        step.removeClass("tpc")
    });
    $(".prev").click(function () {
        $(this).parent(".stage-button").parent(".active_step").removeClass("active_step");
        $(this).parent(".stage-button").parent().prev().addClass("active_step");
        var step = $("#steps").children(".tpc");
        step.prev().addClass("tpc")
        step.removeClass("tpc")
    });

    //Key cart Consultoria Trigger
    $(".key-card").click(function () {
        $(this).next().fadeToggle();
    });

    $('input').on('input', function() {
        tcons = $('#fconsultoria').val();
        testa = $('#festado').val();
        tcida = $('#fcidade').val();
        tnome = $('#fnome').val();
        texpe = $("input[name='fexperiencia']:checked").val();
        tprec = $("#fpreco").val();
        ttemp = $("#ftempo").val();

        var tsema = new Array();
        $("input[name='fsemana']:checked").each(function() {
            tsema.push(this.value);
        });
        thini = $("#fhinicial").val();
        thfin = $("#fhfinal").val();
        tphon = $("#fphone").val();
        temai = $("#femail").val();

        $('#ccons').html(tcons);
        $('#testa').html(testa);
        $('#ccity').html(tcida);
        $('#cnaex').html(tnome+" | Nivel: "+texpe);
        $('#cmone').html("R$ "+tprec);
        $('#ctime').html(ttemp +"h");
        $('#cwick').html(tsema);
        $('#ctinf').html(thini+" ás "+thfin);
        $('#ccont').html(tphon+" | "+temai);
      });
      
});