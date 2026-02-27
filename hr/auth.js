import { supabase } from "./supabase.js";

export async function signUp(email, password) {
  return await supabase.auth.signUp({ email, password });
}

export async function login(email, password) {
  return await supabase.auth.signInWithPassword({ email, password });
}

export async function getUser() {
  const { data } = await supabase.auth.getUser();
  return data.user;
}
