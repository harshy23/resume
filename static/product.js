const buttn = document.querySelector(".resume")

buttn.addEventListener('click',()=>{
    window.location.href = "/register";
    buttn.style.color = "white";
    buttn.style.backgroundColor = "yellowgreen";
    buttn.style.transform = 'scale(1)';
    setTimeout(() => {
      buttn.style.transform = 'scale(1.2)';
    });
});

