export default async function handler(req, res) {
  const { cv_text, role } = req.body;

  const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${Deno.env.get("OPENAI_KEY")}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "gpt-4o-mini",
      messages: [{
        role: "user",
        content: `Score this CV (0-100) for role ${role}: ${cv_text}`
      }]
    })
  });

  const data = await response.json();

  res.json({ score: data.choices[0].message.content });
}
