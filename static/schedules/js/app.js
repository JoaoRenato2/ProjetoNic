const sing_in_btn = document.querySelector("#sign-in-btn");
const sing_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sing_up_btn.addEventListener('click', () => {
    container.classList.add("sign-up-mode");
});

sing_in_btn.addEventListener('click', () => {
    container.classList.remove("sign-up-mode");
});

