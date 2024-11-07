// Função para geração de conteúdo simulada
document.querySelector(".generate-button").addEventListener("click", () => {
    alert("Conteúdo gerado com base nos dados em tempo real!");
});

// Função para renderização da animação simulada
document.querySelector(".render-button").addEventListener("click", () => {
    alert("Renderizando animação... Aguarde!");
    document.querySelector(".animation-preview img").src = "https://via.placeholder.com/960x480";
});

// Controles de pré-visualização
document.querySelector(".play-buttons button[title='Play']").addEventListener("click", () => {
    alert("Animação reproduzida.");
});

document.querySelector(".play-buttons button[title='Pause']").addEventListener("click", () => {
    alert("Animação pausada.");
});

document.querySelector(".feedback-buttons button[title='Like']").addEventListener("click", () => {
    alert("Feedback positivo registrado!");
});

document.querySelector(".feedback-buttons button[title='Dislike']").addEventListener("click", () => {
    alert("Feedback negativo registrado!");
});

document.querySelector(".feedback-buttons button[title='Refresh']").addEventListener("click", () => {
    alert("Animação recarregada.");
});

// Ações finais: Salvar, Enviar para aprovação e Publicar
document.querySelector(".save-button").addEventListener("click", () => {
    alert("Versão salva com sucesso!");
});

document.querySelector(".send-button").addEventListener("click", () => {
    alert("Conteúdo enviado para aprovação.");
});

document.querySelector(".publish-button").addEventListener("click", () => {
    alert("Conteúdo publicado com sucesso!");
});

// Selecionando o formulário e o botão de salvar
const profileForm = document.getElementById("company-profile-form");

// Função para salvar o perfil da empresa
profileForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtenção dos valores dos campos
    const companyName = document.getElementById("company_name").value;
    const locationData = document.getElementById("location_data").value;
    const brandTone = document.getElementById("brand_tone").value;
    const targetAudience = document.getElementById("target_audience").value;
    const callToAction = document.getElementById("call_to_action").value;

    // Verificação de campos obrigatórios
    if (!companyName || !locationData || !brandTone || !targetAudience) {
        alert("Por favor, preencha todos os campos obrigatórios.");
        return;
    }

    // Simulação de salvamento do perfil (aqui entraria a chamada para API, se necessário)
    console.log("Perfil da empresa salvo:", {
        companyName,
        locationData,
        brandTone,
        targetAudience,
        callToAction
    });

    // Feedback de sucesso
    alert("Perfil da empresa salvo com sucesso!");
    profileForm.reset(); // Limpa o formulário após o salvamento
});
