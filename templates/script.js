function getSentiment(event, text) {
    // Schutz: Falls kein Event übergeben oder falscher Tastendruck
    if (!event || event.key !== "Enter" || !text) {
        const answer = document.getElementById("answer");
        if (answer) answer.innerHTML = '';
        return;
    }

    const answer = document.getElementById("answer");
    const answerPart = document.getElementById("answerPart");

    if (answerPart) {
        answerPart.style.visibility = "visible";
    }

    fetch('/sentiment?' + new URLSearchParams({ text: text }), {
        method: 'GET',
    }).then(response => {
        console.log("Antwort erhalten:", response);
        return response.text();
    }).then(text => {
        if (answer) answer.innerHTML = text;
    }).catch(error => {
        console.error("Fehler beim Abrufen des Sentiments:", error);
        if (answer) answer.innerHTML = "Fehler beim Abrufen.";
    });
}