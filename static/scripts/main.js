navClick = document.getElementById("nav-icon-holder");
aside = document.getElementById("aside");

camera=document.getElementById("uploadFileOpen"); //icon
upload=document.getElementById("id_post_image"); //input

toast=document.getElementById("toastContainer");

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
