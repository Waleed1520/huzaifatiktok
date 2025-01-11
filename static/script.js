// Load the dashboard when the page loads
document.addEventListener("DOMContentLoaded", loadDashboard);

// Handle video upload
document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", document.getElementById("title").value);
    formData.append("tags", document.getElementById("tags").value);
    formData.append("video", document.getElementById("video").files[0]);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData,
    });

    const result = await response.json();
    alert(result.message);

    // Reload the dashboard
    loadDashboard();
});

// Load videos for the dashboard
async function loadDashboard() {
    const response = await fetch("/videos");
    const data = await response.json();

    const dashboard = document.getElementById("dashboard");
    dashboard.innerHTML = "";

    data.videos.forEach((video) => {
        const videoItem = document.createElement("div");
        videoItem.className = "video-item";

        videoItem.innerHTML = `
    <video controls autoplay muted>
        <source src="/uploads/${video}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <p>${video}</p>
`;

    

        dashboard.appendChild(videoItem);
    });
}
