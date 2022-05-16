const sing_in_btn = document.querySelector("#sign-in-btn");
const sing_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const cadastro_btn = document.querySelector("#btn_cadastro");
const name_cadastro = document.querySelector(".Matricula_Cadastro");
const email_cadastro = document.querySelector(".Email_Cadastro");
const senha_cadastro = document.querySelector(".Senha_Cadastro");
const h2_name = document.querySelector("#success");
const feedbackArea = document.querySelector(".invalid_feedback");
const pswrdField = document.querySelector("#senha-login");
const usererro =  document.querySelector("#erro_matricula");
const pswrdFieldCadastro = document.querySelector("#senha");
toggleBtnLogin = document.querySelector("#eye-login");
toggleBtnCadastro = document.querySelector("#eye-cadastro");


sing_up_btn.addEventListener('click', () => {
    container.classList.add("sign-up-mode");
    /* window.history.pushState("Mudando","Cadastro","http://127.0.0.1:8000/auth/validar_cadastro/") */
});

sing_in_btn.addEventListener('click', () => {
    container.classList.remove("sign-up-mode");
    /* window.history.pushState("Mudando","Login","http://127.0.0.1:8000/auth/Login.html/") */
});


name_cadastro.addEventListener('keyup',(e)=>{
    const usernameValue = e.target.value;
    feedbackArea.style.display="none"
    name_cadastro.classList.remove("is-invalid")
    if(usernameValue.length>0){
        fetch("/auth/validate-username",{
            body:JSON.stringify({username: usernameValue}), 
            method:'POST',
        })
        .then((res) => res.json())
        .then((data)=>{
            console.log("data", data);
            if(data.username_erro){
                cadastro_btn.disabled = true;
                feedbackArea.style.display="block";
                name_cadastro.classList.add("is-invalid")
                feedbackArea.innerHTML=`<h2>${data.username_erro}</h2>`;
            }else{
                cadastro_btn.removeAttribute("disabled");
            }

        });
    }
});

email_cadastro.addEventListener('keyup',(e)=>{
    const emailValue = e.target.value;
    feedbackArea.style.display="none"
    if(emailValue.length>0){
        fetch("/auth/validate-email",{
            body:JSON.stringify({email: emailValue}), 
            method:'POST',
        })
        .then((res) => res.json())
        .then((data)=>{
            console.log("data", data);
            if(data.email_erro){
                cadastro_btn.disabled = true;
                feedbackArea.style.display="block";
                feedbackArea.innerHTML=`<h2>${data.email_erro}</h2>`;
            }else{
                cadastro_btn.removeAttribute("disabled");
            }

        });
    }
});

toggleBtnLogin.onclick = ()=>{
    if (pswrdField.type == "password"){
        pswrdField.type = "text";
        toggleBtnLogin.classList.add("active")
    }else{
        pswrdField.type = "password";
        toggleBtnLogin.classList.remove("active")
    }
}

toggleBtnCadastro.onclick = ()=>{
    if (pswrdFieldCadastro.type == "password"){
        pswrdFieldCadastro.type = "text";
        toggleBtnCadastro.classList.add("active")
    }else{
        pswrdFieldCadastro.type = "password";
        toggleBtnCadastro.classList.remove("active")
    }
}

 
 