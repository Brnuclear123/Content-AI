// campaign.js

document.addEventListener("DOMContentLoaded", function () {
    const campaignCards = document.querySelectorAll(".campaign-card");

    // Filtrar campanhas com base no status selecionado
    const filterDropdown = document.getElementById("campaign-status");
    filterDropdown?.addEventListener("change", function () {
        const filter = filterDropdown.value;
        campaignCards.forEach(card => {
            const status = card.dataset.status; // Presume que cada card tem data-status="active" etc.
            if (filter === "" || status === filter) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });

    // Ação de edição
    document.querySelectorAll(".edit-campaign").forEach(btn => {
        btn.addEventListener("click", function () {
            const campaignTitle = this.closest(".campaign-card").querySelector(".campaign-title").innerText;
            alert(`Editing campaign: ${campaignTitle}`);
        });
    });

    // Ação de pausar campanha
    document.querySelectorAll(".pause-campaign").forEach(btn => {
        btn.addEventListener("click", function () {
            const campaignTitle = this.closest(".campaign-card").querySelector(".campaign-title").innerText;
            alert(`Pausing campaign: ${campaignTitle}`);
            this.innerText = "▶️ Resume";
            this.classList.replace("pause-campaign", "resume-campaign");
        });
    });

    // Ação de duplicar campanha
    document.querySelectorAll(".duplicate-campaign").forEach(btn => {
        btn.addEventListener("click", function () {
            const campaignCard = this.closest(".campaign-card");
            const clone = campaignCard.cloneNode(true);
            campaignCard.parentNode.appendChild(clone);
            alert("Campaign duplicated successfully!");
        });
    });
});
