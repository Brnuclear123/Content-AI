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
