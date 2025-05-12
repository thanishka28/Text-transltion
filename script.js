function showTextTranslation() {
    document.getElementById("text-translation").style.display = "block";
    document.getElementById("image-upload").style.display = "none";
}

function showImageUpload() {
    document.getElementById("text-translation").style.display = "none";
    document.getElementById("image-upload").style.display = "block";
}

// Function to translate input text
function translateText() {
    let inputText = document.getElementById("input-text").value;
    let targetLanguage = document.getElementById("text-language").value;

    if (inputText.trim() === "") {
        alert("Please enter text to translate.");
        return;
    }

    fetch("http://127.0.0.1:5000/translate-text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText, language: targetLanguage })
    })
    .then(response => response.json())
    .then(data => {
        if (data.translated_text) {
            document.getElementById("translated-text").value = data.translated_text;
        } else {
            alert("Translation failed: " + (data.error));
        }
    })
    .catch(error => alert("Error: " + error));
}

// Function to extract text from an image
function extractTextFromImage() {
    let imageInput = document.getElementById("image-input").files[0];

    if (!imageInput) {
        alert("Please upload an image first.");
        return;
    }

    let formData = new FormData();
    formData.append("image", imageInput);

    fetch("http://127.0.0.1:5000/extract-text", {
        method: "POST",
        body: formData,
        headers: {
            "Accept": "application/json"
        }
    })
    .then(response => response.json()) 
    .then(data => {
        if (data.extracted_text) {
            document.getElementById("extracted-text").value = data.extracted_text;
        } else {
            alert("Text extraction failed: " + (data.error));
        }
    })
    .catch(error => {
        console.error("Fetch Error:", error); 
        alert("Error: " + error);
    });
}

// Function to translate the extracted text
function translateExtractedText() {
    let extractedText = document.getElementById("extracted-text").value;
    let targetLanguage = document.getElementById("image-language").value;

    if (extractedText.trim() === "") {
        alert("No text extracted from the image.");
        return;
    }

    fetch("http://localhost:5000/translate-extracted-text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: extractedText, language: targetLanguage })
    })
    .then(response => response.json())
    .then(data => {
        if (data.translated_text) {
            document.getElementById("image-text").value = data.translated_text;
        } else {
            alert("Translation failed: " + (data.error));
        }
    })
    .catch(error => alert("Error: " + error));
}
