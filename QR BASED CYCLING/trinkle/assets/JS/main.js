
$(function(){
    "use strict"
    $(window).on('scroll',function(event){
        var scroll = $(window).scrollTop();
        if(scroll < 20){
            $(".nav_area").removeClass("sticky");

        }
        else{
            $(".nav_area").addClass("sticky")
        }
    });

    $(document).ready(function(){
        $('.venobox').venobox();
    });

    //wow js
    new WOW().init();

    //tiny slider
    var slider = tns({
        container: '.team-active',
        items:1,
        slideBy:'page',
        autoplay: false,
        mouseDrag: true,
        nav: false,
        controlsText:['<i class="fa-solid fa-angles-left prev"></i>','<i class="fa-solid fa-angles-right next"></i>']
    });

    //scrollit js
    $.scrollIt();
});