$(document).ready(function () {
		
    $.getJSON('/js/estados_cidades.json', function (data) {

        var items = [];
        var options = '<option selected disabled value="" class="font-medium bn-1 tn-4">Escolha um estado</option>';	

        $.each(data, function (key, val) {
            options += '<option value="' + val.nome + '" class="font-regular bn-1 tn-4">' + val.nome + '</option>';
        });					
        $("#fwestado").html(options);				
        
        $("#fwestado").change(function () {				
        
            var options_cidades = '';
            var str = "";					
            
            $("#fwestado option:selected").each(function () {
                str += $(this).text();
            });
            
            $.each(data, function (key, val) {
                if(val.nome == str) {							
                    $.each(val.cidades, function (key_city, val_city) {
                        options_cidades += '<option value="' + val_city + '" class="font-regular bn-1 tn-4">' + val_city + '</option>';
                    });							
                }
            });

            $("#fwcidade").html(options_cidades);
            
        }).change();		
    
    });

});