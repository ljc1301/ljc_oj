function getCookie(name){
    var x=document.cookie.match("\\b"+name+"=([^;]*)\\b");
    return x?x[1]:undefined;
}

$(document).ready(function(){
    $("#submit").click(function(){
        var user=$("#username").val();
        var pid=$("#pid").val();
        var lang=$("#language").val();
        var code=$("#code").val();
        var page=$("#page").val();
        var pd={"username":user,"pid":pid,"language":lang,"code":code,"page":page,"_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/submit",
            data:pd,
            cache:false,
            success:function(data){
                if(data=="-1")
                    alert("输入的题目编号不合法！");
                else
                    window.location="/submissions/"+data;
            },
            error:function(){
                alert("error!");
            }
        });
    });
});