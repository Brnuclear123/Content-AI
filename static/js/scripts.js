function getSelectedTimeRanges() {
    const checkboxes = document.querySelectorAll('input[name="time-range"]:checked');
    const selectedTimeRanges = Array.from(checkboxes).map(checkbox => checkbox.value);
    console.log("Selected Time Ranges:", selectedTimeRanges);
    return selectedTimeRanges;
}


function getSelectedCampaignData() {
    const location = document.getElementById("location").value;
    const store = document.getElementById("store").value;
    const campaignDate = document.getElementById("campaign-date").value;
    console.log(`Location: ${location}, Store: ${store}, Campaign Date: ${campaignDate}`);
}

function likeOption(optionNumber) {
    console.log(`Option ${optionNumber} liked!`);
    // Aqui, você pode adicionar lógica para registrar a ação, como um contador
}

function dislikeOption(optionNumber) {
    console.log(`Option ${optionNumber} disliked!`);
    // Aqui, você pode adicionar lógica para registrar a ação, como um contador
}

function editOption(optionNumber) {
    console.log(`Option ${optionNumber} selected for editing.`);
    // Aqui, você pode adicionar lógica para abrir uma seção de edição
}

function renderAnimation() {
    console.log("Rendering animation...");
    // Aqui, você pode adicionar lógica para renderizar a animação
}
