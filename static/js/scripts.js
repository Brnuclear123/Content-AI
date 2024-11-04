// scripts.js

// Toggle Active Link na Sidebar
document.addEventListener("DOMContentLoaded", function () {
    const sidebarLinks = document.querySelectorAll(".sidebar nav a");
    sidebarLinks.forEach(link => {
        link.addEventListener("click", () => {
            sidebarLinks.forEach(l => l.classList.remove("active"));
            link.classList.add("active");
        });
    });
});

// Exemplo de Função para Alternar Tema Claro/Escuro (opcional)
function toggleTheme() {
    document.body.classList.toggle("dark-mode");
}

document.querySelector("#theme-toggle-btn")?.addEventListener("click", toggleTheme);
