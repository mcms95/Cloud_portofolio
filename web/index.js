const p = document.querySelector("#visit-counter");
VISITORS_ENDPOINT =
  "https://3klidl8hw9.execute-api.us-east-1.amazonaws.com/test/counter";

const updateCounter = async (event) => {
  const response = await fetch(VISITORS_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const visitors = await response.json();
  p.textContent = `This page has been visited ${visitors.visits} times`;
};

window.addEventListener("DOMContentLoaded", updateCounter);