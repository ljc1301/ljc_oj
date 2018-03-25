function getCookie(name){
    var x=document.cookie.match("\\b"+name+"=([^;]*)\\b");
    return x?x[1]:undefined;
}

$(document).ready(function(){
    $("#login").click(function(){
        var user=$("#username").val();
        var pwd=$("#password").val();
        var rem=$("#remember").val();
        var pd={"username":user,"password":pwd,"remember":rem,"_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/login",
            data:pd,
            cache:false,
            success:function(data){
                if(data=="-1")
                    alert("输入的用户名或密码错误！");
                else
                    window.location=document.referrer;
            },
            error:function(){
                alert("error!");
            }
        });
    });
});