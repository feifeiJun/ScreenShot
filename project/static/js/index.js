/**
 * Created by Fei on 15/9/16.
 */
var Submit=document.getElementById("Submit");
Submit.onclick=function(){
    var Search=document.getElementById("Search");
    var Logo=document.getElementById("Dlogo");
    var WebSite=document.getElementById("WebSite");
    var Capture=document.getElementById("ScreenShot");

    Logo.style.float= "left";
    Logo.style.margin= "0% 15%";
    Logo.style.margin.right="5%";

    Search.style.float= "left";
    Search.style.margin="1.5% auto";

    Capture.style.visible="visible";
    //Capture.style.border="darkkhaki dashed";
    //Capture.style.border.radius="5px";



    $.ajax({
            type: "get",
            url: "",
            data: WebSite.value,
            success:function(data,staus){
                $("#ScreenShot").css({"display":"block","backgroundImage":""});

            }
        }
    )
}
