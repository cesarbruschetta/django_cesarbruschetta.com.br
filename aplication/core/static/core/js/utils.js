


function equalizer(obj){
    var maxHeight = 0

    $(obj).each(function(){
        if ($(this).height() > maxHeight) {
            maxHeight = $(this).height()
        }
    })

    $(obj).height(maxHeight);
}
