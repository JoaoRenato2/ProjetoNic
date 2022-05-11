const sing_in_btn = document.querySelector("#sign-in-btn");
const sing_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const cadastro_btn = document.querySelector("#btn_cadastro");
const name_cadastro = document.querySelector(".Matricula_Cadastro");
const email_cadastro = document.querySelector(".Email_Cadastro");
const senha_cadastro = document.querySelector(".Senha_Cadastro");
const h2_name = document.querySelector(".erro-name");


sing_up_btn.addEventListener('click', () => {
    container.classList.add("sign-up-mode");
    /* window.history.pushState("Mudando","Cadastro","http://127.0.0.1:8000/auth/Register.html/") */
});

sing_in_btn.addEventListener('click', () => {
    container.classList.remove("sign-up-mode");
    /* window.history.pushState("Mudando","Login","http://127.0.0.1:8000/auth/Login.html/") */
});

/* cadastro_btn.addEventListener('click', (e) => {
    
    if(name_cadastro.value == ""){
        e.preventDefault();
        window.history.pushState("Mudando","Cadastro","http://127.0.0.1:8000/auth/cadastro/?status=1")
        console.log("Ih")
        h2_name.classList.toggle("active");
    }
    if(email_cadastro.value ==""){
        e.preventDefault();
        window.history.pushState("Mudando","Cadastro","http://127.0.0.1:8000/auth/cadastro/?status=1")
        console.log("Ih")
        h2_name.classList.toggle("active");

        
    }    
});  */


 
 