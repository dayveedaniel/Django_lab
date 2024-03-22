// Get the review popup and the button that opens it
var reviewPopup = document.getElementById("reviewPopup");
var leaveReviewBtn = document.querySelectorAll(".leave-review");

var closeBtn = document.querySelector(".close-btn-re");

// When the user clicks the "Leave review" button, open the popup
leaveReviewBtn.forEach(function(btn) {
    btn.onclick = function() {
        reviewPopup.style.display = "block";
    }
})

// When the user clicks outside the popup, close it
window.onclick = function(event) {
  if (event.target == reviewPopup) {
    reviewPopup.style.display = "none";
  }
}
// When the user clicks the close button, close the popup
closeBtn.onclick = function() {
console.log("in bitton")
  reviewPopup.style.display = "none";
}