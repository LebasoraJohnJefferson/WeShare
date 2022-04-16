navClick = document.getElementById("nav-icon-holder");
aside = document.getElementById("aside");
camera=document.getElementById("uploadFileOpen");
upload=document.getElementById("upload");
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
