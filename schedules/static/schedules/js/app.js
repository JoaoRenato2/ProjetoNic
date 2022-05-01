const sing_in_btn = document.querySelector("#sign-in-btn");
const sing_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sing_up_btn.addEventListener('click', () => {
    container.classList.add("sign-up-mode");
    /* window.history.pushState("Mudando","Cadastro","http://127.0.0.1:8000/auth/Register.html/") */
});

sing_in_btn.addEventListener('click', () => {
    container.classList.remove("sign-up-mode");
    /* window.history.pushState("Mudando","Login","http://127.0.0.1:8000/auth/Login.html/") */
});

