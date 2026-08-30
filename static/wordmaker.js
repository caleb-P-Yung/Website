   var islogedIN = localStorage.getItem("isSignedIn")
  if (islogedIN != "true"){
    window.location.href = "/"
  }
  document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("p1");
    const suffixOutput = document.getElementById("output");
    const prefixOutput = document.getElementById("output");
    const onlySuffix = document.getElementById("d1");
    const onlyPrefix = document.getElementById("d2");

    input.addEventListener("keydown", async (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        const userWord = input.value.trim();
        if (!userWord) return;

        try {
          if (onlySuffix.checked && !onlyPrefix.checked) {
            const res = await fetch("/api/suffix");
            const data = await res.json();
            suffixOutput.textContent += (suffixOutput.textContent ? "\n" : "") + `${userWord}${data.message}`;
          } 
          else if (onlyPrefix.checked && !onlySuffix.checked) {
            const res = await fetch("/api/preffix");
            const data = await res.json();
            prefixOutput.textContent += (prefixOutput.textContent ? "\n" : "") + `${data.message}${userWord}`;
          } 
          else {
            const [sufRes, prefRes] = await Promise.all([
              fetch("/api/suffix"),
              fetch("/api/preffix")
            ]);

            const sufData = await sufRes.json();
            const prefData = await prefRes.json();

            suffixOutput.textContent += (suffixOutput.textContent ? "\n" : "") + `${prefData.message}${userWord}${sufData.message}`;
          }

          input.value = "";
        } catch (err) {
          console.error("Fetch error:", err);
        }
      }
    });
  });