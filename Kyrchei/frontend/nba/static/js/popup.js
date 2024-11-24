function showPopup(message) {
  var popup = document.getElementById("popup");
  var messageElement = document.getElementById("popup-message");

  messageElement.textContent = message;


  popup.style.opacity = '1';
  popup.style.visibility = 'visible';


  setTimeout(() => {
    popup.style.opacity = '0';
    setTimeout(() => {
      popup.style.visibility = 'hidden';
    }, 500);
  }, 3000);
}

document.addEventListener("DOMContentLoaded", () => {
  gsap.from(".player-tile", {
    opacity: 0,
    y: 20,
    duration: 0.6,

  });
  gsap.from(".team-tile", {
    opacity: 0,
    y: 20,
    duration: 0.6,

  });
});

document.querySelectorAll(".team-form").forEach(form => {
  form.addEventListener("submit", async function(event) {
    event.preventDefault();
    var status = document.getElementById("my-form-status");
    var data = new FormData(event.target);

    fetch(event.target.action, {
      method: form.method,
      body: data,
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'Accept': 'application/json'
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to save team');
      }
    })
    .then(data => {
      if (data.message) {
        showPopup(data.message);
      } else if (data.error) {
        showPopup(data.error);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      showPopup('An error occurred while saving the team.');
    });


  });
});

document.querySelectorAll(".team-delete-form").forEach(form => {

  form.addEventListener("submit", async function(event) {
    event.preventDefault();
    var status = document.getElementById("my-form-status");
    var data = new FormData(event.target);
    const tile = form.closest(".player-tile")


    fetch("/dteams", {
      method: form.method,
      body: data,
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'Accept': 'application/json'
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to delete team');
      }
    })
    .then(data => {
      if (data.message) {
        gsap.to(tile, {
          opacity: 0,
          scale: 0,
          duration: 0.5,
          onComplete: () => tile.remove()
        });
        showPopup(data.message);
      } else if (data.error) {
        showPopup(data.error);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      showPopup('An error occurred while deleting the team.');
    });
  });
});


document.querySelectorAll(".player-delete-form").forEach(form => {

  form.addEventListener("submit", async function(event) {
    event.preventDefault();
    var status = document.getElementById("my-form-status");
    var data = new FormData(event.target);
    const tile = form.closest(".team-tile")

    fetch("/dplayers", {
      method: form.method,
      body: data,
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'Accept': 'application/json'
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to delete team');
      }
    })
    .then(data => {
      if (data.message) {
        gsap.to(tile, {
          opacity: 0,
          scale: 0,
          duration: 0.5,
          onComplete: () => tile.remove()

        });
        showPopup(data.message);
      } else if (data.error) {
        showPopup(data.error);
      }
    })
    .catch(error => {
      console.error('Error:', error);
      showPopup('An error occurred while deleting the team.');
    });
  });
});


