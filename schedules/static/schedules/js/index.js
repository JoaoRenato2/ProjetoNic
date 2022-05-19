let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");
let addnew = document.querySelector("#schedule");
let agend = document.querySelector(".panel-scheudle");
let close_form = document.querySelector("#close-form");

btn.onclick = function () {
    sidebar.classList.toggle("active");
}

searchBtn.onclick = function () {
    sidebar.classList.toggle("active");
}


addnew.onclick = function(){
    agend.classList.add("active");
}

close_form.onclick = function(){
    agend.classList.remove("active");
}