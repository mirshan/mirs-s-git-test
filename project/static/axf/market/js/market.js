$(document).ready(function () {

    var alltypebtn=document.getElementById('alltypebtn')
    var showsortbtn=document.getElementById('showsortbtn')


    var typediv=document.getElementById('typediv')
    var sortdiv=document.getElementById('sortdiv')
    // var yellowSlide=document.getElementsByClassName('yellowSlide') //点击显示左侧黄色小竖条
    // #默认两个标签的DIV不显示
    typediv.style.display='none'
    sortdiv.style.display='none'
    // yellowSlide.style.background='green'
    // yellowSlide.style.color='green'


    alltypebtn.addEventListener('click',function () {
        typediv.style.display='block'
        sortdiv.style.display='none'
    },false)
    showsortbtn.addEventListener('click',function () {
        typediv.style.display='none'
        sortdiv.style.display='block'
    },false)


    var subShoppings=document.getElementsByClassName('subShopping')
    var addShoppings=document.getElementsByClassName('addShopping')
    //addShopping
    for (var i=0;i<addShoppings.length;i++){
        addShopping=addShoppings[i]
        addShopping.addEventListener('click',function () {   //添加点击事件
            pid=this.getAttribute('ga')    //获取商品ID
            $.post('/changecart/0/',{'productid':pid},function (data) {   //AJAX请求，修改商品数量。定义0为添加
                if(data.status=='success'){
                    //添加成功，把中间的SPAN的innerHTML变成当前的数量

                }else{
                    if(data.data==-1){
                        window.location.href='/login/'
                    }
                }
                
            })

        },false)
    }
    //subShopping
    for (var i=0;i<subShoppings.length;i++){
        subShopping=subShoppings[i]
        subShopping.addEventListener('click',function () {   //添加点击事件
            console.log('$$$$$$$$$$$')
            pid=this.getAttribute('ga')    //获取商品ID
            $.post('/changecart/1/',{'productid':pid},function (data) {   //AJAX请求，修改商品数量。定义0为添加
                if(data.status=='success'){
                    //添加成功，把中间的SPAN的innerHTML变成当前的数量
                }else{
                    if(data.data==-1){
                        window.location.href='/login/'
                    }
                }

            })

        },false)
    }



});
