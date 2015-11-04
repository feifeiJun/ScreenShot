/**
 * Created by Fei on 15/9/16.
 */
var Submit=document.getElementById("Submit");
Submit.onclick=function() {
    var Search = document.getElementById("Search");
    var Logo = document.getElementById("Dlogo");
    var WebSite = document.getElementById("WebSite");
    var Capture = document.getElementById("ScreenShot");

    Logo.style.float = "left";
    //Logo.style.margin = "0% 7% 0 19% ";
    Logo.style.top = "5%";
    Logo.style.left = "22%";



    Search.style.float = "left";
    Search.style.top = "6%";
    Search.style.left= "25%";
  

    //Search.style.margin = "1.5% auto";
}

    Capture.style.display="block";




//    $.ajax({
//            type: "POST",
//            url: "/shoot/",
//            data: {url: WebSite.value},
//            success:function(data,staus){
//                url = data.url;
//                $("#ScreenShot").css({"display":"block","background-image": "url('" + url + "')"});
//
//            }
//        }
//    )
//}
