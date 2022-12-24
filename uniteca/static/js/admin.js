function SetVisibleMenu(visible) 
{
 if (visible) 
 {
    $("#div1").css("display", "none");
	$("#div2").css("display", "none");
 }
 else 
 {
    $("#div1").removeAttr("style");
 }
}
/*
$(function()
  {
    $("#div2").hide(); 
    $(".menu").on("click", function()
    {
        $("#div2").toggle(); 
    });
});*/
/*
document.querySelectorAll('.navbar .nav-container a ')
  .forEach(e => e.addEventListener('click', _ => change(e.dataset.id)))


function change(n) 
{
  let panels = document.querySelectorAll('main div')
  panels.forEach(p => p.classList.remove('active'))
  panels[n - 1].classList.add('active')
}*/

/*$(document).on('click', '.menu', function() {
  var show = $(this).data('show');
  $(show).removeClass("div2").siblings().addClass("div2");
});*/