console.log("hello world")

let modals = document.getElementsByClassName("modal-open");
let modals_text = document.getElementsByClassName("modals-text");
let modals_photo = document.getElementsByClassName("modal-photo");
let modal_main = document.getElementById("modal-main");
let modal_photo = document.getElementById("modal-photo");
let modal_text = document.getElementById("modal-text");


for(let i = 0; i < modals.length; i++) {
    modals[i].addEventListener("click", function (){
        console.log("hello world");
        modal_main.style.display = "flex";
        modal_photo.src = modals_photo[i].src
        modal_text.innerHTML = modals_text[i].innerHTML
    })
}
modal_main.addEventListener("click", function (){
    modal_main.style.display = "none"
})