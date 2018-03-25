function getCookie(name){
    var x=document.cookie.match("\\b"+name+"=([^;]*)\\b");
    return x?x[1]:undefined;
}

function refresh(){
    var page=$("#page").val()
    var username=$("#username_").val()
    var pid=$("#pid_").val()
    var language=$("#language_").val()
    var result=$("#result_").val()
    pd={"page":page,"username":username,"pid":pid,"language":language,"result":result,"_xsrf":getCookie("_xsrf")};
    $.ajax({
        type:"post",
        url:"/submissions",
        data:pd,
        cache:false,
        success:function(data){
            res=JSON.parse(data);
            for(var i=0;i<res.length;i++){
                var d=document.getElementById("row"+res[i][0]);
                d.removeAttribute("hidden");
                d.setAttribute("data-href",'/submissions/'+res[i][1]);
                $("#id"+res[i][0]).html(res[i][1]);
                $("#user"+res[i][0]).html(res[i][2]);
                $("#pro"+res[i][0]).html(res[i][3]);
                $("#result"+res[i][0]).html(res[i][4]);
                $("#time"+res[i][0]).html(res[i][5]);
                $("#memory"+res[i][0]).html(res[i][6]);
                $("#lang"+res[i][0]).html(res[i][7]);
                $("#length"+res[i][0]).html(res[i][8]);
                $("#submittime"+res[i][0]).html(res[i][9]);
            }
            for(var i=res.length;i<20;i++){
                var d,attr;
                if(i>=10)
                    d=document.getElementById("row"+i);
                else
                    d=document.getElementById("row0"+i);
                attr=document.createAttribute('hidden');
                d.setAttributeNode(attr);
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
    $("#search").click(function(){
        var username=$("#username").val()
        var pid=$("#pid").val()
        var language=$("#language").val()
        var result=$("#result").val()
        window.location="/submissions?username="+username+"&pid="+pid+"&language="+language+"&result="+result;
    });
    $(".clickable-row").click(function(){
        window.document.location=$(this).data("href");
    });
});