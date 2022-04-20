navClick = document.getElementById("nav-icon-holder");
aside = document.getElementById("aside");

camera=document.getElementById("uploadFileOpen"); //icon
upload=document.getElementById("id_post_image"); //input


postImageHolderTemp = document.getElementById('display_image')

toast=document.getElementById("toastContainer");

var image_holder =''

var loadFile = function(event) {
    const [file] = upload.files
    postImageHolderTemp.style.display="flex";
    if (file) {
        postImageHolderTemp.src = URL.createObjectURL(file)
    }
};


if (navClick && aside){
    navClick.addEventListener("click",()=>{
        aside.classList.toggle("trigger")
    })
}


if(camera && upload){
    camera.addEventListener("click",()=>{
        upload.click()
    })
}


if(toast){
    setTimeout(()=>{
        toast.style.display = 'none';
    },3000)
}
