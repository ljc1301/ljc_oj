function getCookie(name){
    var x=document.cookie.match("\\b"+name+"=([^;]*)\\b");
    return x?x[1]:undefined;
}

function refresh(){
    var rid=$("#rid").val();
    pd={"_xsrf":getCookie("_xsrf")};
    $.ajax({
        type:"post",
        url:"/submissions/"+rid,
        data:pd,
        cache:false,
        success:function(data){
            res=JSON.parse(data);
            $("#result").html(res[0]);
            $("#time").html(res[1]);
            $("#memory").html(res[2]);
            var div=document.getElementById("msg");
            if(res[3])
            {
                div.removeAttribute("hidden");
                $("#message").html(res[3]);
            }
            else
            {
                var attr=document.createAttribute('hidden');
                div.setAttributeNode(attr);
            }
        },
        error:function(){
            alert("error!");
        }
    });
}

$(document).ready(function($){
    refresh();
    setInterval("refresh()",2000);
});