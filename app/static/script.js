const startBtn = document.getElementById("startBtn");
const replayBtn = document.getElementById("replayBtn");

const prankAudio = document.getElementById("prankAudio");
const loading = document.getElementById("loading");
const result = document.getElementById("result");

async function playPrank() {
  try {
    await prankAudio.play();
    document.body.classList.add("shake");

    setTimeout(() => {
      document.body.classList.remove("shake");
    }, 800);

  } catch (err) {
    alert("Your browser blocked audio  Please allow sound.");
  }
}

startBtn.addEventListener("click", async () => {
  startBtn.style.display = "none";

  loading.classList.remove("hidden");

  // Fake loading prank 😈
  setTimeout(async () => {
    loading.classList.add("hidden");
    result.classList.remove("hidden");
    await playPrank();
  }, 1500);
});

if (replayBtn) {
  replayBtn.addEventListener("click", async () => {
    prankAudio.currentTime = 0;
    await playPrank();
  });
}