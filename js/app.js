import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'PASTE_URL_HERE'
const supabaseKey = 'PASTE_KEY_HERE'

export const supabase = createClient(supabaseUrl, supabaseKey)
