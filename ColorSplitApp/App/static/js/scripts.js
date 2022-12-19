/*!
* Start Bootstrap - Scrolling Nav v5.0.5 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

document.getElementById("uploadButton").onchange = function() {
    var fileData = this.files[0];//获取到一个FileList对象中的第一个文件( File 对象),是我们上传的文件
    var pettern = /^image/;
    
    console.info(fileData.type)

    if (!pettern.test(fileData.type)) {
        alert("图片格式不正确");
        return;
    }
    var reader = new FileReader();
    reader.readAsDataURL(fileData);//异步读取文件内容，结果用data:url的字符串形式表示
    /*当读取操作成功完成时调用*/
    reader.onload = function(e) {
        console.log(e); //查看对象
        console.log(this.result);//要的数据 这里的this指向FileReader（）对象的实例reader
        document.getElementById("rawImagePreview").style.display="block";
        document.getElementById("rawImagePreview").style.backgroundImage="url("+this.result+")";
    }
};

//每点击一个推荐 就显示
var img = document.getElementsByClassName("imageSample");
//console.log("ok");
var i;
for (i=0; i<img.length; i++){
    img[i].onclick = function(){
        var fileData = this.style.backgroundImage;
        document.getElementById("rawImagePreview").style.display="block";
        document.getElementById("rawImagePreview").style.backgroundImage = fileData;
    }
}


//分色数量处理
var inputNum = document.getElementById("input-num");

//parseint用于将字符串转换为整数
document.getElementById("input-number__decrease").onclick = function(){
    inputNum.value = parseInt(inputNum.value) - 1;
    if (inputNum.value < 2){
        inputNum.value = 2;
    }
}

document.getElementById("input-number__increase").onclick = function(){
    inputNum.value = parseInt(inputNum.value) + 1;
    if (inputNum.value > 10){
        inputNum.value = 10;
    }
}

inputNum.onchange = function(){
    console.log("validating");
    if (inputNum.value > 10){
        inputNum.value = 10;
    }
    if (inputNum.value < 2){
        inputNum.value = 2;
    }
}

