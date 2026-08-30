const usrDis = document.getElementById("d");
var islogedIN = localStorage.getItem("isSignedIn")
var usrName= localStorage.getItem("username")
if (islogedIN == "true"){
  usrDis.textContent = usrName
}else {

  window.location.href = "/"
}
async function updateImage() {
  try {
    const res = await fetch("/api/index");

    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`);
    }

    const data = await res.json();

    const img = document.getElementById("img");
    if (data.message && img) {
      img.src = data.message;
      console.log(`✅ Changed image to: ${data.message}`);
    } else {
      console.warn("⚠️ No image URL found in response.");
    }
  } catch (err) {
    console.error("❌ Failed to update image:", err);
  }
}
updateImage()
document.getElementById("ta").addEventListener("click", async () => {
window.location.href = "tagual"
});
document.getElementById("ch").addEventListener("click", async () => {
window.location.href = "check-list"
});
document.getElementById("wm").addEventListener("click", async () => {
window.location.href = "wordmaker"
});
document.getElementById("fl").addEventListener("click", async () => {
window.location.href =  "flappy"
});
document.getElementById("ai").addEventListener("click", async () => {
window.location.href = "AI"
});
document.getElementById("lo").addEventListener("click", async () => {
localStorage.removeItem("isSignedIn");
localStorage.removeItem("username");
window.location.href = "/";
});