// content_ai.js

document.addEventListener("DOMContentLoaded", function () {
    // Simular a geração de conteúdo ao clicar no botão "Generate Content"
    const generateButton = document.querySelector(".generate-button");
    generateButton?.addEventListener("click", () => {
        alert("Generating AI-driven content...");
        // Aqui você pode adicionar a lógica de geração de conteúdo (exemplo com dados fictícios)
        const contentArea = document.querySelector(".data-cards");
        if (contentArea) {
            contentArea.innerHTML += `
                <div class="data-card">
                    <b>✨ AI-Generated Insight</b><br>Engage teens with tech-savvy slogans!
                </div>`;
        }
    });

    // Validar seleção de localização e loja antes da geração de conteúdo
    document.querySelectorAll("select").forEach(select => {
        select.addEventListener("change", function () {
            if (select.value) {
                select.style.borderColor = "#007aff";
            }
        });
    });
});
