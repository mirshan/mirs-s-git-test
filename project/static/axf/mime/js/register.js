$(document).ready(function () {
    var account=document.getElementById('account')
    var accounterr=document.getElementById('accounterr')      //error消息，准备聚集时消失
    var checkerr=document.getElementById('checkerr')      //同上
    var reg=document.getElementById('reg')

    var pass=document.getElementById('pass')
    var password=document.getElementById('password')
    var passerr=document.getElementById('passerr')

    //聚焦
    account.addEventListener('focus',function () {
        accounterr.style.display='none'
        checkerr.style.display='none'
    },false)
    //离焦
    account.addEventListener('blur',function () {
        instr=this.value    //获取内容判断长度是否符合限制
        if (instr.length <6 || instr.length >12){
            accounterr.style.display='block'
            return
        }

        //判断instr是否已经被注册，只能发送ajax请求了
        $.post('/checkuserid/',{'userid':instr},function (data) {  //请求checkuserid，传参数{'userid':instr}，接收函数function,去views.py中处理数据
            if (data.status=='error'){
               checkerr.style.display='block'   //如果status值为error表示已被注册，显示error信息checkerr
               //  checkerr.setAttribute('style','display:block')    //与上面同样的效果，但不常用
                reg.setAttribute("disabled", true)    //设置提交按钮不可用
                // 这里注意：setAttribute是元素的属性，而style.display指的是css样式，不同，所以把error信息改成setAttribute是不可用的
            }
        })


    },false)



            //******************处理密码***********************
        //聚焦
    pass.addEventListener('focus',function () {
        passerr.style.display='none'
    },false)
    //离焦
    pass.addEventListener('blur',function () {
        instr = this.value    //获取内容判断长度是否符合限制
        if (instr.length < 6 || instr.length > 16) {
            passerr.style.display = 'block'
            return
        }
    },false)

    //密码验证
       password.addEventListener('focus',function () {
        passwderr.style.display='none'
    },false)
    //离焦
    password.addEventListener('blur',function () {
        instr = this.value    //获取内容判断长度是否符合限制
        instr1=pass.value
        if (instr!=instr1) {
            passwderr.style.display = 'block'
            return
        }
    },false)









})