import { supabase } from "./supabase.js";

const form = document.getElementById("applyForm");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = document.getElementById("cv").files[0];
  let cv_url = "";

  // Upload CV
  if (file) {
    const fileName = Date.now() + "_" + file.name;

    const { error } = await supabase.storage
      .from("cv_uploads")
      .upload(fileName, file);

    if (error) return alert("Upload failed");

    const { data } = supabase.storage
      .from("cv_uploads")
      .getPublicUrl(fileName);

    cv_url = data.publicUrl;
  }

  // Save application
  const { error } = await supabase.from("applications").insert([{
    full_name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    cv_url
  }]);

  if (error) alert("Error saving");
  else alert("Application submitted!");
});
