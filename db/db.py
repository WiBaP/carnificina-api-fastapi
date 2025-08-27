# db/db.py
import os
from supabase import create_client, Client

# --- Configuração do Supabase ---
SUPABASE_URL = "https://akkerkqlhntiaipqezbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFra2Vya3FsaG50aWFpcHFlemJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYwMDEyNTYsImV4cCI6MjA3MTU3NzI1Nn0.lk0qluK440e3nWqMqAO3TSSo-bEj8IimGOeWgaFbVa4"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
