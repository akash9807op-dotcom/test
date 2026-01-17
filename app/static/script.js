const startBtn = document.getElementById("startBtn");
const initialView = document.getElementById("initial-view");
const loadingView = document.getElementById("loading");
const resultView = document.getElementById("result");
const hackText = document.getElementById("hack-text");
const fillBar = document.querySelector(".fill");
const prankAudio = document.getElementById("prankAudio");
const body = document.body;
const card = document.querySelector(".card");

// The "Roast" Sequence
const steps = [
  { text: "Connecting to Server...", time: 800 },
  { text: "Verifying Priyanshu's Face...", time: 1500 },
  { text: "⚠️ ERROR: Face not detected...", time: 1000 },
  { text: "Scanning Browser History... 😳", time: 1500 },
  { text: "FOUND: 'How to be cool' searches...", time: 1200 },
  { text: "Uploading History to Dad's WhatsApp...", time: 2000 },
  { text: "99% Complete...", time: 1000 }
];

startBtn.addEventListener("click", async () => {
  // Hide Start, Show Loading
  initialView.classList.add("hidden");
  loadingView.classList.remove("hidden");
  
  // Play the fake hacking sequence
  let totalTime = 0;
  steps.forEach((step, index) => {
    setTimeout(() => {
      hackText.innerText = step.text;
      
      // Update progress bar
      let percentage = ((index + 1) / steps.length) * 100;
      fillBar.style.width = `${percentage}%`;
      
    }, totalTime);
    totalTime += step.time;
  });

  // THE DROP
  setTimeout(() => {
    triggerPrank();
  }, totalTime + 500);
});

function triggerPrank() {
  loadingView.classList.add("hidden");
  resultView.classList.remove("hidden");
  
  // 1. Play Audio
  prankAudio.volume = 1.0;
  // Note: Browsers sometimes block audio if user hasn't interacted enough.
  // Since they clicked "Start", it should work.
  prankAudio.play().catch(e => alert("Click the Replay button for sound!"));

  // 2. Add Visual Chaos
  body.classList.add("chaos");
  card.classList.add("shake-hard");

  // 3. Stop Chaos after 3 seconds
  setTimeout(() => {
    body.classList.remove("chaos");
    card.classList.remove("shake-hard");
  }, 3000);
}

// Replay Button
document.getElementById("replayBtn").addEventListener("click", () => {
  prankAudio.currentTime = 0;
  triggerPrank();
});
