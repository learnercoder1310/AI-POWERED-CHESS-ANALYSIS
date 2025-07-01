// upload.js

document.addEventListener("DOMContentLoaded", () => {
    const fileUpload = document.getElementById("file-upload");
    const form = document.querySelector("form");
  
    form.addEventListener("submit", (event) => {
      if (!fileUpload.files.length) {
        event.preventDefault();
        alert("Please select a file before submitting.");
      }
    });
  });
  