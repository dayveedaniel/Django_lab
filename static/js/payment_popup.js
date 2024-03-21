// Get the popup and the button that opens it
var paymentPopup = document.getElementById("paymentPopup");
var makePaymentBtns = document.querySelectorAll(".make-payment");

// Get the close button and payment form elements
var closeBtn = document.querySelector(".close-btn");
var cardPaymentForm = document.getElementById("cardPaymentForm");
var qrPaymentForm = document.getElementById("qrPaymentForm");

// When the user clicks the "Make Payment" button, open the popup
makePaymentBtns.forEach(function(btn) {
  btn.onclick = function() {
    paymentPopup.style.display = "block";
  }
});

// When the user clicks the close button, close the popup
closeBtn.onclick = function() {
  paymentPopup.style.display = "none";
}

// When the user clicks outside the popup, close it
window.onclick = function(event) {
  if (event.target == paymentPopup) {
    paymentPopup.style.display = "none";
  }
}

// Show/hide payment forms based on selected payment method
var paymentMethodRadios = document.getElementsByName("paymentMethod");
paymentMethodRadios.forEach(function(radio) {
  radio.addEventListener("change", function() {
    if (this.id === "cardPayment") {
      cardPaymentForm.style.display = "block";
      qrPaymentForm.style.display = "none";
    } else {
      cardPaymentForm.style.display = "none";
      qrPaymentForm.style.display = "flex";
    }
  });
});
