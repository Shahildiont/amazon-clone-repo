function show() {
      alert("site under maintenance")
    }
function visit() {
    document.getElementById("popupImage").style.display = "flex";
}

function closePopup() {
    document.getElementById("popupImage").style.display = "none";
}
fetch("http://localhost:8000/api/items")
  .then(response => response.json())
  .then(data => {
    // Get all existing product containers
    const products = document.querySelectorAll(".pro1, .pro3, .pro4, .pro5");

    // Loop through data and update product details
    data.forEach((item, index) => {
      if (products[index]) {
        // Find the price container inside the product card
        const priceDiv = products[index].querySelector(".price");

        // Replace only the price text
        if (priceDiv) {
          priceDiv.innerHTML = `
            <p>Rs.
              <span class="big">${item.item_price}</span>
              M.R.P:${item.item_price * 2} (50% off) Upto 5% off with Amazon Pay
            </p>`;
        }

        // Optionally update item name if needed
        const title = products[index].querySelector("h6.pad15");
        if (title) {
          title.textContent = item.item_name;
        }
      }
    });
  })
  .catch(error => {
    console.error("Failed to load items from API:", error);
  });