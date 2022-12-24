function SetVisibleMenu(visible) 
{
 if (visible) 
 {
    $("#bodycontainer").css("display", "none");
 }
 else 
 {
    $("#bodycontainer").removeAttr("style");
 }
}